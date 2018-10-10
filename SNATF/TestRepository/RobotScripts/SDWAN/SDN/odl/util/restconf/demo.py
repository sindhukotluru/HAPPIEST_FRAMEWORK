import xlwings as xw
import logging
from xlrd import open_workbook
from xlutils.copy import copy
import sys
import json
import os
import sys

ROOT_DIR = r'D:\Karthik\CodeBase\E_R&D'
sys.path.append(ROOT_DIR)

if os.path.exists(ROOT_DIR):
    from SDN.odl.util import template_utils
    from SDN.odl.interface.restconf.resource_instances import INSTANCES
    from SDN import config
    from SDN.odl.util import json_loader
else:
    sys.exit()

msg_constants = {'test_id': None, 'resource': None, 'method': None}


class APIFileTemplate(object):
    HEADER_ROW_INDEX = 3
    RESPONSE_SHEET_EXT = ".response"
    REQUEST_SHEET_EXT = ".request"
    PARAMETERS_COLUMN_NAME = "parameters"


def initialize_logger():
    """

    :return:
    """
    msg_format = '%(asctime)s %(test_id)s %(resource)s %(method)s %(levelname)s %(message)s'
    logging.basicConfig(filename=ROOT_DIR + os.path.sep + r'SDN\odl\util\restconf\demo.log',
                        level=logging.DEBUG, format=msg_format)


def load_request_parameters(request_params_column, source_file):
    """

    :param request_params_column:
    :param source_file:
    :return:
    """
    sheet_name = request_params_column.rsplit(".", 1)[0]
    payload_colname = request_params_column.rsplit(".", 1)[1]

    rb = open_workbook(filename=source_file)
    sh = rb.sheet_by_name(sheet_name)

    header_row = sh.row_values(APIFileTemplate.HEADER_ROW_INDEX)

    param_col_index = header_row.index("parameters")
    payload_col_index = header_row.index(payload_colname)
    request_param_names = sh.col_values(param_col_index, APIFileTemplate.HEADER_ROW_INDEX + 1)
    request_param_values = sh.col_values(payload_col_index, APIFileTemplate.HEADER_ROW_INDEX + 1)

    logging.info("Request Parameter Names : {0}".format(request_param_names), extra=msg_constants)
    logging.info("Request Parameter Values : {0}".format(request_param_values), extra=msg_constants)

    return dict(zip(request_param_names, request_param_values))


def update_response_parameters(response_params, source_file, response_sheet_name, column_name):
    """

    :param response_params:
    :param source_file:
    :param response_sheet_name:
    :param column_name:
    :return:
    """

    logging.info("Updating Response Sheet : {0}".format(response_sheet_name), extra=msg_constants)
    rb = open_workbook(filename=source_file, formatting_info=True)
    sh = rb.sheet_by_name(response_sheet_name)

    header_index = APIFileTemplate.HEADER_ROW_INDEX
    header_row = sh.row_values(header_index)
    logging.debug("Header Row : {0}".format(header_row), extra=msg_constants)
    param_col_index = header_row.index(APIFileTemplate.PARAMETERS_COLUMN_NAME)
    # Check if the column name already exists in the header row.
    if column_name not in header_row:
        header_row.append(column_name)
    value_col_index = header_row.index(column_name)
    logging.debug("Parameter Name Index :{0} | Parameter Value Index : {1}".format(param_col_index, value_col_index),
                  extra=msg_constants)
    # Check if the response parameters are present in the sheet under "parameter" column
    response_params_names = sh.col_values(param_col_index, header_index + 1)
    response_params_values = sh.col_values(value_col_index, header_index + 1)

    # Initialize all parameter values to "" to erase all values from last execution
    response_params_values = ["" for value in response_params_values]

    #for response_param, value in response_params:
    for response_param, value in response_params.iteritems():
        if response_param not in response_params_names:
            response_params_names.append(response_param)
            response_params_values.append("")
        response_params_values[response_params_names.index(response_param)] = value

    logging.info("Response Parameter Names : {0}".format(response_params_names), extra=msg_constants)
    logging.info("Response Parameter Values : {0}".format(response_params_values), extra=msg_constants)

    # Copy entire workbook to be updated
    wb = copy(rb)
    logging.debug("Datasource Sheets : {0}".format([sh.name for sh in rb.sheets()]), extra=msg_constants)
    response_sheet_handle = wb.get_sheet([sh.name for sh in rb.sheets()].index(response_sheet_name))
    logging.debug("Response Sheet Object : {0}".format(response_sheet_handle), extra=msg_constants)
    row_index = 1
    for param, value in zip(response_params_names, response_params_values):
        response_sheet_handle.write(header_index + row_index, param_col_index, param)
        response_sheet_handle.write(header_index + row_index, value_col_index, value)
        row_index += 1
    try:
        wb.save(source_file)
    except IOError as e:
        logging.error("Program Exception : {0}".format(e.message), extra=msg_constants)


@xw.func
def run_api_test(test_id, resource, endpoint_url, method, request_params,
                 expected_response_params, expected_response_code, data_source_file):
    """

    :param test_id:
    :param resource:
    :param endpoint_url:
    :param method:
    :param request_params:
    :param expected_response_params:
    :param expected_response_code:
    :param data_source_file:
    :return:
    """

    initialize_logger()
    test_status = True
    msg_constants['test_id'] = test_id
    msg_constants['resource'] = resource
    msg_constants['method'] = method

    logging.info("Calling service Endpoint URL = {0}".format(endpoint_url), extra=msg_constants)
    logging.info("Request Parameter Column Reference = {0}".format(request_params), extra=msg_constants)
    logging.info("Expected Response Parameter Column Reference = {0}".format(expected_response_params),
                 extra=msg_constants)
    logging.info("Expected Response Code = {0}".format(expected_response_code), extra=msg_constants)
    logging.info("Resource Payload Parameter Source File = {0}".format(data_source_file), extra=msg_constants)

    if method in ("POST", "PUT"):
        # Load request parameters from the resource.request.payload sheet
        request_params_payload = load_request_parameters(request_params, data_source_file)

    # Call the setter methods for the attributes using their respective class objects.
    # 1. Get the Parent Resource class name
    resource_class_name = template_utils.format_attribute_name(resource)

    # 2. Get the parent class instance from the resource_instances class repo
    instance_repo = INSTANCES()
    resource_instance = instance_repo.get_resource_instance(resource_class_name)

    if method in ("POST", "PUT"):
        # 3. Find and Dynamically call the setter methods based on the parameter name
        logging.debug("Resource Class attributes = {0}".format(dir(resource_instance)), extra=msg_constants)

        for param_name in request_params_payload:
            formatted_param_name = template_utils.format_attribute_name(param_name)
            sub_param_list = formatted_param_name.split(".", 1)[1].split(".")
            setter_method_name = "set_" + sub_param_list[-1]
            attribute_name = ".".join(sub_param_list[:-1] + [setter_method_name])

            try:
                attr_object = resource_instance
                for attribute in attribute_name.split(".")[:-1]:
                    logging.debug("Attribute Name : {0}".format(attribute), extra=msg_constants)
                    attr_object = getattr(attr_object, attribute)
                    logging.debug("Resource Child Class Attributes : {0}".format(dir(attr_object)), extra=msg_constants)

                logging.info("Calling Setter Method: {0} for Parameter: {1}".format(
                    setter_method_name, attribute_name), extra=msg_constants)
                setter_func = getattr(attr_object, setter_method_name)
                setter_func(request_params_payload[param_name])
            except AttributeError as ae:
                logging.error(ae.message, extras=msg_constants)

        # 4. Get the JSON Payload values post calling setters methods
        logging.info("Payload params: {0}".format(resource_instance.get_payload()), extra=msg_constants)

    if method == 'GET' and request_params != "":
        # Load request parameters from the resource.request.payload sheet
        request_params_payload = load_request_parameters(request_params, data_source_file)
        logging.debug("Request Parameter Payload : {0}".format(request_params_payload), extra=msg_constants)
        # Replace value query parameter in the URL from the request payload list
        for param_name in request_params_payload:
            sub_param_name = param_name.rsplit(".", 1)[1]
            if '{' + sub_param_name + '}' in endpoint_url:
                endpoint_url = endpoint_url.replace('{' + sub_param_name + '}', request_params_payload[param_name])

    # 5. Set the REST URL for the resource
    url = "http://{0}:{1}/{2}".format(config.CONTROLLER_IP, config.RESTCONFPORT, config.REST_CON + endpoint_url)
    logging.info("Setting Endpoint URL : {0}".format(url), extra=msg_constants)
    getattr(resource_instance, 'set_rest_url')(value=url)

    # 6. Call the corresponding HTTP method
    method_name = ""
    if method == "POST":
        method_name = "create_" + resource_class_name.lower()
    elif method == "GET":
        method_name = "get_" + resource_class_name.lower()
    elif method == "DELETE":
        method_name = "delete_" + resource_class_name.lower()

    logging.info("Calling method :{0}".format(method_name), extra=msg_constants)
    try:
        http_func = getattr(resource_instance, method_name)
        response_code, response_text = http_func()
        logging.info("Actual Response Code : {0}".format(response_code), extra=msg_constants)
        logging.info("Actual Response Text : {0}".format(response_text), extra=msg_constants)
    except AttributeError as ae:
        logging.error(ae.message, extra=msg_constants)

    if str(response_text).strip() != "":
        try:
            response_text = json.loads(response_text)
            logging.debug("Received Response JSON Message : {0} of type {1}".format(response_text, type(response_text)),
                          extra=msg_constants)
            json_params = json_loader.convert_json_to_param_dot_notation(data=response_text, json_params={}, parent=None)
            logging.debug("Response JSON Params : {0}".format(json_params), extra=msg_constants)

            # Update the Response Sheet with Parameter values
            response_sheet_name = resource.lower() + APIFileTemplate.RESPONSE_SHEET_EXT
            update_response_parameters(response_params=json_params, source_file=data_source_file,
                                       response_sheet_name=response_sheet_name, column_name=test_id.upper())

            # Compare the Actual and Expected response in case of GET request
            if method == "GET":
                if json_params != request_params_payload:
                    test_status = False

        except ValueError as e:
            logging.error(e.message, extra=msg_constants)
    else:
        logging.info("Blank response message received", extra=msg_constants)

    logging.info("Test Execution ended with Status:{0} and Response Code: {1}".format(test_status, response_code),
                 extra=msg_constants)

    return response_code

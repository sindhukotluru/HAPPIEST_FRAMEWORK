from Config import ControllerConfig
from copy import deepcopy
import json
from Supporting_Libs import rest_session


def perform_odl_snmp_operation(**kwargs):
    """
    Author: Sirish
    Date: 11/07/2018
    Prepare the RESTCONF input and send for GET operation
    IP,OID,COMMUNITY and VALUE/GET_TYPE
    :return: SNMP-GET output
    """
    input = ControllerConfig.SNMP_INPUT
    payload = deepcopy(input)
    payload['input']['ip-address'] = kwargs['IP']
    payload['input']['oid'] = kwargs['OID']
    payload['input']['community'] = kwargs['COMMUNITY']
    if 'VALUE' in kwargs:
        snmp_operation = 'snmp-set'
        payload['input']['value'] = payload['input'].pop('get-type')
        payload['input']['value'] = kwargs['VALUE']
    else:
        snmp_operation = 'snmp-get'
        get_type = kwargs['GETTYPE'] if 'GETTYPE' in kwargs else 'GET'
        payload['input']['get-type'] = get_type
    API_URL = ControllerConfig.SNMP_API+snmp_operation
    rest_session.send_post_request(url=API_URL, data=json.dumps(payload))
    return rest_session.response_code, arrange_snmp_result(rest_session.response_as_text)

def arrange_snmp_result(response_text):
    arranged_output = ''
    output = ''
    if len(response_text) != 0:
        response_text = json.loads(response_text)
        if 'output' in response_text:
            if 'results' in response_text['output']:
                output = response_text['output']['results']
        elif 'errors' in response_text:
            arranged_output += "ERROR MESSAGE = %s"%response_text["errors"]["error"][0]["error-message"]
        else: output = {}
        if output:
            for entry in output:
                arranged_output += "%s = %s\n"%(entry[entry.keys()[0]],entry[entry.keys()[-1]])

    else: arranged_output = 'No Return data'
    return arranged_output

import json
import re
import unittest
from pprint import pprint

from odl.util import json_loader

from odl.interface.restconf import variables
from odl.util.rest_utils import REST


class TestODLResource(unittest.TestCase):

    def setUp(self):

        self.odlrest = REST(user="admin", password="admin")

    def get_resource_apis_list(self):
        self.api_index_url = r'http://{0}:{1}/apidoc/apis'.format(variables.ODL_SYSTEM_IP_1, variables.RESTCONFPORT)
        self.odlrest.send_get_request(url=self.api_index_url)
        pprint(self.odlrest.response_as_text)
        response_json = json_loader.load(self.odlrest.response_as_text)
        api_list = []
        for apis in response_json["apis"]:
            api_list.append(apis["path"])
        return api_list

    def get_resource_names(self):
        api_list = self.get_resource_apis_list()
        resources = []
        for url in api_list:
            resources.append(url.rsplit("/", 1)[1].split("(")[0])
        return resources

    def get_resource_api_mapping(self):
        api_list = self.get_resource_apis_list()
        resource_apis = {url.rsplit("/", 1)[1].split("(")[0]:url for url in api_list}
        return resource_apis

    def get_resource_apis(self, resource_url):
        self.odlrest.send_get_request(resource_url)
        response_json = json_loader.load(self.odlrest.response_as_text)
        api_list = []
        for apis in response_json["apis"]:
           api_list.append(apis["path"])
        return list(set(api_list))

    def get_config_params_from_apis(self, url, http_method="POST"):
        config_object_list = []
        self.odlrest.send_get_request(url)
        response_json = json_loader.load(self.odlrest.response_as_text)
        if "apis" in response_json:
            for api in response_json["apis"]:
                if api["path"] == "/config/":
                    for oper in api["operations"]:
                        if oper["method"] == http_method:
                            config_object_list = [param["type"] for param in oper["parameters"]]
        return config_object_list

    def get_config_properties_for_model(self, model_name, url):
        self.odlrest.send_get_request(url)
        response_json = json_loader.load(self.odlrest.response_as_text)
        properties = {}
        if "models" in response_json:
            regexp = "\(config\){0}POST".format(model_name.replace("(config)",""))
            for prop in response_json["models"].keys():
                if re.search(regexp, prop) is not None:
                    properties = response_json["models"][prop]["properties"]
        return properties

    def get_model_properties(self, properties):

        model_properties = {}
        for props in properties:
            if ("items" in properties[props]) and ("$ref" in properties[props]["items"]):
                model_properties[props] = properties[props]["items"]["$ref"]
            else:
                model_properties[props] = ""
        return model_properties


    def update_json(self, dict_json, url):
        pprint(dict_json)
        for config_model in dict_json:
            # Get parameters for only (config) type properties
            if dict_json[config_model] != "":
                model_properties = self.get_config_properties_for_model(model_name=config_model, url=url)
                print("\n*** PROPERTIES for CONFIG MODEL = {0}".format(config_model))
                pprint(model_properties)
                properties = self.get_model_properties(properties=model_properties)
                if properties:
                    dict_json[config_model] = properties
                else:
                    dict_json[config_model] = ""
                #Process (config) type properties parameters for child (config) objects
                for params in dict_json[config_model]:
                    if "(config)" in dict_json[config_model][params]:
                        print("CONFIG TYPE PARAMETERS = ", dict_json[config_model][params])
                        self.update_json(dict_json[config_model], url)

    @unittest.skip("Skipped")
    def test_get_odl_resource_apis(self):
       print(self.get_resource_apis_list())

    @unittest.skip("Skipped")
    def test_get_resource_names(self):
        print(self.get_resource_names())

    @unittest.skip("Skipped")
    def test_get_resource_mapping(self):
        pprint(self.get_resource_api_mapping())

    @unittest.skip("Skipped")
    def test_resource_apis(self):
        for resource, url in self.get_resource_api_mapping().iteritems():
            print("\n RESOURCE :: " + resource)
            print(self.get_resource_apis(resource_url=url))

    def test_get_configuration_objects(self):
        lst_of_skipped_resources = ['opendaylight-action-types', 'network-topology', 'ietf-interfaces', 'XSQL',
                                    'entity-owners', 'bgp']

        lst_of_test_resources = ["bgp"]

        for resource, url in self.get_resource_api_mapping().iteritems():
            # Skipping some resources
            #if resource not in lst_of_skipped_resources:
            #if resource in lst_of_skipped_resources:
            if resource in lst_of_test_resources:
                print("\n RESOURCE :: " + resource)
                print url
                dict_resource_json = {}
                dict_resource_json[resource] = {}
                #GET the APIs and Model JSON for the Resource
                config_resource_models = self.get_config_params_from_apis(url=url)
                for model_name in config_resource_models:
                    dict_resource_json[resource][model_name] = {}
                print("BEFORE UPDATE")
                pprint(dict_resource_json)
                self.update_json(dict_resource_json[resource], url)
                print("AFTER UPDATE")
                pprint(dict_resource_json)
                # Dump the JSON to a file
                for model_name in config_resource_models:
                    output_file = r'C:\Users\Karthik.prakash\PycharmProjects\SDN\test\data\{0}.json'.format(model_name)
                    json.dump(dict_resource_json[resource][model_name], open(output_file, "w"),
                              indent=4, sort_keys=True, separators=(',', ': '), ensure_ascii=True)

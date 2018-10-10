import os
import unittest
from pprint import pprint

from SDN.odl.util import json_loader


class TestUtils(unittest.TestCase):

    @unittest.skip("Skipped")
    def test_json_loader(self):
        json_file = os.path.join(os.getcwd(), r'data\vpn_instance.json')
        pprint(json_loader.load(json_file))

    @unittest.skip("Skipped")
    def test_dict_to_class_attrs(self):
        json_file = os.path.join(os.getcwd(), r'data\vpn_instance.json')
        json_loader.dict_to_class_attrs(json_loader.load(json_file))

    def test_json_to_dot_notation(self):
        json_file = os.path.join(os.getcwd(), r'data\vpn_instance.json')
        json_params = json_loader.convert_json_to_param_dot_notation(json_loader.load(json_file))
        pprint(json_params)


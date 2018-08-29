import os
import unittest
from pprint import pprint

from jinja2 import Environment, BaseLoader
from util import json_loader

from odl import constants
from odl.util import template_utils


class TestTemplate(unittest.TestCase):

    #@unittest.skip("Test Skipped")
    def test_vpn_template(self):
        template_file = os.path.join(constants.ROOT_DIR, r'template\restconf\vpn_instance.template')
        json_file = os.path.join(constants.ROOT_DIR, r'test\data\vpn_instance_org.json')
        json_file = os.path.join(constants.ROOT_DIR, r'test\data\(config)vpn-instances.json')
        vpn_instance_class_file = os.path.join(constants.ROOT_DIR, r'restconf\api\{0}.py'.format(
            os.path.split(json_file)[1].strip(".json")))

        print(json_file)
        class_attrs = json_loader.dict_to_class_attrs(json_loader.load(json_file))

        env = Environment(loader=BaseLoader(),trim_blocks=True)
        env.filters['format_attribute_name'] = template_utils.format_attribute_name
        template = env.from_string(open(template_file).read())
        class_code = template.render(class_attrs=class_attrs)

        with open(vpn_instance_class_file, "w") as fh:
            fh.write(class_code)

    @unittest.skip("Test Skipped")
    def test_multiple_json_templates(self):

        template_file = os.path.join(constants.ROOT_DIR, r'template\restconf\vpn_instance.template')

        lst_of_json_templates = [r'data\vpn_instance.json', r'data\ietf_interface.json', r'data\vpn_interface.json']
        restconf_interface = os.path.join(constants.ROOT_DIR, 'restconf')

        for template in lst_of_json_templates:
            json_file = os.path.join(os.getcwd(), template)
            class_attrs = json_loader.dict_to_class_attrs(json_loader.load(json_file), class_attrs={})
            pprint(class_attrs)
            env = Environment(loader=BaseLoader(), trim_blocks=True)
            env.filters['format_attribute_name'] = template_utils.format_attribute_name
            template = env.from_string(open(template_file).read())
            class_code = template.render(class_attrs=class_attrs)

            with open(restconf_interface + os.path.sep + os.path.split(json_file)[1].strip('.json') + ".py", "w") as fh:
                fh.write(class_code)


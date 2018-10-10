import os
import re
import argparse
from jinja2 import Environment, BaseLoader

from SDN.odl.util import json_loader
from SDN.odl.util import template_utils


def generate_resource_class(template_file, json_file, class_file):

    class_attrs = json_loader.dict_to_class_attrs(json_loader.load(json_file))

    env = Environment(loader=BaseLoader(), trim_blocks=True)
    env.filters['format_attribute_name'] = template_utils.format_attribute_name
    template = env.from_string(open(template_file).read())
    class_code = template.render(class_attrs=class_attrs)

    with open(class_file, "w") as fh:
        fh.write(class_code)


if __name__ == '__main__':
    options = argparse.ArgumentParser()

    options.add_argument('--template', dest='template_file', help='path of the Jinja template file')
    options.add_argument('--json_file', dest='json_file', help='path of the json schema file for the ODL resource')
    options.add_argument('--output', dest='class_file', help='path of the python class file to be generated')

    args = vars(options.parse_args())
    regexp = r'\(config\)(.*).json$'
    pattern = re.compile(regexp)
    class_file_name = pattern.findall(os.path.split(args['json_file'])[1])[0]

    generate_resource_class(template_file=args['template_file'],
                            json_file=args['json_file'],
                            class_file=(args['class_file'] + os.path.sep +
                                        template_utils.format_attribute_name(class_file_name) + ".py"))

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

def get_json_files_list():
    json_path = r'/home/test/repo_12_04_17/SDN/odl/interface/restconf/json/new_json_files'
    # json_path = r'D:\SDWAN\SDN\odl\interface\restconf\json'

    dirListing = os.listdir(json_path)
    jsonFiles = []
    for item in dirListing:
        if ".json" in item:
            #jsonFiles.append(json_path+'\\'+item)     # This is for windows env
            jsonFiles.append(json_path + '/' + item)    # This is for linux env
    #print "JSONFILES:", jsonFiles
    return jsonFiles

def create_class(arg, file):
    regexp = r'\(config\)(.*).json$'
    pattern = re.compile(regexp)

    #class_file_name = pattern.findall(os.path.split(args['json_file'])[1])[0]
    class_file_name = pattern.findall(os.path.split(file)[1])[0]
    generate_resource_class(template_file=arg['template_file'],
                            json_file=file,
                            class_file=(arg['class_file'] + os.path.sep +
                                        template_utils.format_attribute_name(class_file_name) + ".py"))


if __name__ == '__main__':
    options = argparse.ArgumentParser()

    options.add_argument('--template', dest='template_file', help='path of the Jinja template file')
    options.add_argument('--json_file', dest='json_file', default='all', help='path of the json schema file for the ODL resource. default "all"')
    options.add_argument('--output', dest='class_file', help='path of the python class file to be generated')

    args = vars(options.parse_args())

    #regexp = r'\(config\)(.*).json$'
    #pattern = re.compile(regexp)

    if re.search("all", args['json_file']):
        json_list = get_json_files_list()
        for test in json_list:
            #print "TEST:", test
            create_class(args, test)
    else:
        #print "TEST:", args['json_file']
        create_class(args, args['json_file'])

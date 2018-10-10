import json
import os


def load(source):
    if os.path.isfile(source) is True:
        with open(source) as json_file:
            data = json.load(json_file)
            return data
    else:
        return json.loads(source)


def dict_to_class_attrs(data, class_attrs={}):
    for key, value in data.iteritems():
        if isinstance(value, dict):
            class_attrs[key] = data[key].keys()
            dict_to_class_attrs(value, class_attrs=class_attrs)
    return class_attrs


def convert_json_to_param_dot_notation(data, parent=None, json_params={}):

    if isinstance(data, str):
        data = json.loads(data)

    for key, value in data.items():
        if parent is None:
            parent = key
            param = parent
        else:
            param = parent + "." + key

        if isinstance(value, list):
            value = value[0]
            if isinstance(value, dict):
                convert_json_to_param_dot_notation(data=value, parent=param, json_params=json_params)
        elif isinstance(value, dict):
            convert_json_to_param_dot_notation(data=value, parent=param, json_params=json_params)
        else:
            #json_params.append((param, value))
            json_params[param] = str(value)
    return json_params
from copy import deepcopy
import json
from SDN.odl.interface.restconf import rest_session



class INSTRUCTION(object):

    _INSTRUCTION_FIELD = "instruction"
    _ORDER_FIELD = "order"
    _APPLY_ACTIONS_FIELD = "apply-actions"

    def __init__(self):
        self._template = {}
        self._template[self._ORDER_FIELD] = None
        self._template[self._APPLY_ACTIONS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._apply_actions = APPLY_ACTIONS()

    @property
    def apply_actions(self):
        return self._apply_actions

    def set_order(self, value):
        self._template[self._ORDER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._APPLY_ACTIONS_FIELD] = self.apply_actions.get_template(default=default)
            return self._default_template
        else:
            self._template[self._APPLY_ACTIONS_FIELD] = self.apply_actions.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        apply_actions_payload = self.apply_actions.get_payload()
        if apply_actions_payload:
            payload[self._APPLY_ACTIONS_FIELD] = apply_actions_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_instruction(self):

        payload = {self._INSTRUCTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_instruction(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_instruction(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ETHERNET_MATCH(object):

    _ETHERNET_MATCH_FIELD = "ethernet-match"
    _ETHERNET_TYPE_FIELD = "ethernet-type"

    def __init__(self):
        self._template = {}
        self._template[self._ETHERNET_TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ethernet_type = ETHERNET_TYPE()

    @property
    def ethernet_type(self):
        return self._ethernet_type

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ETHERNET_TYPE_FIELD] = self.ethernet_type.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ETHERNET_TYPE_FIELD] = self.ethernet_type.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ethernet_type_payload = self.ethernet_type.get_payload()
        if ethernet_type_payload:
            payload[self._ETHERNET_TYPE_FIELD] = ethernet_type_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ethernet_match(self):

        payload = {self._ETHERNET_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ethernet_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ethernet_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class IP_MATCH(object):

    _IP_MATCH_FIELD = "ip-match"
    _IP_PROTOCOL_FIELD = "ip-protocol"

    def __init__(self):
        self._template = {}
        self._template[self._IP_PROTOCOL_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_ip_protocol(self, value):
        self._template[self._IP_PROTOCOL_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ip_match(self):

        payload = {self._IP_MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ip_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ip_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class FLOW(object):

    _FLOW_FIELD = "flow"
    _PRIORITY_FIELD = "priority"
    _TABLE_ID_FIELD = "table_id"
    _ID_FIELD = "id"
    _MATCH_FIELD = "match"
    _INSTRUCTIONS_FIELD = "instructions"

    def __init__(self):
        self._template = {}
        self._template[self._PRIORITY_FIELD] = None
        self._template[self._TABLE_ID_FIELD] = None
        self._template[self._ID_FIELD] = None
        self._template[self._MATCH_FIELD] = None
        self._template[self._INSTRUCTIONS_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._match = MATCH()
        self._instructions = INSTRUCTIONS()

    @property
    def match(self):
        return self._match

    @property
    def instructions(self):
        return self._instructions

    def set_priority(self, value):
        self._template[self._PRIORITY_FIELD] = value

    def set_table_id(self, value):
        self._template[self._TABLE_ID_FIELD] = value

    def set_id(self, value):
        self._template[self._ID_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._MATCH_FIELD] = self.match.get_template(default=default)
            self._default_template[self._INSTRUCTIONS_FIELD] = self.instructions.get_template(default=default)
            return self._default_template
        else:
            self._template[self._MATCH_FIELD] = self.match.get_template()
            self._template[self._INSTRUCTIONS_FIELD] = self.instructions.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        match_payload = self.match.get_payload()
        if match_payload:
            payload[self._MATCH_FIELD] = match_payload
        instructions_payload = self.instructions.get_payload()
        if instructions_payload:
            payload[self._INSTRUCTIONS_FIELD] = instructions_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_flow(self):

        payload = {self._FLOW_FIELD: self.get_payload()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_flow(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_flow(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class OUTPUT_ACTION(object):

    _OUTPUT_ACTION_FIELD = "output-action"
    _MAX_LENGTH_FIELD = "max-length"
    _OUTPUT_NODE_CONNECTOR_FIELD = "output-node-connector"

    def __init__(self):
        self._template = {}
        self._template[self._MAX_LENGTH_FIELD] = None
        self._template[self._OUTPUT_NODE_CONNECTOR_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_max_length(self, value):
        self._template[self._MAX_LENGTH_FIELD] = value

    def set_output_node_connector(self, value):
        self._template[self._OUTPUT_NODE_CONNECTOR_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_output_action(self):

        payload = {self._OUTPUT_ACTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_output_action(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_output_action(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ETHERNET_TYPE(object):

    _ETHERNET_TYPE_FIELD = "ethernet-type"
    _TYPE_FIELD = "type"

    def __init__(self):
        self._template = {}
        self._template[self._TYPE_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None

    def set_type(self, value):
        self._template[self._TYPE_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            return self._default_template
        else:
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_ethernet_type(self):

        payload = {self._ETHERNET_TYPE_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_ethernet_type(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_ethernet_type(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class APPLY_ACTIONS(object):

    _APPLY_ACTIONS_FIELD = "apply-actions"
    _ACTION_FIELD = "action"

    def __init__(self):
        self._template = {}
        self._template[self._ACTION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._action = ACTION()

    @property
    def action(self):
        return self._action

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._ACTION_FIELD] = self.action.get_template(default=default)
            return self._default_template
        else:
            self._template[self._ACTION_FIELD] = self.action.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        action_payload = self.action.get_payload()
        if action_payload:
            payload[self._ACTION_FIELD] = action_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_apply_actions(self):

        payload = {self._APPLY_ACTIONS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_apply_actions(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_apply_actions(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class ACTION(object):

    _ACTION_FIELD = "action"
    _OUTPUT_ACTION_FIELD = "output-action"
    _ORDER_FIELD = "order"

    def __init__(self):
        self._template = {}
        self._template[self._OUTPUT_ACTION_FIELD] = None
        self._template[self._ORDER_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._output_action = OUTPUT_ACTION()

    @property
    def output_action(self):
        return self._output_action

    def set_order(self, value):
        self._template[self._ORDER_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._OUTPUT_ACTION_FIELD] = self.output_action.get_template(default=default)
            return self._default_template
        else:
            self._template[self._OUTPUT_ACTION_FIELD] = self.output_action.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        output_action_payload = self.output_action.get_payload()
        if output_action_payload:
            payload[self._OUTPUT_ACTION_FIELD] = output_action_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_action(self):

        payload = {self._ACTION_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_action(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_action(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class MATCH(object):

    _MATCH_FIELD = "match"
    _IPV4_SOURCE_FIELD = "ipv4-source"
    _IP_MATCH_FIELD = "ip-match"
    _ETHERNET_MATCH_FIELD = "ethernet-match"
    _TCP_DESTINATION_PORT_FIELD = "tcp-destination-port"
    _TCP_SOURCE_PORT_FIELD = "tcp-source-port"
    _IPV4_DESTINATION_FIELD = "ipv4-destination"
    _IN_PORT_FIELD = "in-port"

    def __init__(self):
        self._template = {}
        self._template[self._IPV4_SOURCE_FIELD] = None
        self._template[self._IP_MATCH_FIELD] = None
        self._template[self._ETHERNET_MATCH_FIELD] = None
        self._template[self._TCP_DESTINATION_PORT_FIELD] = None
        self._template[self._TCP_SOURCE_PORT_FIELD] = None
        self._template[self._IPV4_DESTINATION_FIELD] = None
        self._template[self._IN_PORT_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._ip_match = IP_MATCH()
        self._ethernet_match = ETHERNET_MATCH()

    @property
    def ip_match(self):
        return self._ip_match

    @property
    def ethernet_match(self):
        return self._ethernet_match

    def set_ipv4_source(self, value):
        self._template[self._IPV4_SOURCE_FIELD] = value

    def set_tcp_destination_port(self, value):
        self._template[self._TCP_DESTINATION_PORT_FIELD] = value

    def set_tcp_source_port(self, value):
        self._template[self._TCP_SOURCE_PORT_FIELD] = value

    def set_ipv4_destination(self, value):
        self._template[self._IPV4_DESTINATION_FIELD] = value

    def set_in_port(self, value):
        self._template[self._IN_PORT_FIELD] = value

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._IP_MATCH_FIELD] = self.ip_match.get_template(default=default)
            self._default_template[self._ETHERNET_MATCH_FIELD] = self.ethernet_match.get_template(default=default)
            return self._default_template
        else:
            self._template[self._IP_MATCH_FIELD] = self.ip_match.get_template()
            self._template[self._ETHERNET_MATCH_FIELD] = self.ethernet_match.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        ip_match_payload = self.ip_match.get_payload()
        if ip_match_payload:
            payload[self._IP_MATCH_FIELD] = ip_match_payload
        ethernet_match_payload = self.ethernet_match.get_payload()
        if ethernet_match_payload:
            payload[self._ETHERNET_MATCH_FIELD] = ethernet_match_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_match(self):

        payload = {self._MATCH_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_match(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_match(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


class INSTRUCTIONS(object):

    _INSTRUCTIONS_FIELD = "instructions"
    _INSTRUCTION_FIELD = "instruction"

    def __init__(self):
        self._template = {}
        self._template[self._INSTRUCTION_FIELD] = None
        self._default_template = deepcopy(self._template)
        self._REST_URL = None
        self._instruction = INSTRUCTION()

    @property
    def instruction(self):
        return self._instruction

    def set_rest_url(self, value):
        self._REST_URL = value

    def get_template(self, default=False):
        if default:
            self._default_template[self._INSTRUCTION_FIELD] = self.instruction.get_template(default=default)
            return self._default_template
        else:
            self._template[self._INSTRUCTION_FIELD] = self.instruction.get_template()
            return self._template

    def get_payload(self):
        payload = {key: value for key, value in self._template.iteritems() if value is not None}
        instruction_payload = self.instruction.get_payload()
        if instruction_payload:
            payload[self._INSTRUCTION_FIELD] = instruction_payload
        return payload

    def get_json(self, default=False):
        if default:
            return json.dumps(self.get_template(default=default))
        return json.dumps(self.get_payload())

    def create_instructions(self):

        payload = {self._INSTRUCTIONS_FIELD: self.get_template()}
        rest_session.send_post_request(url=self._REST_URL, data=json.dumps(payload))
        return rest_session.response_code, rest_session.response_as_text

    def delete_instructions(self):
        rest_session.send_delete_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text

    def get_instructions(self):
        rest_session.send_get_request(url=self._REST_URL)
        return rest_session.response_code, rest_session.response_as_text


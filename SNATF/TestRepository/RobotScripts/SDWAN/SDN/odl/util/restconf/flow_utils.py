from pprint import pprint

from SDN import config
from SDN.odl.interface.restconf.api.flows import FLOW


def configure_flows(self, **flow_attrs):

    self.flow_obj = FLOW()

    url = r'http://{0}:{1}{2}{3}'.format(config.CONTROLLER_IP, config.RESTCONFPORT,
                                         config.REST_CON, config.CONFIG_FLOW_API)
    print(url)
    self.flow_obj.set_rest_url(value=url)
    self.flow_obj.set_id(flow_attrs["id"])
    self.flow_obj.set_priority(flow_attrs["priority"])
    self.flow_obj.set_table_id(flow_attrs["table_id"])

    if "ipv4_source" in flow_attrs:
        self.flow_obj.match.set_ipv4_source(flow_attrs["ipv4_source"])

    self.flow_obj.match.ethernet_match.ethernet_type.set_type(flow_attrs["type"])

    self.flow_obj.instructions.instruction.set_order(flow_attrs["order"])
    self.flow_obj.instructions.instruction.apply_actions.action.set_order(flow_attrs["order"])
    self.flow_obj.instructions.instruction.apply_actions.action.output_action.set_output_node_connector(
        flow_attrs["export_node_connector"])
    self.flow_obj.instructions.instruction.apply_actions.action.output_action.set_max_length(flow_attrs["max_length"])
    self.flow_obj.instructions.instruction.apply_actions.action.set_order(flow_attrs["order"])

    pprint(self.flow_obj.get_json())
    print(self.flow_obj.create_flow())
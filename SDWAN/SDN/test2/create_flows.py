import unittest
from pprint import pprint
from SDN.odl.interface.restconf.api.flows import FLOW
from SDN import config

class TESTFLOW(unittest.TestCase):

    def test_config_flows(self):
        exp_set_id = "0"
        exp_set_type = "2048"
        exp_set_flow_node_inventory_ipv4_source = ""
        exp_set_order = "0"
        exp_set_priority = "500"
        exp_set_table_id = "1"
        exp_output_node_connector = "NORMAL"
        exp_max_length = "555"
        self.flow_obj = FLOW()

        url = r'http://{0}:{1}{2}{3}'.format(config.CONTROLLER_IP, config.RESTCONFPORT,
                                               config.REST_CON, config.CONFIG_FLOW_API)
        print(url)
        self.flow_obj.set_rest_url(value=url)
        self.flow_obj.set_id(exp_set_id)
        self.flow_obj.set_priority(exp_set_priority)
        self.flow_obj.set_table_id(exp_set_table_id)


        self.flow_obj.match.set_ipv4_source(exp_set_flow_node_inventory_ipv4_source)

        self.flow_obj.match.ethernet_match.ethernet_type.set_type(exp_set_type)

        self.flow_obj.instructions.instruction.set_order(exp_set_order)
        self.flow_obj.instructions.instruction.apply_actions.action.set_order(exp_set_order)
        self.flow_obj.instructions.instruction.apply_actions.action.output_action.set_output_node_connector(exp_output_node_connector)
        self.flow_obj.instructions.instruction.apply_actions.action.output_action.set_max_length(exp_max_length)
        self.flow_obj.instructions.instruction.apply_actions.action.set_order(exp_set_order)

        pprint(self.flow_obj.get_json())
        print(self.flow_obj.create_flow())

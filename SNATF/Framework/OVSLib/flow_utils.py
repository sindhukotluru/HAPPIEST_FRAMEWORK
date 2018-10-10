from pprint import pprint
import sys
import re
sys.path.append('/home/test/SNATF/Framework')
sys.path.append('/home/test/SNATF/TestRepository/Config')
import config
import ControllerConfig
from OVSLib.flows import FLOW
from LoggerLib.log_generate import fill_getLogger

class FlowManagement(object):

    def __init__(self):
        self.flow_obj = FLOW()
        logger_name = __name__.split('.')[-1]
        self.log_handler = fill_getLogger(logger_name)

    def insert_data_to_flows(self, flow_attrs,url):
        """
        This method to feed the flow attributes to controller
        :param flow_attrs:
        """
        self.flow_obj.set_rest_url(value=url)

        if flow_attrs is not None:
            self.flow_obj.set_id(flow_attrs["id"])
            self.flow_obj.set_table_id(flow_attrs["table"])
            if "priority" in flow_attrs:
                self.flow_obj.set_priority(flow_attrs["priority"])
            if "in_port" in flow_attrs:
                self.flow_obj.match.set_in_port(flow_attrs["in_port"])
            if "dl_src" in flow_attrs:
                self.flow_obj.match.ethernet_match.ethernet_source.set_address(flow_attrs["dl_src"])
            if "dl_dst" in flow_attrs:
                self.flow_obj.match.ethernet_match.ethernet_destination.set_address(flow_attrs(["dl_dst"]))
            if "nw_src" in flow_attrs:
                self.flow_obj.match.set_ipv4_source(flow_attrs["nw_src"])
                self.flow_obj.match.ethernet_match.ethernet_type.set_type(flow_attrs["dl_type"])

            if "nw_proto" in flow_attrs:
                self.flow_obj.match.ip_match.set_ip_protocol(flow_attrs["nw_proto"])
            if "dl_type" in flow_attrs:
                self.flow_obj.match.ethernet_match.ethernet_type.set_type(flow_attrs["dl_type"])
                if flow_attrs["dl_type"] is "2048" or "0x0800":
                    self.flow_obj.match.ip_match.set_ip_proto("ipv4")
            if "tcp_dst" in flow_attrs:
                self.flow_obj.match.set_tcp_destination_port(flow_attrs['tcp_dst'])
            if "icmp_type" in flow_attrs:
                print flow_attrs["icmp_type"]
                self.flow_obj.match.icmp4_match.set_icmpv4_type(flow_attrs["icmp_type"])
            if "icmp_code" in flow_attrs:
                self.flow_obj.match.icmp4_match.set_icmpv4_code(flow_attrs["icmp_code"])
            if "dl_vlan" in flow_attrs:
                self.flow_obj.match.vlan_match.vlan_id.set_vlan_id_present("true")
                self.flow_obj.match.vlan_match.vlan_id.set_vlan_id(flow_attrs["dl_vlan"])
            if str(flow_attrs["actions"]).lower() != 'drop':
                self.flow_obj.instructions.instruction.set_order(flow_attrs["order"])
                if ',' not in str(flow_attrs["actions"]):
                    self.flow_obj.instructions.instruction.apply_actions.action.\
                                                                     set_order_output_action(flow_attrs["order"])
                    self.flow_obj.instructions.instruction.apply_actions.action.output_action.\
                                                                 set_output_node_connector(flow_attrs["actions"])
                    self.flow_obj.instructions.instruction.apply_actions.action.output_action.\
                                                                         set_max_length(flow_attrs["max_length"])

                else:
                    if 'strip_vlan' in str(flow_attrs["actions"]):
                        self.flow_obj.instructions.instruction.apply_actions.action.\
                                                                   set_order_pop_vlan_action(flow_attrs["order"])
                        self.flow_obj.instructions.instruction.apply_actions.action.enable_pop_vlan_action()
                        self.flow_obj.instructions.instruction.apply_actions.action.\
                                                                set_order_output_action(int(flow_attrs["order"])+1)
                        self.flow_obj.instructions.instruction.apply_actions.action.output_action.\
                                                     set_output_node_connector(flow_attrs["actions"].split(',')[1])
                        self.flow_obj.instructions.instruction.apply_actions.action.output_action.\
                                                                        set_max_length(flow_attrs["max_length"])

                    elif 'mod_vlan_vid' in str(flow_attrs["actions"]):
                        self.flow_obj.instructions.instruction.apply_actions.action.\
                                                                      set_order_push_vlan_action(flow_attrs["order"])
                        self.flow_obj.instructions.instruction.apply_actions.action.\
                                                                          push_vlan_action.set_ethernet_type("33024")
                        self.flow_obj.instructions.instruction.apply_actions.action.\
                                                               set_order_set_field_action(int(flow_attrs["order"])+1)
                        self.flow_obj.instructions.instruction.apply_actions.action.set_field_action.vlan_match.\
                                                                                  vlan_id.set_vlan_id_present("true")
                        self.flow_obj.instructions.instruction.apply_actions.action.set_field_action.vlan_match.\
                                               vlan_id.set_vlan_id(flow_attrs["actions"].split(':')[1].split(',')[0])
                        self.flow_obj.instructions.instruction.apply_actions.action.\
                                                                  set_order_output_action(int(flow_attrs["order"])+2)
                        self.flow_obj.instructions.instruction.apply_actions.action.output_action.\
                                                       set_output_node_connector(flow_attrs["actions"].split(',')[1])
                        self.flow_obj.instructions.instruction.apply_actions.action.output_action.\
                                                                             set_max_length(flow_attrs["max_length"])


    def configure_flows(self, option,flow_attrs):
        if option == 'add':return self.add_flows(flow_attrs)
        elif option == 'delete':return self.clear_flows(flow_attrs)
        else:
            self.log_handler.writeInfolog('INVALID OPTION TO CONFIGURE FLOWS !!!')
            return False

    def add_flows(self, flow_attrs):

        url = r'http://{0}:{1}{2}{3}'.format(ControllerConfig.CONTROLLER_INFO["IP"],
                                             ControllerConfig.CONTROLLER_RESTCONF_INFO['RESTCONFPORT'],
                                         ControllerConfig.OF_REST_CON, ControllerConfig.OF_API)
        url += flow_attrs["table"]+"/"+"flow/"+flow_attrs["id"]
        self.insert_data_to_flows(flow_attrs=flow_attrs,url=url)
        #pprint(self.flow_obj.get_json())
        self.log_handler.writeInfolog('\nREST CONF URL TO PUSH FLOW:%s'%url)
        set_response_code, set_response_text = self.flow_obj.create_flow()
        if set_response_code != 200:
            pprint(self.flow_obj.get_json())
        get_response_code, get_response_text = self.flow_obj.get_flow()
        if (set_response_code and get_response_code == 200) and \
                ('error' not in get_response_text) and len(str(get_response_text)) > 0:
            return True
        else:
            return False


    def clear_flows(self,flow_attrs=None):
        """
        This method is to clear the flows those are added by the controller
        :param flow_attrs:
        """
        if flow_attrs is not None:
            url = r'http://{0}:{1}{2}{3}'.format(ControllerConfig.CONTROLLER_INFO["IP"],
                                                 ControllerConfig.CONTROLLER_RESTCONF_INFO['RESTCONFPORT'],
                                         ControllerConfig.OF_REST_CON, ControllerConfig.OF_API)
            url += flow_attrs["table"]+"/"+"flow/"+flow_attrs["id"]

        else:
            flow_api = re.search(r'(/open.*openflow:\d+).*',ControllerConfig.OF_API).group(1)
            url = r'http://{0}:{1}{2}{3}'.format(ControllerConfig.CONTROLLER_INFO["IP"],
                                                 ControllerConfig.CONTROLLER_RESTCONF_INFO['RESTCONFPORT'],
                                                 ControllerConfig.OF_REST_CON,flow_api)

        self.insert_data_to_flows(flow_attrs=None, url=url)
        self.log_handler.writeInfolog('\nREST CONF URL TO DEL FLOW:%s'%url)
        del_response_code,del_response_text = self.flow_obj.delete_flow()
        #print(self.flow_obj.get_flow())
        print " >>>>>>>>>>>> DEL RESPONSE: %s"%del_response_code
        if flow_attrs is None:
            if del_response_code == 200 or del_response_code == 404:
                return True
            else: return False
        else:
            if del_response_code == 200 and ('rror' not in del_response_text):
                return True
            else:
                self.log_handler.writeErrorlog("Response Code: %s\nResponse Text:%5s"%(del_response_code,del_response_text))
                return False

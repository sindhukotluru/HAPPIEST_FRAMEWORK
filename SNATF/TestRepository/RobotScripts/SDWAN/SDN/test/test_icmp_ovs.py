import unittest
import sys
sys.path.append('/home/test/repo_12_04_17/repo_latest/')
from SDN import config
from SDN.mininet import OvsConf
from SDN.mininet.ovs import ovs
from SDN.core.utils.sys_utils import remote_ping
from SDN.core.interface.cli_interface import SSHConnection

class test_OVS_FUNC(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.ovs_obj = ovs(IP=config.SWITCH_IP, username= config.SWITCH_USER, password= config.SWITCH_PASSWORD)


    #@unittest.skip("Test to be Skipped")

    @unittest.skip("Test to be Skipped")
    def test_1_ovs_cntrlr_health_check(self):
        """
         Check the requested bridge
         is configured and available in vsctl
        """
        if config.MININET and self.MN:
            self.mn.execute_command("sudo mn -c")
            if self.mn.execute_command("sudo mn",exp_out="mininet>"):
                print "Bridge created with controller has created by MININET\n"
                return True
            else:
                print "Mininet is not able to prepare topology, chacl it...\n"
                return False
        if self.ovs_obj.create_validate_bridge(config.OVS_BRIDGE,[config.CONTROLLER_IP, 6653]):
            print "bridge %s and controller %s configured properly\n" %(config.OVS_BRIDGE, config.CONTROLLER_IP)
            return True
        else:
            print "Something wrong with OVS bridge & controller config\n"

    @unittest.skip("Test to be Skipped")
    def test_2_ovs_ports_connectivity(self):
        """
        Checks the topology availability
        i.e., links between hosts & OVS and OVS & controller
        :return:
        """
        if config.MININET and self.MN:
            print "Ports association with bridge has done by MININET\n"
            return True
        if self.ovs_obj.addports_validate(config.OVS_BRIDGE, config.OVS_BRIDGE_PORTS):
            print "Ports %s are connected properly to the bridge %s\n" %(config.OVS_BRIDGE_PORTS, config.OVS_BRIDGE)
            return True
        else:
            print "Something wrong with logical connections with the ports %s and bridge %s\n"%(config.OVS_BRIDGE_PORTS, config.OVS_BRIDGE)
            return False

    def test_5_port_based_flows_test(self):
        buckets = ['mod_dl_src=00:00:00:92:11:11,mod_dl_dst=00:00:00:91:22:22,output:2',
                   'mod_dl_src=00:00:00:91:11:11,mod_dl_dst=00:00:00:92:22:22,output:1',
                   'mod_dl_src=00:00:00:93:11:11,mod_dl_dst=00:00:00:93:22:22,output:1']

        flows_input = {'bridge': 'ovs', 'group': '0', 'type': 'all', 'buckets': buckets}
        self.ovs_obj.add_group_flows(flows_input)

    @unittest.skip("Test to be Skipped")
    def test_4_port_based_flows_test(self):
        self.ovs_obj.addflows(interface="ovs", protocol="icmp", protocolType="",priority=500, input_port=1, action="output:2")
        self.ovs_obj.addflows(interface="ovs", protocol="icmp", protocolType="",priority=500, input_port=2, action="output:1")
        self.ovs_obj.addflows(interface="ovs", protocol="ssh", protocolType="", priority=500, input_port=1,action="output:2")
        self.ovs_obj.addflows(interface="ovs", protocol="ssh", protocolType="", priority=500, input_port=2,action="output:1")

        self.ovs_obj.addflows(interface="ovs", protocol="arp", protocolType="", priority=500, input_port=1,action="output:2")
        self.ovs_obj.addflows(interface="ovs", protocol="icmp", protocolType="", priority=500, input_port=2,action="output:1")

    @unittest.skip("Test to be Skipped")
    def test_3_port_based_flows_test(self):
        """
        This method is to test the OVS functionality in presence of traffic
        :return:

        """
        status = remote_ping(config.HOST1_IP, config.HOST1_USER, config.HOST1_PASSWORD, config.h2_port1, echo_count=10)
        if status:
            print "Ping between hosts H1 & H2 through OVS is Successfull\n"
        self.ovs_obj.addflows(interface=ovs,protocol=icmp,priority=500,input_port=1,action="output:2")
        self.ovs_obj.addflows(interface=ovs, protocol=icmp, priority=500, input_port=2, action="output:1")




        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE, inputs=None)
        flow_input = {OvsConf.flow_inputs['Pri']: OvsConf.priority[0], OvsConf.flow_inputs['iPort']: OvsConf.ports[0]}
        action = {OvsConf.flow_actions[0]: [OvsConf.ports[1]]}
        self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE, inputs=flow_input, action=action)
        flow_input = {OvsConf.flow_inputs['Pri']: OvsConf.priority[0], OvsConf.flow_inputs['iPort']: OvsConf.ports[1]}
        action = {OvsConf.flow_actions[0]: [OvsConf.ports[0]]}
        self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE, inputs=flow_input, action=action)

        status = remote_ping(config.HOST1_IP,config.HOST1_USER,config.HOST1_PASSWORD,config.h2_port1,echo_count=10)
        if status:
            print "Ping between hosts H1 & H2 through OVS is Successfull\n"
        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE, inputs=flow_input)
        status = remote_ping(config.HOST1_IP, config.HOST1_USER, config.HOST1_PASSWORD, config.h2_port1, echo_count=10)
        if not status:
            print "Ping between hosts H1 & H2 through OVS failed as flows are deleted\n"
        self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE, inputs=flow_input, action=action)
        action = {OvsConf.flow_actions[2]: None}
        self.ovs_obj.manage_flows(manage_type="alter", br_name=config.OVS_BRIDGE, inputs=flow_input, action=action)


        #flow_input = {OvsConf.flow_inputs['Pri']:OvsConf.priority[0],OvsConf.flow_inputs['iPort']:OvsConf.ports[0],OvsConf.flow_inputs['Protocol']:"arp"}
        #action = {OvsConf.flow_actions[0]:[OvsConf.ports[1]]}
        #self.ovs_obj.manage_flows(manage_type="add",br_name=config.OVS_BRIDGE, inputs = flow_input, action = action)
        #action = {OvsConf.flow_actions[2]: None}
        #self.ovs_obj.manage_flows(manage_type="alter", br_name=config.OVS_BRIDGE, inputs=flow_input,action=action)
        #action = {OvsConf.flow_actions[0]:[OvsConf.ports[1],4]}
        #self.ovs_obj.manage_flows(manage_type="alter", br_name=config.OVS_BRIDGE, inputs=flow_input, action=action)
        #self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE, inputs=flow_input)


if __name__== "__main__":
    unittest.main()

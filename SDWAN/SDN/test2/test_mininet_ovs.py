import unittest
import sys
sys.path.append('/home/test/Sirish_repo/repo_latest/')
from SDN import config
from SDN.mininet import OvsConf
from SDN.mininet.ovs import ovs
import time
from SDN.mininet import MininetInterface

class test_OVS_FUNC(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.mini = False
        self.ovs_obj = ovs(IP=config.SWITCH_IP, username= config.SWITCH_USER, password= config.SWITCH_PASSWORD,root_password=config.SWITCH_ROOT_PSWD)

        if config.MININET:
            self.mn = MininetInterface.MininetConnection(IP=config.SWITCH_IP, username= config.SWITCH_USER, password= config.SWITCH_PASSWORD)
            self.MN = self.mn.connect(controller="remote",contIP=config.CONTROLLER_IP,customScript="/home/test/custom.py", topo="Switch2")
            if self.MN: self.mini = True

    unittest.skip("Test to be Skipped")

    def test_1_ovs_cntrlr_health_check(self):
        """
         Check the requested bridge
         is configured and available in vsctl
        """
        topo=None
        msg = ""
        if self.mini:
            topo = self.mini
            msg = "by Mininet"

        if self.ovs_obj.create_validate_bridge(config.OVS_BRIDGE,[config.CONTROLLER_IP, 6653],topo=topo):
            print "bridge %s and controller %s configured properly %s\n" %(config.OVS_BRIDGE, config.CONTROLLER_IP, msg)
            time.sleep(10)
            return True
        else:
            print "Something wrong with OVS bridge & controller config\n"

    def test_2_ovs_ports_connectivity(self):
        """
        Checks the topology availability
        i.e., links between hosts & OVS and OVS & controller
        :return:
        """
        if self.mini:
            print "Ports association with bridge has done by MININET\n"
            return True
        if self.ovs_obj.addports_validate(config.OVS_BRIDGE, config.OVS_BRIDGE_PORTS):
            print "Ports %s are connected properly to the bridge %s\n" %(config.OVS_BRIDGE_PORTS, config.OVS_BRIDGE)
            return True
        else:
            print "Something wrong with logical connections with the ports %s and bridge %s\n"%(config.OVS_BRIDGE_PORTS, config.OVS_BRIDGE)
            return False

    def test_3_port_based_flows_test(self):
        """
        This method is to test the OVS functionality in presence of traffic
        :return:
        """
        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE, inputs=None)
        flow_input = {OvsConf.flow_inputs['Pri']: OvsConf.priority[0], OvsConf.flow_inputs['iPort']: OvsConf.ports[0]}
        action = {OvsConf.flow_actions[0]: [OvsConf.ports[1]]}
        self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE, inputs=flow_input, action=action)
        flow_input = {OvsConf.flow_inputs['Pri']: OvsConf.priority[0], OvsConf.flow_inputs['iPort']: OvsConf.ports[1]}
        action = {OvsConf.flow_actions[0]: [OvsConf.ports[0]]}
        self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE, inputs=flow_input, action=action)
        if self.mini:
            return self.mn.ping("h3","h4")
        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE, inputs=flow_input)
        if self.mini:
            return self.mn.ping("h3","h4")
        """
        else:
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
        """
        #if self.mini:self.mn.disconnect()
if __name__== "__main__":
    unittest.main()

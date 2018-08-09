import unittest
import sys
sys.path.append('/home/test/AUTOMATION/HAPPIEST_FRAMEWORK')
from Config import config
from Config import OvsConf
from Supporting_Libs.ovs import ovs
from Supporting_Libs.Karaf import Karaf
from Supporting_Libs import debugHelper
from Supporting_Libs.hosts import hosts
import time
from Supporting_Libs import MininetInterface
from Supporting_Libs import sys_utils
from Supporting_Libs.Traffic_Generator import Scapy
import pdb


class test_OVS_ODL_FUNC_Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.mini = False
        self.ovs_obj = ovs(IP=config.SWITCH_IP, username= config.SWITCH_USER,
                           password= config.SWITCH_PASSWORD)
        if config.MININET:
            self.mn = MininetInterface.MininetConnection(IP=config.SWITCH_IP, username= config.SWITCH_USER,
                                                         password= config.SWITCH_PASSWORD)
            self.MN = self.mn.connect_mini()
            if self.MN:
                self.mn.make_mini_topology(controller="remote",contIP=config.CONTROLLER_IP,
                                           customScript="/home/test/custom.py", topo="Switch2")
                self.mini = True

        self.cntrlr_obj = Karaf(IP=config.CONTROLLER_IP, username=config.CONTROLLER_USER,
                               password=config.CONTROLLER_PASSWORD)

        if not config.MININET:
            self.h1 = hosts(IP=config.HOST1_IP, username= config.HOST1_USER, password= config.HOST1_PASSWORD)
            #self.h1.connect_host()
            self.h2 = hosts(IP=config.HOST2_IP, username=config.HOST2_USER, password=config.HOST2_PASSWORD)
            #self.h2.connect_host()

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
            #self.ovs_obj.write2log("bridge %s and controller %s configured properly %s\n"
            self.ovs_obj.log_handler.writeInfolog("bridge %s and controller %s configured properly %s\n"
                                   %(config.OVS_BRIDGE, config.CONTROLLER_IP, msg))
            time.sleep(5)
            return True
        else:
            #self.ovs_obj.write2log("Something wrong with OVS bridge & controller config\n")
            self.ovs_obj.log_handler.writeErrorlog("Something wrong with OVS bridge & controller config\n")
            debugHelper.debug_controller_failure(self.ovs_obj, self.cntrlr_obj)
            assert False

    unittest.skip("Test to be Skipped")
    def test_2_ovs_ports_connectivity(self):
        """
        Checks the topology availability
        i.e., links between hosts & OVS and OVS & controller
        :return:
        """
        topo=None
        msg = ""
        if self.mini:
            topo = self.mini
            msg = "by MININET"
        if self.ovs_obj.addports_validate(config.OVS_BRIDGE, config.OVS_BRIDGE_PORTS,topo=topo):
            #self.ovs_obj.write2log("Ports %s are connected properly to the bridge %s %s\n"
            self.ovs_obj.log_handler.writeInfolog("Ports %s are connected properly to the bridge %s %s\n"
                                   %(config.OVS_BRIDGE_PORTS, config.OVS_BRIDGE,msg))
            return True
        else:
            #self.ovs_obj.write2log("Something wrong with logical connections with the ports %s and bridge %s\n"
            self.ovs_obj.log_handler.writeErrorlog("Something wrong with logical connections with the ports %s "
                                                   "and bridge %s\n"%(config.OVS_BRIDGE_PORTS, config.OVS_BRIDGE))
            assert False

    unittest.skip("Test to be Skipped")
    def test_3_make_host_nics_up(self):
        """
        This method is to make hosts initial configuration ready
        :return:
        """
        if self.mini:
            obj1=obj2=self.mn
        else:
            obj1 = self.h1
            obj2 = self.h2

        if sys_utils.configure_host_nic_ip(obj=obj1,node = config.source,if_name=config.HOST1_PORTS[0],
                                           ip=config.HOST1_IPs[0]):
            if sys_utils.configure_host_nic_ip(obj=obj2,node=config.dest,if_name=config.HOST2_PORTS[0],
                                               ip=config.HOST2_IPs[0]):
                 pass
            else:
                 assert False
        else:
            assert False



if __name__== "__main__":
    unittest.main()

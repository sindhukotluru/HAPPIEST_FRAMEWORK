import unittest
import sys
sys.path.append('/home/test/HAPPIEST_FRAMEWORK')
from Config import config,ControllerConfig
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
        self.ovs_obj = ovs(IP="192.168.203.45", username= config.SWITCH['USER'],
                           password= config.SWITCH['PASSWORD'])

    unittest.skip("Test to be Skipped")
    def test_1_ovs_cntrlr_health_check(self):
#        self.ovs_obj.ovs_execute_command(cmd="ovs-vsctl add-br abcdefghij")
#        print self.ovs_obj.resp
        #c = "ip netns exec qdhcp-e9b7f509-949c-4578-9af9-6e2960a9b0f3 route -n"
        c = "ovs-ofctl dump-flows mec_br1"
        self.ovs_obj.ovs_execute_command(cmd=c)
#        print self.ovs_obj.resp

if __name__== "__main__":
    unittest.main()

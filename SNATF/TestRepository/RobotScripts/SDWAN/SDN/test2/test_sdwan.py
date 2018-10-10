import unittest
from SDN.test.sdwan_flows import SDWAN


class TestSDWAN(unittest.TestCase):

    def setUp(self):
        self.sdwan_instance = SDWAN()

    def test_sdwan_scenarios(self):

        #1. Ping all Device from Test Execution Machine
        devices = ['10.18.20.138', '10.18.20.96']
        assert(self.sdwan_instance.e_PowerUpDevices(devices=devices))

        #2. Verify openflow version and Configured Flows
        open_flow_version = '2.3.1'
        protocol = "OpenFlow13"
        protocolType = "arp"
        interface = "s1"
        print(self.sdwan_instance.v_VerifyConfigFlows(open_flow_version=open_flow_version,
                                                      protocol=protocol, protocolType=protocolType,
                                                      interface=interface))




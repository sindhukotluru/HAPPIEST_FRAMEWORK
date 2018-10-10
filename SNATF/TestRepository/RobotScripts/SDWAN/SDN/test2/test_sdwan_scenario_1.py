import unittest
import sys
sys.path.append('/home/test/vivek_repo')
from SDN.test2.sdwan_flows import SDWAN_FLOWS
from SDN import config
from SDN.sdwan.interface.webpages.configure import SERVICE_TYPE, LINK_TYPE

class TestSDWAN(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.sdwanflows_obj = SDWAN_FLOWS()

    #@unittest.skip("Test to be Skipped")
    def test_1_PowerUpDevices(self):
        status = True
        print("\nTest 1: Verify if all Devices are Powered Up")
        devices = [config.CLIENT_IP, config.SWITCH_IP, config.HOST1_IP, config.HOST2_IP]
        status = self.sdwanflows_obj.e_PowerUpDevices(devices=devices)
        print status
        #assert (self.sdwanflows_obj.e_PowerUpDevices(devices=devices))

    #@unittest.skip("Test to be Skipped")
    def test_2_Configure_and_Verify_DefaultFlows(self):
        print("\nTest 2: Verify if Default Flows can be configured from Web UI")
        #self.sdwanflows_obj.e_ConfigureDefaultFlows()


        print("\nTest: Verify if the Connection between OVS Switch and remote Devices is established")
        dest_devices = [config.CLIENT_IP, config.HOST1_IP, config.HOST2_IP]

        for remote_ip in dest_devices:

            status = self.sdwanflows_obj.e_PingDevices(source_ip=config.SWITCH_IP, source_user=config.SWITCH_USER,
                                                       source_password=config.SWITCH_PASSWORD, destination_ip=remote_ip)
            print status

            if not status:
                print("Remote Device IP: {0} not reachable from Switch IP:{1}".format(config.SWITCH_IP, remote_ip))
            assert status

    #@unittest.skip("Test to be Skipped")
    def test_3_Configure_and_Verify_UIFlows(self):
        print("\nTest: Verify the MPLS and DIA Flows configured through the WebUI")

        interface = "s1"
        open_flow_version = '2.5.0'
        protocol = "OpenFlow13"
        protocolType = 'tcp'

        #self.sdwanflows_obj.e_ConfigureUIFlows(service=SERVICE_TYPE.SSH, link_type=LINK_TYPE.MPLS)

        #assert(self.sdwanflows_obj.v_VerifyConfigFlows(open_flow_version=open_flow_version,
         #                                              protocol=protocol, protocolType=protocolType,
          #                                             interface=interface))

        self.sdwanflows_obj.e_ConfigureUIFlows(service=SERVICE_TYPE.ARP, link_type=LINK_TYPE.MPLS)

        assert (self.sdwanflows_obj.v_VerifyConfigFlows(open_flow_version=open_flow_version,
                                                        protocol=protocol, protocolType=SERVICE_TYPE.ARP, interface=interface))

        print("Test: Verify the Flow Statistics table for configured flows")

        assert(self.sdwanflows_obj.v_VerifyFlowStatistics(service=SERVICE_TYPE.SSH,
                                                          protocolType='tcp',
                                                          interface=interface,
                                                          link_type=LINK_TYPE.MPLS,
                                                          protocol=protocol))

        assert (self.sdwanflows_obj.v_VerifyFlowStatistics(service=SERVICE_TYPE.ARP,
                                                           protocolType=SERVICE_TYPE.ARP,
                                                           interface=interface,
                                                           link_type=LINK_TYPE.MPLS,
                                                           protocol=protocol))

    unittest.skip("Test to be Skipped")
    def test_4_Verify_Traffic_Generator(self):

        traffic = self.sdwanflows_obj.e_TrafficGenerator()
        print("\nTest Verify if Traffic Generated is received by the Host")

        print(traffic)
        if traffic:
            print "Inside Assert True"
            assert True
        else:
            print "Inside Assert False"
            assert False



if __name__== "__main__":
    unittest.main()







from SDN.mininet import ovs
from SDN import config

import unittest
from pprint import pprint
IP = "10.18.20.214"
IP = config.CONTROLLER_IP
usr = config.SWITCH_USER
pwd = config.SWITCH_PASSWORD


class TestOVS(unittest.TestCase):

    def setUp(self):
        print 'Setup->'
        self.S1 = ovs.ovs(IP=IP, username=usr, password=pwd)

    def test_addflows(self):

        """self.S1.addflows(interface='s1',
                         protocol='OpenFlow13',
                         protocolType='arp',
                         actions='FLOOD')
        """
        assert(self.S1.dumpflows(interface='s1',
                          protocol='OpenFlow13',
                          protocolType='arp',))

    @unittest.skip("Test to be Skipped")
    def test_ifconfig(self):

        Resp = self.S1.ifconfig(InterfaceList= False)
        pprint(Resp[1])
        Resp = self.S1.ifconfig(InterfaceList= True)
        pprint(Resp[1])

    @unittest.skip("Test to be Skipped")
    def test_iperf(self):
        Resp = self.S1.iperf_client(client = '10.18.20.214',
                                    client_username= 'mininet',
                                    client_password='mininet',
                                    serverip='10.18.20.92'
                                    )
        print Resp


if __name__== "__main__":
    unittest.main()
    
    
             



 

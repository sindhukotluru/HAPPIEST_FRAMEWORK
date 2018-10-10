##import base
from SDN.mininet import MininetInterface
import unittest
from pprint import pprint
import re

IP= "10.18.20.214"
username = "mininet"
password= "mininet"

class Test_MininetConnections(unittest.TestCase):

    def setUp(self):
        print "->Setup"
        self.S1 = MininetInterface.MininetConnection(IP= IP, username= username,password= password)

    def tearDown(self):
        print "TearDown<-"
        self.S1.disconnect()
        del(self.S1)
    
    def test_ping(self):
        if self.S1.connect() is True :
            Resp = self.S1.ping('h1','h2')
            if Resp.find("0% packet loss")>0 :
                print Resp
    
    def test_pingall(self):
        if self.S1.connect() is True :
            print  self.S1.pingall() 
   
    def test_links(self):
        if self.S1.connect() is True:
            print self.S1.getlinks()

    def test_nodes(self):
        if self.S1.connect() is True:
            print self.S1.getnodes()
    
    def test_dump(self):
        if self.S1.connect() is True:
            print self.S1.dump()
    
    def test_get_host_IP(self, cmd='h1'):
        if self.S1.connect() is True:
            print self.S1.get_host_IP(cmd)
    
    def test_get_switch_IP(self, cmd='s1'):
        if self.S1.connect() is True:
            print self.S1.get_switch_IP(cmd)
    
    def test_get_host_pid(self, cmd='h1'):
        if self.S1.connect() is True:
            print self.S1.get_host_pid(cmd)
    
    def test_get_switch_pid(self, cmd='s1'):
        if self.S1.connect() is True:
            print self.S1.get_switch_pid(cmd)
    
    def test_perform_test(self):
        if self.S1.connect() is True:
            data = self.S1.perform_test()
            if isinstance(eval("".join(re.findall("Results: (.*)", data))), (list)):
                print self.S1.perform_test()
    
    def test_get_ports(self):
        if self.S1.connect() is True:
            data =self.S1.get_ports()
            if data.find("-eth*"):
                print data
    
        
if __name__== "__main__" :
    unittest.main()

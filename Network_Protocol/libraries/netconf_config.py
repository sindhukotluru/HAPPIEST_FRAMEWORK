import sys
import re
import Netconf_Device
from threading import Thread
from time import sleep

class netconf_config(object):

    @staticmethod
    def config_ip_addr(*args):
        """args[0] is Router name ex., R1
           args[1] is Router link ex., Link_R1_R2"""

        dev = Netconf_Device.Netconf_Device()
        sys.stdout.write("Configuring IP address for %s" % args[0])
        status = dev.set_IP(R6, Link_R6)
        if status is False:
            sys.stdout.write("Configuration of IP Address for %s Failed" % args[0])
        else:
            sys.stdout.write("Configured  IP Address for %s" % args[0])

    @staticmethod
    def configure_net_conf(*args):
        """args[0] is Router name ex., R1
           args[1] is Router lconfigure_net_confink ex., Link_R1_R2"""

        dev = Netconf_Device.Netconf_Device()
        sys.stdout.write("Configuring IP address for %s" % args[0])
        status = dev.configure_netconf(R6, Link_R6)
        if status is False:
            sys.stdout.write("Configuration of Netconf for %s Failed" % args[0])
        else:
            sys.stdout.write("Configured  Netconf server for %s" % args[0])
def start_configure(device):
    netconf_config.config_ip_addr(device[0], device[1], device[2])
   
def start_netconf_configure(device):
    netconf_config.configure_net_conf(device[0], device[1], device[2])
    

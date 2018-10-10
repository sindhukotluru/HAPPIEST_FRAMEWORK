from SDN.core.utils import sys_utils
from SDN.mininet.ovs import ovs
from SDN import config

class SDWAN(object):

    def e_PowerUpDevices(self, devices):
        """
        1. Ping all the devices from Test Execution engine.
        :return: Return True if ping succeeds else False
        """
        status = True
        for ip in devices:
            status &= sys_utils.ping(ip=ip, echo_count=3)
        return status


    def e_ConfigFlows(self):
        """
        1. Configure the pre-requisite flows to between Client and Nodes using the Controller's REST API
        :return: Return True is the REST API return status code as 200 else False
        """
        pass

    def v_VerifyConfigFlows(self, open_flow_version, protocol, protocolType, interface):
        """
        1. Verify OpenFlow version
        2. Verify the configured flow executing the open flow dump commands on the rasberryPI device.
        :return: Output of the Dump flow command.
        """
        status = True
        ovs_intf = ovs(IP=config.HOST1_IP, username=config.MININET_USER, password=config.MININET_PASS)
        exp_version = open_flow_version
        actual_version = ovs_intf.version()

        status &= True if exp_version == actual_version else False
        if status:
            status &= ovs_intf.dumpflows(protocol=protocol, protocolType=protocolType, interface=interface)
            return ovs_intf.rc.resp if status else None
        else:
            print("Version Information mismatch. Found {0} instead of {1}".format(actual_version, exp_version))



    def e_PingDevices(self):
        """
        1. Ping between Source and Destination.
        :return: Return True if ping succeeds else False
        """
        source_ip = ""
        source_user = ""
        source_password = ""
        destination_ip = ""
        status = True

        status &= sys_utils.remote_ping(source_ip=source_ip, source_user=source_user,
                                        source_password=source_password, destination_ip=destination_ip)


    def e_TrafficGenerator(self):
        """
        1. Execute the iperf command on the Client(Source) machine with type of traffic to be generated
        :return: None
        """
        pass

    def v_VerifyTraffic(self):
        """
        1. Execute the iperf command on the Destination machine and capture the output of the traffic recieved.
        :return:
        """
        pass
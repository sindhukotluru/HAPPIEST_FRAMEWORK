from pprint import pprint

from SDN.core.utils import sys_utils
from SDN.mininet.ovs import ovs
from SDN import config
from SDN.odl.util.restconf import flow_utils
from SDN.sdwan.interface.webpages.pages import Pages
from SDN.core.interface.web_interface import WebInterface
from SDN.core.utils.common_types import BrowserType
from SDN.sdwan.interface.webpages.configure import SERVICE_TYPE, LINK_TYPE
from SDN.sdwan.utils import iperf

import pdb


class SDWAN_FLOWS(object):

    def __init__(self):
        pass
    #
    def page_open(self):
        self.sdwan_page = Pages(WebInterface(browser=BrowserType.CHROME))
        self.sdwan_page.base_page.browse_url(url=config.BASE_PAGE_URL)

    def e_PowerUpDevices(self, devices):
        """
        1. Ping all the devices from Test Execution engine.
        :return: Return True if ping succeeds else False
        """
        status = True
        for ip in devices:
            status &= sys_utils.ping(ip=ip, echo_count=3)
            #print status
            #print ip
        return status

    def e_ConfigureDefaultFlows(self):
        """
        Press the Reload button on the Web UI Topology Section
        :return:
        """
        # TBD : Call the method which verifies this in OpenFlowDumps command executed on Switch using SSH
        # Return status if on verification of output
        self.sdwan_page.topology_page.navigate_to_topology_section()
        self.sdwan_page.topology_page.reload_topology_view()



    def e_ConfigureUIFlows(self, service, link_type):
        """
        Configure the UI Flows on the Web Administration Configuration section
        """

        self.sdwan_page.configure_page.navigate_to_configure_section()
        self.sdwan_page.configure_page.configure_service(service=service,
                                                         link_type=link_type)
        self.sdwan_page.topology_page.navigate_to_topology_section()
        self.sdwan_page.topology_page.reload_topology_view()




    def e_ConfigFlows(self):
        """
        1. Configure the pre-requisite flows to between Client and Nodes using the Controller's REST API
        :return: Return True is the REST API return status code as 200 else False
        """
        # FLOW 1
        exp_id = "0"
        exp_type = "2048"
        exp_flow_node_inventory_ipv4_source = ""
        exp_order = "0"
        exp_priority = "500"
        exp_table_id = "1"
        exp_output_node_connector = "NORMAL"
        exp_max_length = "555"
        flow_utils.configure_flows(id=exp_id, type=exp_type, ipv4_source=exp_flow_node_inventory_ipv4_source,
                                   order=exp_order, priority=exp_priority, table_id=exp_table_id,
                                   output_node_connector=exp_output_node_connector, max_length=exp_max_length)


    def v_VerifyConfigFlows(self, open_flow_version, protocol, protocolType, interface):
        """
        1. Verify OpenFlow version
        2. Verify the configured flow executing the open flow dump commands on the rasberryPI device.
        :return: Output of the Dump flow command.
        """
        status = True
        ovs_intf = ovs(IP=config.SWITCH_IP, username=config.SWITCH_USER, password=config.SWITCH_PASSWORD)

        exp_version = open_flow_version
        actual_version = ovs_intf.version()

        status &= True if exp_version == actual_version else False


        if status:
            flow_info = None
            print "\nflow_info 1 = ", flow_info
            flow_info = ovs_intf.get_flows(protocol=protocol, protocolType=protocolType, interface=interface)
            print "\nflow_info 2= ", flow_info

            if flow_info:

                for flow in flow_info:

                    try:
                        actual_protocol = flow["priority"].split(",")[1].split(" ")[0]
                    except IndexError:
                        actual_protocol = None
                    if protocolType != actual_protocol:
                        status &= False
                        print("Protocol Mismatch. Expected {0} but found {1}".format(protocolType, actual_protocol))
            else:
                status &= False
                print("No flow found for configured Protocol: {0}".format(protocolType))
        else:
            status &= False
            print("Version Information mismatch. Found {0} instead of {1}".format(actual_version, exp_version))

        return status

    def v_VerifyFlowStatistics(self, service, protocolType, interface, link_type, protocol):

        status = True
        self.sdwan_page.statistics_page.navigate_to_statistics_section()
        self.sdwan_page.statistics_page.navigate_to_flow_table_statistics()
        flow_statistics = self.sdwan_page.statistics_page.get_flow_table_information()

        expected_flows = [{self.sdwan_page.statistics_page.INPUT_HEADER: link_type,
                         self.sdwan_page.statistics_page.OUTPUT_HEADER: LINK_TYPE.EDGE,
                         self.sdwan_page.statistics_page.SERVICE_HEADER: service.upper(),
                         self.sdwan_page.statistics_page.TABLEID_HEADER: '0'},
                         {self.sdwan_page.statistics_page.INPUT_HEADER: LINK_TYPE.EDGE,
                         self.sdwan_page.statistics_page.OUTPUT_HEADER: link_type,
                         self.sdwan_page.statistics_page.SERVICE_HEADER: service.upper(),
                         self.sdwan_page.statistics_page.TABLEID_HEADER: '0'}]

        for flow in expected_flows:
            found_flow = False
            for actual_flows in flow_statistics:
                subset = {key: value for key,value in actual_flows.iteritems() if key in flow.keys()}
                if subset == flow:
                    found_flow = True
            status &= found_flow

        return status

        pass

    def e_PingDevices(self, source_ip, source_user, source_password, destination_ip):
        """
        1. Ping between Source and Destination.
        :return: Return True if ping succeeds else False
        """
        status = True

        status &= sys_utils.remote_ping(source_ip=source_ip, source_user=source_user,
                                        source_password=source_password, destination_ip=destination_ip)
        return status


    def e_TrafficGenerator(self):
        """
        1. Execute the iperf command on the Client(Source) machine with type of traffic to be generated
        :return: None
        """
        self.transmitted_traffic, self.received_traffic = iperf.monitor_server_traffic(
            server_ip=config.HOST1_IP, server_username=config.HOST1_USER, server_password=config.HOST1_PASSWORD,
            client_ip=config.CLIENT_IP, client_username=config.CLIENT_USER,
            client_password=config.CLIENT_PASSWORD, port='5001')

        return True if self.transmitted_traffic and self.received_traffic else False

    def v_VerifyTraffic(self):
        """
        1. Execute the iperf command on the Destination machine and capture the output of the traffic recieved.
        :return:
        """
        return True if self.received_traffic else False

import unittest
import sys
sys.path.append('/home/test/AUTOMATION/HAPPIEST_FRAMEWORK')
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
        self.ovs_obj = ovs(IP=config.SWITCH['IP'], username= config.SWITCH['USER'],
                           password= config.SWITCH['PASSWORD'])
        if config.MININET:
            self.mn = MininetInterface.MininetConnection(IP=config.SWITCH['IP'], username= config.SWITCH['USER'],
                                                         password= config.SWITCH['PASSWORD'])
            self.MN = self.mn.connect_mini()
            if self.MN:
                self.mn.make_mini_topology(controller="remote",contIP=ControllerConfig.CONTROLLER_INFO['IP'],
                                           customScript="/home/test/custom.py", topo="Switch2")
                self.mini = True
        if ControllerConfig.CONTROLLER_TYPE == "ODL":
            self.cntrlr_obj = Karaf(IP=ControllerConfig.CONTROLLER_INFO["IP"], username=ControllerConfig.CONTROLLER_INFO['USER'],
                               password=ControllerConfig.CONTROLLER_INFO['PASSWORD'])

        if not config.MININET:
            self.h1 = hosts(IP=config.HOST1['IP'], username= config.HOST1['USER'], password= config.HOST1['PASSWORD'])
            #self.h1.connect_host()
            self.h2 = hosts(IP=config.HOST2['IP'], username=config.HOST2['USER'], password=config.HOST2['PASSWORD'])
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

        if self.ovs_obj.create_validate_bridge(config.OVS_BRIDGE_CONF['NAME'],[ControllerConfig.CONTROLLER_INFO["IP"], 6653],topo=topo):
            #self.ovs_obj.write2log("bridge %s and controller %s configured properly %s\n"
            self.ovs_obj.log_handler.writeInfolog("bridge %s and controller %s configured properly %s\n"
                                   %(config.OVS_BRIDGE_CONF['NAME'], ControllerConfig.CONTROLLER_INFO["IP"], msg))
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
        if self.ovs_obj.addports_validate(config.OVS_BRIDGE_CONF["NAME"], config.OVS_BRIDGE_CONF["PORTS"],topo=topo):
            #self.ovs_obj.write2log("Ports %s are connected properly to the bridge %s %s\n"
            self.ovs_obj.log_handler.writeInfolog("Ports %s are connected properly to the bridge %s %s\n"
                                   %(config.OVS_BRIDGE_CONF["PORTS"], config.OVS_BRIDGE_CONF["NAME"],msg))
            return True
        else:
            #self.ovs_obj.write2log("Something wrong with logical connections with the ports %s and bridge %s\n"
            self.ovs_obj.log_handler.writeErrorlog("Something wrong with logical connections with the ports %s "
                                                   "and bridge %s\n"%(config.OVS_BRIDGE_CONF["PORTS"], config.OVS_BRIDGE_CONF["NAME"]))
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

        if sys_utils.configure_host_nic_ip(obj=obj1,node = config.source,if_name=config.HOST1["PORT_CONFIG"]["iface1"],
                                           ip=config.HOST1["PORT_CONFIG"]["iface1_ip"]):
            if sys_utils.configure_host_nic_ip(obj=obj2,node=config.dest,if_name=config.HOST2["PORT_CONFIG"]["iface1"],
                                               ip=config.HOST2["PORT_CONFIG"]["iface1_ip"]):
                 pass
            else:
                 assert False
        else:
            assert False

    unittest.skip("Test to be Skipped")
    def test_4_vlan_based_flows_test(self):
        """
        This method is to test VLAN based test cases
        :return:
        """
        #self.ovs_obj.write2log(" >>>>>>>>>>Tests for VLAN involved FLOWS <<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests for VLAN involved FLOWS <<<<<<<<<<<<\n")
        if self.mini:
            obj1 = obj2 = self.mn
            node1 = config.source
            node2 = config.dest
            dst_nic = config.HOST2["PORT_CONFIG"]["iface1"]
        else:
            obj1 = self.h1
            obj2 = self.h2
            node1 = node2 = None
            dst_nic = config.HOST2["PORT_CONFIG"]["iface1"]

        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=None,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        #self.ovs_obj.write2log(" >>>>>>>>>>Test: Traffic Forward on vlan_vid match<<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Test: Traffic Forward on vlan_vid match<<<<<<<<<<<<\n")
        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[0],"id": "1","dl_vlan":OvsConf.vlans[0],
                      "table": "0","order": "0","actions":'%s'%(OvsConf.ports[1])}
        self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        self.tg = Scapy(device_obj=obj1, node=node1)
        packet = self.tg.generate_packet_to_send(pkt_type='vlan')
        output = self.h1.send_pkts_n_capture(scapy_obj=self.tg, node=obj2, src_if=config.HOST1["PORT_CONFIG"]["iface"],
                                             dst_if=config.HOST2["PORT_CONFIG"]["iface1"], pkt=packet, count=config.pkt_count,
                                             inter=config.interval, filter='vlan')
        valid_count = sys_utils.validate_output(search_str='vlan %s'%OvsConf.vlans[0], input=output)
        if valid_count != 0:
            #self.ovs_obj.write2log("VLAN Tagged Packets are captured on Remote Host")
            self.ovs_obj.log_handler.writeInfolog("VLAN Tagged Packets are captured on Remote Host")
        else:
            #self.ovs_obj.write2log("VLAN Tagged Packets are NOT FOUND on Remote Host, UNEXPECTED!!!!!")
            self.ovs_obj.log_handler.writeErrorlog("VLAN Tagged Packets are NOT FOUND on Remote Host, UNEXPECTED!!!!!")
            assert False

        #self.ovs_obj.write2log(" >>>>>>>>>>Tests to verify strip_vlan functionality <<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests to verify strip_vlan functionality <<<<<<<<<<<<\n")
#        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
#                                  controller=ControllerConfig.CONTROLLER_TYPE)
        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[0],
                      "id": "1", "table": "0", "order": "0","dl_vlan":OvsConf.vlans[0],
                      "actions": 'strip_vlan,%s' % (OvsConf.ports[1])}
        self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        output = self.h1.send_pkts_n_capture(scapy_obj=self.tg, node=obj2, src_if=config.HOST1["PORT_CONFIG"]["iface"],
                                             dst_if=config.HOST2["PORT_CONFIG"]["iface1"], pkt=packet, count=config.pkt_count,
                                             inter=config.interval, filter='vlan')
        valid_count = sys_utils.validate_output(search_str='vlan %s'%OvsConf.vlans[0], input=output)
        self.tg.disconnect()
        if valid_count == 0:
            #self.ovs_obj.write2log("VLAN Tagged Packets are not captured on Remote Host")
            self.ovs_obj.log_handler.writeInfolog("VLAN Tagged Packets are not captured on Remote Host")
        else:
            self.ovs_obj.log_handler.writeErrorlog("VLAN Tagged Packets FOUND on Remote Host, UNEXPECTED!!!!!")
            assert False

    unittest.skip("Test to be Skipped")
    def test_5_vlan_based_flows_test(self):
        """
        This method is to test VLAN based test cases
        :return:
        """
        #self.ovs_obj.write2log(" >>>>>>>>>>Tests for VLAN involved FLOWS <<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests for VLAN involved FLOWS <<<<<<<<<<<<\n")
        #controller = None
        if self.mini:
            obj = self.mn
            node1 = config.source
            node2 = config.dest
            dst_nic = config.HOST2["PORT_CONFIG"]["iface1"]
        else:
            obj = self.h1
            node1 = None
            node2 = self.h2
            dst_nic = config.HOST2["PORT_CONFIG"]["iface1"]

        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=None,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        #self.ovs_obj.write2log(" >>>>>>>>>>Tests to verify mod_vlan_vid functionality <<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests to verify mod_vlan_vid functionality <<<<<<<<<<<<\n")
        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[0],
                      "id": "1","table": "0","order": "0","actions":'mod_vlan_vid:%s,%s'%(OvsConf.vlans[0],OvsConf.ports[1])}
        self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        capture_pkts = sys_utils.peer_ping_capture(obj,node2=node2,dst_nic=dst_nic,
                                                   filter='vlan %s'%OvsConf.vlans[0],node1=node1)
        if sys_utils.validate_output(search_str=OvsConf.vlans[0],input=capture_pkts) == 0:
            assert False
        else:
            #self.ovs_obj.write2log("VLAN with ID %s has pushed to untagged ping packet and captured \n"%OvsConf.vlans[0])
            self.ovs_obj.log_handler.writeInfolog("VLAN with ID %s has pushed to untagged ping packet "
                                                  "and captured \n" % OvsConf.vlans[0])

        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,controller=ControllerConfig.CONTROLLER_TYPE)
        capture_pkts = sys_utils.peer_ping_capture(obj, node2=node2, dst_nic=dst_nic,filter='vlan %s' % OvsConf.vlans[0], node1=node1)
        if sys_utils.validate_output(search_str=OvsConf.vlans[0],input=capture_pkts) != 0:
            assert False
        else:
            #self.ovs_obj.write2log(" VLAN with ID %s is not present in the captured packets \n"%OvsConf.vlans[0])
            self.ovs_obj.log_handler.writeInfolog(" VLAN with ID %s is not present "
                                                  "in the captured packets \n" % OvsConf.vlans[0])

        self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)


    unittest.skip("Test to be Skipped")
    def test_6_port_based_flows_test(self):
        """
        This method is to test the OVS functionality in presence of traffic
        :return:
        """
        #self.ovs_obj.write2log(" >>>>>>>>>>Tests for PORT ID involved FLOWS <<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests for PORT ID involved FLOWS <<<<<<<<<<<<\n")
        if self.mini:
            obj = self.mn
            source = config.source
            dest = config.HOST2["PORT_CONFIG"]["iface1_ip"]
        else:
            obj = self.h1
            source = None
            dest = config.HOST2["PORT_CONFIG"]["iface1_ip"]

        status = self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=None,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[0], "id": "1","table": "0",
                      "order": "0","actions":OvsConf.ports[1]}
        status = self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[1], "id": "2", "table": "0",
                      "order": "0","actions": OvsConf.ports[0]}
        status = self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        result = sys_utils.peer_ping(obj,source=source,dest=dest)
        if result is False: assert result
        status = self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        result1 = sys_utils.peer_ping(obj, source=source, dest=dest)
        if result1 is True: assert result

        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[1],
                      "id": "2", "table": "0","order": "0", "actions": OvsConf.ports[0]}
        status = self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        result2 = sys_utils.peer_ping(obj,source=source,dest=dest)
        if result2 is False: assert result

    unittest.skip("Test to be Skipped")
    def test_7_ACL_Rules_based_flows_test(self):
        """
        This method is to test the ACL rules using OVS flows
        :return:
        """
        #self.ovs_obj.write2log(" >>>>>>>>>>Tests for ACL Rules using OVS FLOWS <<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests for ACL Rules using OVS FLOWS <<<<<<<<<<<<\n")
        if self.mini:
            obj1 = obj2 = self.mn
            node1 = config.source
            node2 = config.dest
            dst_nic = config.HOST2["PORT_CONFIG"]["iface1"]
        else:
            obj1 = self.h1
            obj2 = self.h2
            node1 = node2 = None
            dst_nic = config.HOST2["PORT_CONFIG"]["iface1"]

        status = self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=None,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        #self.ovs_obj.write2log(" >>>>>>>>>>Tests to ALLOW ICMP packets to other port <<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests to ALLOW ICMP packets to other port <<<<<<<<<<<<\n")
        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[0], "id": "0", "table": "0",
                     "order": "0", "dl_type": "2048","nw_proto":'1',"icmp_type":'8',"actions": OvsConf.ports[1]}
        status = self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        self.tg = Scapy(device_obj=obj1,node=node1)
        packet = self.tg.generate_packet_to_send(pkt_type='icmpv4')
        output = self.h1.send_pkts_n_capture(scapy_obj=self.tg,node=obj2,src_if=config.HOST1["PORT_CONFIG"]["iface"],
                                             dst_if=config.HOST2["PORT_CONFIG"]["iface1"],pkt=packet,count=config.pkt_count,
                                             inter=config.interval,filter='icmp[0]==8')
        valid_count = sys_utils.validate_output(search_str = 'ICMP echo request',input=output)
        if valid_count != 0:
            #self.ovs_obj.write2log("ICMP echo request messages are forwarded to host2 port"
            self.ovs_obj.log_handler.writeInfolog("ICMP echo request messages are forwarded to host2 port"
                                   " & captured as expected\n")
        else:
            #self.ovs_obj.write2log("ICMP echo request messages are dropped as UNEXPECTED !!!!!\n")
            self.ovs_obj.log_handler.writeErrorlog("ICMP echo request messages are dropped as UNEXPECTED !!!!!\n")
            assert False
        status = self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests to BLOCK ICMP packets <<<<<<<<<<<<\n")
        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[0], "id": "0", "table": "0",
                      "order": "0", "dl_type": "2048", "nw_proto": '1', "icmp_type": '8', "actions": 'drop'}
        status = self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        packet = self.tg.generate_packet_to_send(pkt_type='icmpv4')
        output = self.h1.send_pkts_n_capture(scapy_obj=self.tg, node=obj2, src_if=config.HOST1["PORT_CONFIG"]["iface"],
                                dst_if=config.HOST2["PORT_CONFIG"]["iface1"], pkt=packet, count=config.pkt_count,
                                             inter=config.interval,filter='icmp[0]==8')
        self.tg.disconnect()
        valid_count = sys_utils.validate_output(search_str = 'ICMP echo request',input=output)
        if valid_count == 0:
            #self.ovs_obj.write2log("All the ICMP echo request messages are dropped as expected\n")
            self.ovs_obj.log_handler.writeInfolog("All the ICMP echo request messages are dropped as expected\n")
        else:
            self.ovs_obj.log_handler.writeErrorlog("All the ICMP echo request messages are not dropped, UNEXPECTED !!!!!\n")
            assert False

        if not self.mini:
            status = self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                      controller=ControllerConfig.CONTROLLER_TYPE)
            if status is False: assert False
            #self.ovs_obj.write2log(" >>>>>>>>>>Tests to ALLOW SSH to the connected HOST's test ip <<<<<<<<<<<<\n")
            self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests to ALLOW SSH to the connected HOST's test ip <<<<<<<<<<<<\n")
            flow_input = {"priority": OvsConf.priority[0],"id": "0", "table": "0","order": "0","actions": 'NORMAL'}
            status = self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                      controller=ControllerConfig.CONTROLLER_TYPE)
            if status is False: assert False
            if self.h1.execute_command_host(cmd='ssh -o ConnectTimeout=10 %s@%s'
                 %(config.HOST1["USER"],config.HOST2["PORT_CONFIG"]["iface1_ip"].split('/')[0]),exp_out='yes/no'):
                if self.h1.execute_command_host(cmd='no',exp_out='#'):
                    #self.ovs_obj.write2log("Able to perform SSH to the connected HOST test ip\n")
                    self.ovs_obj.log_handler.writeInfolog("Able to perform SSH to the connected HOST test ip\n")
            else:
                self.ovs_obj.log_handler.writeErrorlog("Unable to perform SSH to the connected "
                                                       "          HOST test ip, UNEXPECTED !!!!!!!!\n")
                assert False

            #self.ovs_obj.write2log(" >>>>>>>>>>Tests to BLOCK SSH to the connected HOST's test ip <<<<<<<<<<<<\n")
            self.ovs_obj.log_handler.writeInfolog(" >>>>>>>>>>Tests to BLOCK SSH to the connected "
                                                                          "HOST's test ip <<<<<<<<<<<<\n")
            flow_input = {"priority": OvsConf.priority[1], "id": "1", "table": "0", "order": "0", "dl_type": "2048",
                          "nw_proto": '6', "tcp_dst":'22',"actions": 'drop'}
            status = self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                      controller=ControllerConfig.CONTROLLER_TYPE)
            if status is False: assert False
            if self.h1.execute_command_host(cmd='ssh -o ConnectTimeout=10 %s@%s'
                    % (config.HOST1["USER"], config.HOST2["PORT_CONFIG"]["iface1_ip"].split('/')[0]), exp_out='Connection timed out'):
                #self.ovs_obj.write2log("SSH to the connected HOST's test ip failed due to "
                self.ovs_obj.log_handler.writeInfolog("SSH to the connected HOST's test ip failed due to "
                                       "tcp flow which drops tcp packet with dest port=22 \n")
            else:
                assert False


    unittest.skip("Test to be Skipped")
    def test_8_IPv4_based_flows_test(self):
        """
        This method is to test the IPv4 based tests OVS flows
        :return:
        """
        #self.ovs_obj.write2log(">>>>>>>>>>Tests for IPv4 macth based OVS FLOWS <<<<<<<<<<<<\n")
        self.ovs_obj.log_handler.writeInfolog(">>>>>>>>>>Tests for IPv4 macth based OVS FLOWS <<<<<<<<<<<<\n")

        if self.mini:
            obj1 = obj2 = self.mn
            node1 = config.source
            node2 = config.dest
            dst_nic = config.HOST2["PORT_CONFIG"]["iface1"]
        else:
            obj1 = self.h1
            obj2 = self.h2
            node1 = node2 = None
            dst_nic = config.HOST2["PORT_CONFIG"]["iface1"]

        status = self.ovs_obj.manage_flows(manage_type="delete", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=None,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        flow_input = {"priority": OvsConf.priority[0], "in_port": OvsConf.ports[0], "id": "0", "table": "0",
                      "order": "0", "dl_type": "2048", "nw_src":OvsConf.ip_addr[0],"actions":OvsConf.ports[1]}
        status = self.ovs_obj.manage_flows(manage_type="add", br_name=config.OVS_BRIDGE_CONF["NAME"], flow_inputs=flow_input,
                                  controller=ControllerConfig.CONTROLLER_TYPE)
        if status is False: assert False
        config.IP['src_ip'] = '33.33.33.1'
        #self.ovs_obj.write2log(">>>>>>>>>> Sending IP packets(%s) within the configured network range "
        self.ovs_obj.log_handler.writeInfolog(">>>>>>>>>> Sending IP packets(%s) within the configured network range "
                                                                                    "<<<<<<<<<<<"%config.IP['src_ip'])
        self.tg = Scapy(device_obj=obj1, node=node1)
        packet = self.tg.generate_packet_to_send(pkt_type='ip')
        output = self.h1.send_pkts_n_capture(scapy_obj=self.tg, node=obj2, src_if=config.HOST1["PORT_CONFIG"]["iface"],
                                             dst_if=config.HOST2["PORT_CONFIG"]["iface1"], pkt=packet, count=config.pkt_count,
                                             inter=config.interval, filter='ip')
        valid_count = sys_utils.validate_output(search_str=config.IP['src_ip'], input=output)
        if valid_count != 0:
            #self.ovs_obj.write2log("IP packets with %s are received on other HOST, EXPECTED\n"%config.IP['src_ip'])
            self.ovs_obj.log_handler.writeInfolog("IP packets with %s are received on other HOST, "
                                                  "                 EXPECTED\n" % config.IP['src_ip'])
        else:
            #self.ovs_obj.write2log("IP packets with %s are not received on other HOST, UNEXPECTED\n"%config.IP['src_ip'])
            self.ovs_obj.log_handler.writeErrorlog("IP packets with %s are not received "
                                                           "on other HOST, UNEXPECTED\n" % config.IP['src_ip'])
            assert False
        #self.ovs_obj.write2log(">>>>>>>>>> Sending IP packets(%s) from out of configured network range "
        self.ovs_obj.log_handler.writeInfolog(">>>>>>>>>> Sending IP packets(%s) from out of configured network range "
                                                                                     "<<<<<<<<<<<"%config.IP['src_ip'])
        config.IP['src_ip'] = '44.33.33.1'
        packet = self.tg.generate_packet_to_send(pkt_type='ip')
        output = self.h1.send_pkts_n_capture(scapy_obj=self.tg, node=obj2, src_if=config.HOST1["PORT_CONFIG"]["iface"],
                                             dst_if=config.HOST2["PORT_CONFIG"]["iface1"], pkt=packet, count=config.pkt_count,
                                             inter=config.interval, filter='ip')
        self.tg.disconnect()
        valid_count = sys_utils.validate_output(search_str=config.IP['src_ip'], input=output)
        if valid_count == 0:
            #self.ovs_obj.write2log("IP packets with %s are not received on other HOST, EXPECTED\n" % config.IP['src_ip'])
            self.ovs_obj.log_handler.writeInfolog("IP packets with %s are not received "
                                                      "on other HOST, EXPECTED\n" % config.IP['src_ip'])
        else:
            #self.ovs_obj.write2log("IP packets with %s are received on other HOST, UNEXPECTED\n" % config.IP['src_ip'])
            self.ovs_obj.log_handler.writeErrorlog("IP packets with %s are received "
                                                    "on other HOST, UNEXPECTED\n" % config.IP['src_ip'])
            assert False


if __name__== "__main__":
    unittest.main()

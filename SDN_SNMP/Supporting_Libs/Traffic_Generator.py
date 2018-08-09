import re
from Config import config
from Supporting_Libs.log_generate import fill_getLogger
import time


class Scapy(object):
    """
    Class is to handle the SCAPY
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self,device_obj,node=None):
        self.Prompt = ">>>"
        self.TG = device_obj
#        flag = 0
#        if config.MININET:
#           if self.TG.mini_execute_command(cmd='%s scapy'%node,prompt=self.Prompt):
#                flag += 1
#        else:
#            if self.TG.execute_command_host(cmd='scapy',prompt=self.Prompt):
#                flag += 1
        logger_name = __name__.split('.')[-1]
        self.log_handler = fill_getLogger(logger_name)
##        self.TG.wri2log('Entereded into SCAPY Traffic Gen mode') if flag >= 1 \
##            else self.TG.wri2log('Failed to start SCAPY, check properly')
#        self.log_handler.writeInfolog('Entereded into SCAPY Traffic Gen mode') if flag >= 1 \
#                      else self.log_handler.writeErrorlog('Failed to start SCAPY, check properly')

    def connect(self):
        flag = 0
        if config.MININET:
            if self.TG.mini_execute_command(cmd='%s scapy'%node,prompt=self.Prompt):
                flag += 1
        else:
            if self.TG.execute_command_host(cmd='scapy',prompt=self.Prompt):
                flag += 1
        self.log_handler.writeInfolog('Entereded into SCAPY Traffic Gen mode') if flag >= 1 \
                      else self.log_handler.writeErrorlog('Failed to start SCAPY, check properly')
        
    def disconnect(self):
        flag = 0
        if config.MININET:
            if self.TG.mini_execute_command(cmd='exit()',prompt='mininet> '):
                flag += 1
        else:
            if self.TG.execute_command_host(cmd='exit()',prompt='#'):
                flag += 1
        #self.TG.wri2log('EXITED from SCAPY Traffic Gen mode') if flag >= 1 \
            #else self.TG.wri2log('Failed to EXIT from SCAPY, check properly')
        self.log_handler.writeInfolog('EXITED from SCAPY Traffic Gen mode') if flag >= 1 \
            else self.log_handler.writeErrorlog('Failed to EXIT from SCAPY, check properly')


    def generate_packet_to_send(self,pkt_type):
        """
        Makes the command pattern to trigger the traffic
        :return:
        """
        cmd_pattern = ''
        if str(pkt_type) == 'icmpv4':
            cmd_pattern += self.Ether(config.Ethernet)+'/Dot1Q(vlan=%s)/'%config.Vlan["vlan_id"]+self.IP(config.IP)+'/'+self.ICMPV4(config.ICMPv4)
        if str(pkt_type) == 'arp':
            cmd_pattern += self.Ether(config.Ethernet) + '/' + self.Arp(config.Arp)
        if str(pkt_type) == 'ip':
            cmd_pattern += self.Ether(config.Ethernet) + '/' + self.IP(config.IP)
        if str(pkt_type) == 'vlan':
            cmd_pattern += self.Ether(config.Ethernet) + '/' + self.VLAN(config.Vlan)+self.Arp(config.Arp)
        if str(pkt_type) == 'ether':
            cmd_pattern += self.Ether(config.Ethernet)

        return cmd_pattern


    def send_cmd_to_scapy(self,pkt,ifname,count,inter):
        result = False
        cmd = "sendp(%s,iface='%s',count=%s,inter=%s)"%(pkt,ifname,count,inter)
        time.sleep(5)
        return_val =  self.TG.mini_execute_command(cmd=cmd, prompt=self.Prompt) if config.MININET \
            else self.TG.execute_command_host(cmd=cmd, prompt=self.Prompt)
        if return_val:
            if re.search('Sent %s packets.'%count,self.TG.resp):
                self.log_handler.writeInfolog("Successfully sent %s packets from SCAPY"%count)
                result = True
            else:
                self.log_handler.writeErrorlog("Failed to sent packets from SCAPY")
        return result


    def Ether(self,profile):
        """
        To frame Ether header with the provided values
        :return:
        """
        ether_src = profile['src'] if 'src' in profile else '00:01:02:03:04:05'
        ether_dst = profile['dst'] if 'dst' in profile else '00:02:03:04:05:06'
        ether_pkt = "Ether(dst=%s, src=%s)"%(ether_dst,ether_src)
        return ether_pkt


    def IP(self,profile):
        """
        To frame IP header with the provided values
        :return:
        """
        Ip_src = profile['src_ip'] if 'src_ip' in profile else ''
        Ip_dst = profile['dst_ip'] if 'dst_ip' in profile else ''
        IP_pkt = "IP(src='%s', dst='%s')"%(Ip_src,Ip_dst)
        return IP_pkt


    def Arp(self,profile):
        """
        This method is to construct ARP packets
        :return:
        """
        Src_Ip = profile['src_ip'] if 'src_ip' in profile else ''
        Dst_Ip = profile['dst_ip'] if 'dst_ip' in profile else ''
        Op_Code = profile['op_code'] if 'op_code' in profile else '1'
        Arp_pkt = "ARP(op=%s, psrc='%s', pdst='%s')"%(Op_Code,Src_Ip,Dst_Ip)
        return Arp_pkt


    def ICMPV4(self,profile):
        """
        This method is to construct the ICMPV4 packet
        :return:
        """
        ICMPv4_type = profile['type'] if 'type' in profile else '8'
        ICMPv4_code = profile['code'] if 'code' in profile else '0'
        ICMPv4_pkt = 'ICMP(type=%s,code=%s)'%(ICMPv4_type,ICMPv4_code)
        return ICMPv4_pkt


    def VLAN(self,profile):
        """
         This method is to construct the VLAN 802.1Q header
        :return:
        """
        VLAN_Pkt = None
        VID = profile['vlan_id'] if 'vlan_id' in profile else None
        if VID is not None:
            #VLAN_Pkt = 'Dot1Q(vlan=1)/Dot1Q(vlan=%s)/'%VID
            VLAN_Pkt = 'Dot1Q(vlan=%s)/' % VID
        return VLAN_Pkt

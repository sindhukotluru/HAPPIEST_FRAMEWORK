import re
import time
from cli_interface import SSHConnection
from log_generate import fill_getLogger
#from SDN import config


class hosts(SSHConnection):
    """
    This is to make the hosts instances by using the host login details from the config file.
    Date: 10/07/2017
    Author: Sirish
    """

    _cap_file = '/tmp/cap.txt'
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self,*args,**kwargs):
        super(hosts,self).__init__(*args,**kwargs)
        self.IP = kwargs['IP']
        self.usr = kwargs['username']
        self.pwd = kwargs['password']
        self.connect()
        logger_name = __name__.split('.')[-1]
        self.log_handler = fill_getLogger(logger_name)
        self.log_handler.writeInfolog("************* SSH to HOST %s *************" % self.IP)

    def connect_host(self):
        """
        To Connect to the host
        """
        self.connect()
        self.log_handler.writeInfolog("************* SSH to HOST %s *************" %self.IP)

    def execute_command_host(self,cmd,exp_out=None,prompt='#'):
        """
        This method helps to apply commands on host
        """
        self.cmd_from = 'HOST'
        return self.execute_command(cmd= cmd,exp_out=exp_out,prompt=prompt)

    def config_host_nic_ip(self,if_name,ip):
        result = False
        if self.execute_command_host(cmd='ifconfig %s up'%if_name,prompt='#'):
            if self.resp.find('Device not found') == 0:
                self.log_handler.writeErrorlog(msg="Unable to find the Interface %s to configure IP Address"%if_name)
            else:
                self.execute_command_host(cmd='ifconfig %s 0 up'%if_name,prompt="#")
                if self.execute_command_host(cmd='ifconfig %s %s up' %(if_name,ip),prompt="#"):
                    self.execute_command_host(cmd='ifconfig %s' %if_name,prompt='#')
                    if self.resp.find('%s'%ip.split('/')[0]) == -1:
                        self.log_handler.writeErrorlog(msg="Unable to Assign IP Address to the Interface %s"%if_name)
                    else:
                        self.log_handler.writeInfolog(msg="Successfully Assigned IP Address on the Interface %s" % if_name)
                        result = True
        return result

    def ping(self, peer_ip, count="5"):
        ping_cmd = "ping %s -c %s"%(peer_ip.split('/')[0],count)
        if self.execute_command_host(cmd=ping_cmd,prompt='#'):
            regex = r', 0% packet loss'
            if re.search(regex, self.resp):
                return True
            else:
                return False
        else:
            self.log_handler.writeErrorlog("*************Timed-out!!! *************")
            return False

#    def start_capture_on_host(self,iface,filter,count=5):
#        """
#        To start capture the packets using desired command with pattern
#        :return: captured file
#        """
#        if 'vlan' in filter: filter = 'arp'
#        self.execute_command_host(cmd='rm -rf %s'%self._cap_file,exp_out='#')
#        self.CMD = 'tcpdump -e -i %s -c %s %s > %s &'%(iface,count,filter,self._cap_file)
#        #self.CMD = 'tcpdump -e -i %s -c %s > %s &' % (iface, count,self._cap_file)
#        if self.execute_command_host(cmd=self.CMD,exp_out='#'):
#            reg_out = re.search('\[\d+\]\s+(\d+)\s+',self.resp)
#            if reg_out is not None:
#                time.sleep(5)
#                return reg_out.group(1),self._cap_file
#        else: return 0

    def start_capture_on_host(self,timeout,iface,count=10):
        """
        To start capture the packets using desired command with pattern
        :return: captured file
        """
        self.execute_command_host(cmd='rm -rf %s' % self._cap_file, exp_out='#')
        self.CMD = 'timeout %s tcpdump -i %s -e > %s &' % (timeout, iface, self._cap_file)
        if self.execute_command_host(cmd=self.CMD, exp_out='#'):
            reg_out = re.search('\[\d+\]\s+(\d+)\s+', self.resp)
            if reg_out is not None:
                #time.sleep()
                return reg_out.group(1),self._cap_file
            else: return 0

    def stop_capture_on_host(self,pid):
        """
        Stop the capturing process
        :return:
        """
        return True if self.execute_command_host(cmd='kill -9 %s'%pid) else False

    def get_data_from_file(self,input_file = None):
        if input_file is None: input_file = self._cap_file
        captured_data = None
        self.execute_command_host(cmd='ls -lrt %s' % input_file, exp_out='#')
        if self.execute_command_host(cmd='cat %s'%input_file,exp_out='#'):
            captured_data = self.resp
            print captured_data
        return captured_data


    def ping_n_capture(self,node,dst_nic,filter,count='5'):
        """
        This method is to run ping as background process and capture on other end
        :return:
        """
        dst_ip = self.get_host_nic_ip(peer_node=node,peer_nic=dst_nic)
        PID,cap_file = node.start_capture_on_host(iface=dst_nic,filter=filter)
        self.ping(peer_ip=dst_ip,count=count)
        node.stop_capture_on_host(pid=PID)
        return node.get_data_from_file(input_file=cap_file)

    def send_pkts_n_capture(self,scapy_obj,node,src_if,dst_if,pkt,count,inter):
        """
        This method is to send traffic using scapy and capture
        :return:
        """
        timeout = (inter*count)+4
        PID,cap_file = node.start_capture_on_host(timeout=int(timeout), iface=dst_if)
        scapy_obj.send_cmd_to_scapy(pkt=pkt, ifname=src_if,
                                    count=count,inter=inter)
        time.sleep(3)
        node.stop_capture_on_host(pid=PID)
        return node.get_data_from_file(input_file=cap_file)

    def get_host_nic_ip(self,peer_node,peer_nic):
        """
        To get the nic ip of host
        """
        if peer_node.execute_command_host(cmd='ifconfig %s' %peer_nic, exp_out='#'):
            result = peer_node.resp
            reg_out = re.search('\s*.*inet addr:(.*)\s+Bcast.*', result)
            if reg_out:
                return reg_out.group(1)


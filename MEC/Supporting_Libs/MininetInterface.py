import re
import time
import sys, os
from pexpect import pxssh
from Supporting_Libs.patterns import RegexPatterns
from Config import config
#from Interface import SSHConnection
from Supporting_Libs.cli_interface import SSHConnection

DEBUG = False

def dlog(string):
    if DEBUG:
        print string


class MininetConnection(SSHConnection):
    _cap_file = '/tmp/mininet_cap.txt'
    def __init__(self,*args,**kwargs):
        super(MininetConnection,self).__init__(*args,**kwargs)
        self.IP = kwargs['IP']
        self.usr = kwargs['username']
        self.pwd = kwargs['password']
        self.root_pwd = config.SWITCH_ROOT_PSWD
        self.connected = False
        self.disconnected = False
        #self.rc = pxssh.pxssh()
        
    ##To make sure there is only a single instance of this class
    def __new__(self, *args, **kwargs):
        if not hasattr(self,"_inst"):
            self._inst = super(MininetConnection,self).__new__(self,*args,**kwargs)
            dlog("Creating a new instance for the class")
        else:
            dlog("Returning the already created instance...")
        self._inst.wri2log('*************** CONNECTING TO MININET MACHINE ***************')

        return self._inst

    def connect_mini(self,status = True):
        self.parameters = " "
        if status and not self.connected:
            #self.rc.login(self.IP,self.usr,self.pwd)
            return self._inst.connect()

    def mini_execute_command(self,cmd,prompt,exp_out=None):
        self._inst.cmd_from = 'MININET'
        return self._inst.execute_command(cmd=cmd,exp_out=exp_out,prompt=prompt)

    def make_mini_topology(self,topology=None,**kwargs):
        self.wri2log('*************** MAKING TOPOLOGY USING MININET ***************')
        if topology is None:
            self._inst.mini_execute_command(cmd="sudo mn -c",prompt="#") ##Clearing off the previous session !
            if kwargs.has_key('controller') is True :
                self.controller = kwargs.get('controller')
                self.customIP = kwargs.get('contIP')
                self.parameters += " --controller=%s,ip=%s "%(self.controller,self.customIP)
            if kwargs.has_key('customScript') is True :
                self.custom = kwargs.get('customScript')
                self.parameters += " --custom %s "%(self.custom)
            if kwargs.has_key('switch') is True :
                self.switch = kwargs.get('switch')
                self.parameters += " --switch %s,"%(self.switch)
            if kwargs.has_key('protocol') is True :
                self.protocol = kwargs.get('protocol')
                self.parameters += "protocol=%s "%(self.protocol)
            if kwargs.has_key('topo') is True :
                self.topo = kwargs.get('topo')
                #self.nodes = kwargs.get('nodes')
                self.parameters += " --topo %s"%(self.topo)
                
            dlog(self.parameters)
            result = self._inst.mini_execute_command(cmd="sudo mn %s"%(self.parameters),prompt='mininet> ')
            ##Force my session to use the mininet>> terminal
            if result is True :
                self._inst.connected = True
                #dlog(self.rc.before)
                return True
            ##else:
             #   self.rc.PROMPT = "mininet> "
             #   time.sleep(0.01)
             #   if self.rc.prompt() is True :
             #       self.connected = True
             #       #dlog(self.rc.before)
             #       return True
            else:
                #dlog(self.rc.before)
                return False


    def disconnect(self,status= True):
        if status and not self.disconnected:
            self._inst.PROMPT = '\\[PEXPECT\\][\\$\\#] '
            self._inst.mini_execute_command(cmd='exit',prompt=self._inst.PROMPT)
            time.sleep(5)
            self._inst.disconnected = True
            del(self._inst)

    def customCommand(self,cmd):
        if self._inst.mini_execute_command(cmd):
            return self._inst.resp

    def config_host_nic_ip(self,node,if_name,ip):
        result = False
        self._inst.mini_execute_command(cmd='%s ifconfig -a' % (node), prompt='mininet> ')
        out = self._inst.mini_execute_command(cmd='%s ifconfig %s up'%(node,if_name),prompt='mininet> ')
        if out:
            if self._inst.resp.find('command not found') == 0:
                self._inst.wri2log(msg="Unable to find the Interface %s to configure IP Address"%if_name)
            else:
                self._inst.mini_execute_command(cmd='%s ifconfig %s 0 up'%(node,if_name),prompt="mininet> ")
                if self._inst.mini_execute_command(cmd='%s ifconfig %s %s up' %(node,if_name,ip),prompt="mininet> "):
                    self._inst.mini_execute_command(cmd='%s ifconfig %s' %(node,if_name),prompt="mininet> ")

                    if self._inst.resp.find('%s'%ip.split('/')[0]) == -1:
                        self._inst.wri2log(msg="Unable to Assign IP Address to the Interface %s"%if_name)
                    else:
                        self._inst.wri2log(msg="Successfully Assigned IP Address on the Interface %s" % if_name)
                        result = True
        return result

    def ping(self,node1,node2,backgrnd=False):
        """
        :param nodes: arguments Two node names
        :return: response equivalent to "h1 ping h2 -c" in a mininet session
        """
        h1 = node1
        h2 = node2             #node2 can be an dest IP if it consists of multiple nics
        #self.rc.sendline("links")
        PING = "%s ping %s -c 5"%(h1,h2.split('/')[0])
        if backgrnd is True:PING += " &"
        result = self._inst.mini_execute_command(cmd=PING,prompt='mininet> ')
        time.sleep(0.01)
        if result:
            regex = r', 0% packet loss'
            if re.search(regex,self._inst.resp):
                return True
            else: return False
        else:
            self._inst.wri2log("*************Timed-out!!! *************")
            return False


    def Dup_ping_n_capture(self,node1,node2,dst_nic,count=7):
        """
        This method is to run ping as background process and capture on other end
        :return:
        """
        self._inst.mini_execute_command(cmd='%s rm -rf /tmp/temp_pcap.txt'%node2, prompt='mininet> ')
        dst_ip = self._inst.get_host_nic_ip(node=node2,nic=dst_nic)
        CMD = "%s tshark -V -i %s -c %s > /tmp/temp_pcap.txt &" %(node2,dst_nic,count)
        self._inst.mini_execute_command(cmd=CMD, prompt='mininet> ')
        self.ping(node1=node1,node2=dst_ip)
        time.sleep(7)
        if self._inst.mini_execute_command(cmd='%s cat /tmp/temp_pcap.txt'%node2, prompt='mininet> '):
            return_result = self._inst.resp
            self._inst.mini_execute_command(cmd='%s rm -rf /tmp/temp_pcap.txt'%node2, prompt='mininet> ')
            return return_result

    def start_capture_on_mini(self,iface,filter,node,count=5):
        """
        To start capture the packets using desired command with pattern
        """
        #if 'vlan' in filter: filter = 'arp'
        self._inst.mini_execute_command(cmd='%s rm -rf %s'%(node,self._inst._cap_file),prompt='mininet> ')
        self.CMD = '%s tcpdump -e -i %s -c %s %s > %s &'%(node,iface,count,filter,self._inst._cap_file)
        if self._inst.mini_execute_command(cmd=self.CMD,prompt='mininet> '):
            reg_out = re.search('\[\d+\]\s+(\d+)\s+',self.resp)
            if reg_out is not None:
                return reg_out.group(1),self._inst._cap_file
            else: return 0, self._inst._cap_file
        else: return 0,self._inst._cap_file

    def stop_capture_on_mini(self,node,pid):
        """
        Stop the capturing process
        :return:
        """
        self.CMD = '%s killall tcpdump'%node if pid == 0 else '%s kill -9 %s'%(node,pid)
        return True if self._inst.mini_execute_command(cmd=self.CMD,prompt='mininet> ') else False

    def get_data_from_file(self,node,input_file = None):
        if input_file is None: input_file = self._cap_file
        captured_data = None
        if self._inst.mini_execute_command(cmd='%s cat %s'%(node,input_file),prompt='mininet> '):
            captured_data = self._inst.resp
        return captured_data


    def ping_n_capture(self,node1,node2,dst_nic,filter,count='5'):
        """
        This method is to run ping as background process and capture on other end
        :return:
        """
        captured_data = None
        pcap_file = self._inst._cap_file
        #node.execute_command_host(cmd='rm -rf %s'%pcap_file, exp_out='#')
        dst_ip = self._inst.get_host_nic_ip(node=node2,nic=dst_nic)
        #CMD = "tshark -i %s -c %s -w %s &" %(dst_nic,count,pcap_file)
        CMD = "%s tcpdump -e -i %s -c %s %s > %s &"%(node2,dst_nic,count,filter,pcap_file)
        PID,cap_file = self._inst.start_capture_on_mini(iface=dst_nic,filter=filter,node=node2)
        self.ping(node1=node1,node2=dst_ip)
        self._inst.stop_capture_on_mini(node=node2,pid=PID)
        if self._inst._inst.mini_execute_command(cmd='%s cat %s'%(node2,cap_file),prompt='mininet> '):
            captured_data = self._inst.resp
        return captured_data


    def get_host_nic_ip(self,node,nic):
        """
        To get the nic ip of host
        """
        if self._inst.mini_execute_command(cmd='%s ifconfig %s'%(node,nic),prompt='mininet> '):
            result = self._inst.resp
            reg_out = re.search('\s*.*inet addr:(.*)\s+Bcast.*',result)
            if reg_out:
                return reg_out.group(1)


    def getMAC(string, occurance=1):
        reload (re)
        pat = re.pattern(RegexPatterns["MAC"])
        if occurance == 1 :
            return re.search(pat,string,re.I).group()
        else:
            return [matchedpattern  \
                    for matchedpattern in \
                    re.finditer(RegexPatterns["MAC"],string)]


    def pingall(self):
        """
        :param nodes:
        :return:
        """
        result = self._inst.mini_execute_command(cmd="pingall")
        if result:
            return self._inst.resp


comment_flag = False
if comment_flag:
    def runpyline(self,cmd):
        """
        :param: python line execution
        :Ex: py dir(s1)-> To know the switch attributes
        :runpyline('dir(s1)')
        :return unbuffered response to the python line
        """
        self.rc.sendline("py %s")
        if self.rc.prompt():
            return self.rc.before

    def getlinks(self):
        """
        To display Links between hosts and switches
        """
        self.rc.sendline("net")
        if self.rc.prompt():
            return self.rc.before

    def getnodes(self):
        """
        To display nodes
        """
        self.rc.sendline("nodes")
        if self.rc.prompt():
            return self.rc.before

    def dump(self):
        """
        showing all info abt nodes
        """
        self.rc.sendline("dump")
        if self.rc.prompt():
            return self.rc.before


    def get_host_IP(self, host ='h1'):
        """
        To get Host Ip Address
        """
        self.rc.sendline("%s ifconfig -a" % str(host))
        if self.rc.prompt():
            return self.rc.before

    def get_switch_IP(self, switch='s1'):
        """
        to get Switch IP Address
        """
        self.rc.sendline("%s ifconfig -a" % str(switch))
        if self.rc.prompt():
            return self.rc.before

    def get_host_pid(self, host='h1'):
        """
        to get host pid
        """
        self.rc.sendline("%s ps -a" % str(host))
        if self.rc.prompt():
            return self.rc.before

    def get_switch_pid(self, switch='s1'):
        """
        To get Switch PID
        """
        self.rc.sendline("%s ps -a" % str(switch))
        if self.rc.prompt():
            return self.rc.before

    def perform_test(self):
        """
        Bandwidth testing
        """
        self.rc.sendline("iperf")
        if self.rc.prompt():
            return self.rc.before

    def get_ports(self):
        """
        get ports of network
        """
        self.rc.sendline("ports")
        if self.rc.prompt():
            return self.rc.before



import re
import time
import sys, os
from pexpect import pxssh
from patterns import RegexPatterns
from Interface import SSHConnection

DEBUG = False

def dlog(string):
    if DEBUG:
        print string


class MininetConnection(SSHConnection): 

    def __init__(self,*args,**kwargs):
        super(MininetConnection,self).__init__(*args,**kwargs)
        self.IP = kwargs['IP']
        self.usr = kwargs['username']
        self.pwd = kwargs['password']
        self.connected = False
        self.disconnected = False
        
    ##To make sure there is only a single instance of this class
    def __new__(self, *args, **kwargs):
        if not hasattr(self,"_inst"):
            self._inst = super(MininetConnection,self).__new__(self,*args,**kwargs)
            dlog("Creating a new instance for the class")
        else:
            dlog("Returning the already created instance...")
        return self._inst

    def connect(self,status = True, **kwargs):
        self.parameters = " "
        if status and not self.connected :
            try :
                self.rc.login(self.IP,self.usr,self.pwd)
            except Exception as E :
                print "Error during login:"+str(E)
                sys.exit(0)
            except ExceptionPxssh :
                print "Check IP, username and password!!"
                sys.exit(0)

            self.rc.sendline("sudo mn -c") ##Clearing off the previous session !
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
                self.nodes = kwargs.get('nodes')
                self.parameters += " --topo %s,%s "%(self.topo, str(self.nodes))
                
            dlog(self.parameters)
            self.rc.sendline("sudo mn %s"%(self.parameters))

            ##Force my session to use the mininet>> terminal
            if self.rc.prompt() is True : 
                self.rc.PROMPT = "mininet> "
                time.sleep(0.01)
                self.connected = True
                dlog(self.rc.before)
                return self.rc.prompt()
            else:
                self.rc.PROMPT = "mininet> "
                time.sleep(0.01)
                if self.rc.prompt() is True :
                    self.connected = True
                    dlog(self.rc.before)
                    return self.rc.prompt()
                else:
                    dlog(self.rc.before)
                    return False


    def disconnect(self,status= True):
        if status and not self.disconnected:
            self.rc.sendline("exit")
            self.rc.PROMPT = '\\[PEXPECT\\][\\$\\#] '
            time.sleep(0.1)
            if self.rc.prompt():
                self.rc.logout()
                self.disconnected = True
                del(self.rc)

    def customCommand(self,cmd):
        self.rc.sendline(cmd)
        if self.rc.prompt():
            return self.rc.before


    def ping(self,node1,node2):
        """
        :param nodes: arguments Two node names
        :return: response equivalent to "h1 ping h2 -c" in a mininet session
        """
        h1 = node1
        h2 = node2
        self.rc.sendline("""%s ping %s -c3"""%(h1,h2))
        time.sleep(0.01)
        if self.rc.prompt():
            return self.rc.before
        else:
            print "Timed-out!!!"


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
        self.rc.sendline("pingall")
        if self.rc.prompt():
            return self.rc.before

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

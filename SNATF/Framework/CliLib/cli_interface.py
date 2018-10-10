"""
Inherit the SSHConnection to build protocol specific class objects.
Ex:  Mininet, Telnetlib, etc.

"""
import os
import re
import time
import sys
from __builtin__ import locals
from log_generate import *
import pdb

sys.path.append('/usr/share/pycharm/helpers/')


if 'java' in sys.platform or os.name == 'nt':
    sys.path.append(r'C:\jython2.7.0\Lib\site-packages')
    from SSHLibrary.library import SSHLibrary
else:
    from pexpect import pxssh

Debug = False


def dlog(log):
    if Debug:
        print("\n{0}".format(log))

logger_name = __name__.split('.')[-1]
log_handler = fill_getLogger(logger_name)

class Connection(object):
    """
    Base class for all the types of connections.
    """
    log_handler = log_handler
    cmd_from='HM-SDN-NFV'

    def wri2log(self,msg):
        self.log_handler.CMD_FROM['cmd_from'] = self.cmd_from
        self.log_handler.writeTolog(msg=msg)

    def connect(self):
        pass

    def disconnect(self):
        pass


class SSHConnection(Connection):
    def __init__(self, IP, username, password, port=22):
        self.resp = ""
        if 'java' in sys.platform or os.name == 'nt':
            self.rc = _RobotSSHConnection(IP=IP, username=username, password=password, port=port)
        else:
            self.rc = _PexpectSSHConnection(IP=IP, username=username, password=password, port=port)

    def connect(self):
        return self.rc.connect()

#    def execute_command(self, cmd, wait=True):
#        status = self.rc.execute_command(cmd, wait=wait)
#        self.resp = self.rc.resp
#        return status

    def execute_command(self, cmd, exp_out=None, prompt="#"):
        flag=0
        if exp_out is not None:
            if self.rc.exe_cmd_out(cmd, exp_out):
                self.resp = self.rc.resp
                flag = 1
                self.log_handler.writeInfolog('%s'%self.rc.resp)
                return True
        else:
            if self.rc.execute_command(cmd,prompt):
                self.resp = self.rc.resp
                flag = 1
                self.log_handler.writeInfolog('%s' % self.rc.resp)
                return True
        if flag is 0:
            self.wri2log("\n!!!!!!!!!!!!! Wrong Command: %s"%cmd)
            return False

    def repeat_execute_command(self,max_timer,sleep_timer,brk_pattern,cmd,exp_out=None, prompt="#"):
        """
        To repeat any cmd exeution till provided timer expired
        """
        increment_flag = sleep_timer
        while(increment_flag <= max_timer):
            self.execute_command(cmd=cmd,exp_out=exp_out,prompt=prompt)
            if re.search(brk_pattern,self.resp):
                break
            time.sleep(sleep_timer)
            increment_flag = increment_flag  + sleep_timer
            
    def disconnect(self):
        return self.rc.disconnect()


class _PexpectSSHConnection(Connection):
    def __init__(self, IP, username, password, port=22):
        self.IP = IP
        self.rc = pxssh.pxssh()
        self.usr = username
        self.pwd = password
        self.port = port
        self.resp = ""

    def connect(self):
        self.rc.login(self.IP, self.usr, self.pwd)
        self.rc.sendline("")
        self.rc.setecho(False)
        if self.rc.prompt():
            #self.wri2log(self.rc.before)
            dlog(self.rc.before)
            self.rc.sendline("sudo su")
            if self.rc.expect(["password",'#']) == 0:
                self.rc.sendline(self.pwd)
                self.rc.expect("#")
            return True
        else:
            self.wri2log('*********************** FAILED TO GET EXPECTED PROMPT FOR %s, CHECK THE CONNECTIVITY ***********************'%self.IP)

    def disconnect(self):
        self.log_handler.writeInfolog(msg='**********  Closing the SSh Session  **********')
        self.rc.close()

    def execute_command(self, cmd, prompt):
        dlog("Command Execution: {0}".format(cmd))
#        pdb.set_trace()
        result = False
        self.rc.PROMPT = prompt
        self.rc.sendline(cmd)
        time.sleep(2)
        if self.rc.prompt(timeout=60):
            self.resp = self.rc.before
            dlog("Before=" + self.rc.before)
            dlog("After=" + self.rc.after)
            self.rc.buffer = ''               #when format is used, before size is exceeded so garbage output is given so freeing buffer everytime
            result = True
        else:
            self.log_handler.writeInfolog(">>>>> %s"%self.rc.buffer)
            self.log_handler.writeInfolog("<<<<< %s"%self.rc.before)
            self.log_handler.writeInfolog("###### %s"%self.rc.after)
        return result

    def exe_cmd_out(self, cmd, exp_out):
        result = False
        dlog("Command Execution: {0}".format(cmd))
        self.rc.sendline(cmd)
        temp = self.rc.expect(exp_out, timeout = 60)
        if temp is 0:
            self.resp = self.rc.before
            dlog("Before=" + self.rc.before)
            dlog("After=" + self.rc.after)
            result = True
        else:
            self.log_handler.writeInfolog(">>>>> %s"%self.rc.buffer)
            self.log_handler.writeInfolog("<<<<< %s"%self.rc.before)
            self.log_handler.writeInfolog("###### %s"%self.rc.after)

        return result

    def capture_output(self, wait):
        #if not wait:
        if self.rc.prompt():
            self.resp = self.rc.before
            dlog(self.resp)
            return self.rc.before

class _RobotSSHConnection(Connection):
    """
    This class used the Robot Framework SSHLibrary to provide an interface to connect and remotely execute commands.
    It is supported on both Jython and Python
    """

    def __init__(self, IP, username, password, port=22):
        self.rc = SSHLibrary()
        self.IP = IP
        self.usr = username
        self.pwd = password
        self.port = port
        self.resp = ""

    def connect(self):
        try:
            self.rc.open_connection(host=self.IP, port=self.port)
            self.rc.login(username=self.usr, password=self.pwd)
            return True
        except:
            return False

    def execute_command(self, cmd, wait):
        dlog("Command Execution: {0}".format(cmd))
        if wait:
            self.resp = self.rc.execute_command(cmd)
            dlog(self.resp)
            if self.resp:
                dlog("INFO: Successful Response")
                return True
            else:
                # dlog("INFO: No Response")
                return False
        else:
            self.rc.start_command(cmd)

    def capture_output(self, wait):
        if not wait:
            self.resp = self.rc.read_command_output()
        return self.resp

    def disconnect(self):
        self.rc.close_connection()


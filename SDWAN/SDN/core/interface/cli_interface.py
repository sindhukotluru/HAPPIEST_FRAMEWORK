"""
Inherit the SSHConnection to build protocol specific class objects.
Ex:  Mininet, Telnetlib, etc.

"""
import os
import time
import sys
from __builtin__ import locals

if 'java' in sys.platform or os.name == 'nt':
    sys.path.append(r'C:\jython2.7.0\Lib\site-packages')
    from SSHLibrary.library import SSHLibrary
else:
    from pexpect import pxssh

Debug = True


def dlog(log):
    if Debug:
        print("\n{0}".format(log))


class Connection(object):
    """
    Base class for all the types of connections.
    """

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

    def execute_command(self, cmd, wait=True):
        status = self.rc.execute_command(cmd, wait=wait)
        self.resp = self.rc.resp
        return status

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
            dlog(self.rc.before)
            return True

    def execute_command(self, cmd, wait):
        #dlog("Command Execution: {0}".format(cmd))
        self.rc.sendline(cmd)
        if wait:
            if self.rc.prompt():
                self.resp = self.rc.before
                #
                # dlog(self.rc.before)
                return True

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


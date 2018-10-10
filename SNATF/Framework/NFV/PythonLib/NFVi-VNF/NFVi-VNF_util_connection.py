from pexpect import pxssh


class Connection(object):
    """
    Base class for all the types of connections.
    """

    def connect(self):
        pass

    def disconnect(self):
        pass

    def execute_command(self, cmd):
        pass


class SSHConnection(Connection):
    def __init__(self, IP, username, password=None, ssh_key=None, port=22):
        self.resp = ""

        self.conn = _PexpectSSHConnection(IP=IP, username=username, password=password, ssh_key=ssh_key, port=port)

    def connect(self):
        return self.conn.connect()

    def execute_command(self, cmd):
        status = self.conn.execute_command(cmd)
        self.resp = self.conn.resp
        return status

    def disconnect(self):
        self.conn.disconnect()


class _PexpectSSHConnection(Connection):
    def __init__(self, IP, username, password=None, ssh_key=None, port=22):
        self.IP = IP
        self.rc = pxssh.pxssh()
        self.usr = username
        self.pwd = None
        self.ssh_key = None
        if password is not None:
            self.pwd = password
        self.port = port
        if ssh_key is not None:
            self.ssh_key = ssh_key
        self.resp = ""
        self.timeout = 30

    def connect(self):
        if self.pwd:
            self.rc.login(server=self.IP, username=self.usr, password=self.pwd, login_timeout=self.timeout)
        elif self.ssh_key:
            self.rc.login(server=self.IP, username=self.usr, ssh_key=self.ssh_key, login_timeout=self.timeout)
        self.rc.sendline("")
        self.rc.setecho(False)
        if self.rc.prompt():
            return True

    def execute_command(self, cmd):
        print "cmd: ", cmd
        self.rc.sendline(cmd)
        if self.rc.prompt():
            self.resp = self.rc.before
            return True

    def disconnect(self):
        self.rc.close()

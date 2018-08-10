from netmiko import ConnectHandler, SCPConn
class vyos_config:
    def __init__(self,host):
        vyos = ConnectHandler(device_type='vyos', ip=host, username='vyos', password='vyos')
        self.vyos = vyos
    def execute(self, command):
        output=self.vyos.send_command(command)
        print output
    def configure(self, commands):
        output=self.vyos.send_config_set(commands)
        print output
        self.vyos.commit()
        self.vyos.exit_config_mode()
    def file_transfer(self):
        scp_conn = SCPConn(self.vyos)
        s_file="/openvpn-1.key"
        d_file="/config/auth/openvpn-1.key"
        scp_conn.scp_transfer_file(s_file,d_file)

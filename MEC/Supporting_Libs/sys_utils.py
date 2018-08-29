from subprocess import Popen, PIPE
import re
from Supporting_Libs.cli_interface import SSHConnection
import platform
from Config import config


def create_ovs_bridge(obj, br_name, cntrlr_ip):
    """
    To configure ovs bridge
    :return:
    """
    return obj.create_validate_bridge(br_name=br_name, cntrlr=[cntrlr_ip, 6653])

def add_ports_to_ovs(obj,br_name, ports):
    return obj.addports_validate(br_name=br_name, ports=ports)

def flow_management(obj,manage_type,br_name,flow_inputs):
    for key, value in flow_inputs.items():
        if str(key) == 'Null':
            flow_inputs = None
    if str(manage_type) == 'delete': manage_type = 'delete'
    elif str(manage_type) == 'add': manage_type = 'add'
    return obj.manage_flows(manage_type=manage_type,br_name=br_name,flow_inputs=flow_inputs,controller=config.CONTROLLER_TYPE)


# TBD: Add validation for valid IP Address. Also consider the use pyping module.
def ping(ip, echo_count=1):
    cmd_args = []
    exp_message = None
    
    os_type = platform.system().lower()
    if platform.system().lower() == 'java':
        import java.lang
        os_type = java.lang.System.getProperty("os.name").lower()
    
    if 'windows' in os_type:
        cmd_args = ['-n', str(echo_count)]
        exp_message = "Packets: Sent = {0}, Received = {1}, Lost = 0 (0% loss)".format(echo_count, echo_count)
    else:
        cmd_args = ['-c{0}'.format(echo_count)]
        exp_message = "{0} packets transmitted, {1} received, 0% packet loss".format(echo_count, echo_count)
    

    cmd = Popen(["ping"] + [ip] + cmd_args, stdout=PIPE, stderr=PIPE)
    cmd_output = cmd.stdout.read()
    
    return True if exp_message in cmd_output else False

def remote_ping(source_ip, source_user, source_password, destination_ip, echo_count=1):
    status = False
    ssh_obj = SSHConnection(IP=source_ip, username=source_user, password=source_password)
    conn_status = ssh_obj.connect()
    if conn_status:
        print destination_ip
        print("SSH connection success")
        cmd = "ping {0} -c{1}".format(destination_ip, echo_count)
        if ssh_obj.execute_command(cmd=cmd):
            exp_message = r'{0} packets transmitted, {1} received, 0% packet loss'.format(echo_count, echo_count)
            command_output = ssh_obj.resp
            status = True if exp_message in command_output else False
    return status

def peer_ping(obj,count=config.pkt_count,source="h1",dest="h2"):
    return obj.ping(node1=source,node2=dest,count=count) if config.MININET else obj.ping(peer_ip=dest,count=count)


def start_capture(obj,iface,filter,count=config.pkt_count,node=None):
    return obj.start_capture_on_mini(iface=iface,filter=filter,node=node,count=count) if config.MININET \
        else obj.start_capture_on_host(iface=iface,filter=filter,count=count)

def stop_capture(obj,pid,node=None):
    return obj.stop_capture_on_mini(node=node,pid=pid) if config.MININET else obj.stop_capture_on_host(pid)

def get_data_from_file(obj,input_file,node=None):
    return obj.get_data_from_file(input_file=input_file,node=node) if config.MININET \
        else obj.get_data_from_file(input_file=input_file)

def peer_ping_capture(obj,node2,dst_nic,filter,node1=None,count=config.pkt_count):
    return obj.ping_n_capture(node1=node1,node2=node2,dst_nic=dst_nic,count=count,filter=filter) if config.MININET \
        else obj.ping_n_capture(node=node2,dst_nic=dst_nic,count=count,filter=filter)

def configure_host_nic_ip(obj,node,if_name,ip):
    return obj.config_host_nic_ip(node=node,if_name=if_name,ip=ip) if config.MININET \
        else obj.config_host_nic_ip(if_name=if_name,ip=ip)

def validate_output(search_str, input):
    #status_code = input.find(str(search_str))
    match_list = []
    match_list.extend(re.findall(r'%s'%search_str,input))
    return len(match_list)

def make_mec_input(input_data,services):
    default_services = ['Ip-Tables','DNS-MASq','Telemetry']
    alias_services = ['firewall','dns','telemetry']
    for service in default_services:
        if service not in services:
            if input_data.has_key('services'):
                for key,value in input_data['services'].items():
                    if value == service:
                        input_data['services'].pop(key)
            elif input_data.has_key('config'):
                #input_data["config"]['vlan'][0].pop(service)
                if service != 'Telemetry':
                    input_data["config"]['vlan'][0][alias_services[default_services.index(service)]]=[]
                    name = 'fwS' if 'Ip' in service else 'dnsS'
                    input_data["config"]['vlan'][0][name] = "false"
                else:
                    input_data["config"]['vlan'][0]["telemetry"][0]["selected"]="false"
    return input_data














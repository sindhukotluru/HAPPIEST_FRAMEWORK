import util_findhost
from util_connection import SSHConnection
import time
import os
import subprocess
import json

def parse_json(cmd, stack_name, key=None):
    if cmd == 'stackShow':
        ost_cmd = "openstack stack show " + stack_name + " -f json"
    if cmd == 'serverShow':
        ost_cmd = "openstack server show " + stack_name + " -f json"
    if cmd == 'imageShow':
        ost_cmd = "openstack image show " + stack_name + " -f json"
    print "show_stack_command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    if key == "noStack":
        return output
    data = json.loads(output)
    if key == "server_name":
        return data["outputs"][0]["output_value"]
    elif key != None:
        return data[key]
    else:
        return data

def validate_ip_vnf_multistack(multi_stack_name):
    login_ip = []
    time.sleep(30)
    ost_cmd = "openstack server list | grep %s-server1" % multi_stack_name
    print "Command1: %s" % ost_cmd
    output = exec_sys_command(ost_cmd)
    exact_server_name1 = output.split('|')[2].split()[0]
    login_ip.append(output.split('|')[4].split(',')[1].split(';')[0].split()[0])

    ost_cmd = "openstack server list | grep %s-server2" % multi_stack_name
    print "Command2: %s" % ost_cmd
    output = exec_sys_command(ost_cmd)
    exact_server_name2 = output.split('|')[2].split()[0]
    login_ip.append(output.split('|')[4].split(',')[1].split(';')[0].split()[0])
    # login_ip = get_multi_float_ip(multi_stack_name)

    ost_cmd = "openstack server list | grep %s-server3" % multi_stack_name
    print "Command2: %s" % ost_cmd
    output = exec_sys_command(ost_cmd)
    exact_server_name2 = output.split('|')[2].split()[0]
    login_ip.append(output.split('|')[4].split(',')[1].split(';')[0].split()[0])

    exact_server_name = [exact_server_name1, exact_server_name2]
    print "Login IP: %s" %login_ip

    for idx, server_name in enumerate(exact_server_name):
        ip_float = login_ip[idx]
        print "IP Float: %s " % ip_float
        try:
            try:
                c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/lcm/key234demo.pem")
                c1.connect()
            except:
                c1 = SSHConnection(IP=ip_float, username="centos", ssh_key="/home/test/automation/lcm/key234demo.pem")
                c1.connect()
                #c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
                #c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
        except:
            print "first connection failed"
	    time.sleep(180)
            try:
                c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/lcm/key234demo.pem")
            except:
                c1 = SSHConnection(IP=ip_float, username="centos", ssh_key="/home/test/automation/lcm/key234demo.pem")
            #c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
            #c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
            c1.connect()
            print "Connection Successful"
        c1.disconnect()
    return login_ip

def test_icmp_traffic(login_ip1, login_ip3):
    status = True
    c1 = SSHConnection(IP=login_ip1, username="ubuntu", ssh_key="/home/test/automation/lcm/key234demo.pem")
    c3 = SSHConnection(IP=login_ip3, username="ubuntu", ssh_key="/home/test/automation/lcm/key234demo.pem")
    #c1 = SSHConnection(IP=login_ip1, username="ubuntu", password="ubuntu")
    #c3 = SSHConnection(IP=login_ip3, username="ubuntu", password="ubuntu")
    if c1.connect() and c3.connect():
        c3.execute_command("ifconfig ens3")
        eth1_detail = c3.conn.rc.before
        c3_eth1_ip = util_findhost.search_host(eth1_detail)
        print "c3_eth1_ip :", c3_eth1_ip
        cmd = "ping -c 3 " + c3_eth1_ip
        pat = "0% packet loss"
        check1 = run_check_cmd(c1, cmd, pat)
        print "the value of icmp check1 is:", check1
        if check1:
            print "Verification of Ping test -- Successful"
        else:
            status = False
            print "Verification of Ping test -- Failed."

        c1.disconnect()
        c3.disconnect()
        return status

def vnf_create_multistack(stack_name):
    if not create_stack(stack_name, 'ubuntu_multiserver.yml'):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    if stack_create_status == "Stack CREATE completed successfully":
        if validate_ip_vnf_multistack(stack_name):
            print "server ip validation PASS"
            return True
        else:
            print "server ip validation failed"
            return False
    else:
        print "stack_create_status is:", stack_create_status
        return False

def vnf_icmp_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)

    login_ip = validate_ip_vnf_multistack(stack_name)

    result = test_icmp_traffic(login_ip[0], login_ip[2])

    return result

set_environment("admin-openrc")
def test_complete():
    pass

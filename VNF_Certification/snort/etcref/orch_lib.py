import util_findhost
from util_connection import SSHConnection
import time
import os
import subprocess
import json

import paramiko
import re
import logging
import logging.handlers
# import socket
# import iptc
# from subprocess import call
# from netmiko.ssh_exception import NetMikoTimeoutException
# import nfv_lib
import re

import sys

def exec_sys_command(cmd):
    #return os.popen(cmd).read()
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    if out:
        return out
    if err:
        return err
	
def create_stack(stack_name, heat_tmplt):
    ost_cmd = 'openstack stack create -t /home/test/automation/rmaity/test_demo/yaml/' + heat_tmplt + ' ' + stack_name
    print "create vm command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return False if output.find(stack_name) == -1 else True
    # return True

def upgrade_stack(stack_name, heat_tmplt):
    ost_cmd = 'openstack stack update -t /home/test/automation/rmaity/test_demo/yaml/' + heat_tmplt + ' ' + stack_name
    print "create vm command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return False if output.find(stack_name) == -1 else True

def downgrade_stack(stack_name, heat_tmplt):
    ost_cmd = 'openstack stack update -t /home/test/automation/rmaity/test_demo/yaml/' + heat_tmplt + ' ' + stack_name
    print "create vm command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return False if output.find(stack_name) == -1 else True

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
	    
def delete_stack(stack_name):
    ost_cmd = "openstack stack delete --yes " + stack_name
    print "Delete stack command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return output 

def delete_server(server_name):
    ost_cmd = "openstack server delete --wait " + server_name
    print "Delete server command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return output

def reboot_server(server_name, boot_type='soft'):
    if boot_type == 'soft':
        ost_cmd = "openstack server reboot --soft --wait " + server_name
    elif boot_type == 'hard':
        ost_cmd = "openstack server reboot --hard --wait " + server_name
    else:
        print "Invalid boot type"
        return False
    output = exec_sys_command(ost_cmd)
    return output

def create_snapshot(server_name, snapshot_name):
    ost_cmd = "openstack server list | grep %s" % server_name
    output = exec_sys_command(ost_cmd)
    exact_server_name = output.split('|')[2].split()[0]
    ost_cmd = "openstack server image create %s --name %s" %(exact_server_name, snapshot_name)
    print "Create snapshot command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    time.sleep(180)
    return False if output.find(snapshot_name) == -1 else True

def delete_snapshot(snapshot_name):
    ost_cmd = "openstack image delete " + snapshot_name
    print "Revert snapshot command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return output 

def pause_server(server_name):
    ost_cmd = "openstack server pause " + server_name
    print "Server pause command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return output

def unpause_server(server_name):
    ost_cmd = "openstack server unpause " + server_name
    print "Server unpause command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return output

def suspend_server(server_name):
    ost_cmd = "openstack server suspend " + server_name
    print "Server suspend command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return output 

def resume_server(server_name):
    ost_cmd = "openstack server resume " + server_name
    print "Server resume command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return output

def migrate_server(server_name):
    ost_cmd = "openstack server migrate --shared-migration --wait " + server_name
    print "Server migrate command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return False if output.find(server_name) == -1 else True

def live_migrate_server(server_name):
    ost_cmd = "openstack server migrate --live cirros32 --wait " + server_name
    print "Server migrate command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return False if output.find(server_name) == -1 else True

def validate_ip_vnf(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    ip_set = parse_json('serverShow', server_name, "addresses")
    # ip_eth0 = None
    print ip_set
    if ';' in ip_set:
        ip2 = ip_set.split(';')[0].split("=")[1]
        ip_set = ip_set.split(';')[1]
    else:
        ip2 = None
    ip = ip_set.split(',')[0].split("=")[1]
    ip_float = ip_set.split(',')[1]
    subprocess.call(["sudo", "dhclient", "eth1"])
    subprocess.call(["cp", "/dev/null", "/home/test/.ssh/known_hosts"])
    c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
    # c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
    try:
        c1.connect()
    except:
        print "first connection failed"
        time.sleep(180)
        c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
        # c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
        c1.connect()
    c1.execute_command("sudo ifconfig eth0")
    intf_v = c1.conn.rc.before
    ip_eth0 = util_findhost.search_host(intf_v)
    if ip2:
        c1.execute_command("sudo ifconfig eth1")
        intf_v = c1.conn.rc.before
        ip_eth1 = util_findhost.search_host(intf_v)
    c1.disconnect()
    if ip2:
        assert ip_eth1 == ip2
    return ip_eth0 == ip

def set_environment(env_file):
    script = "/home/test/automation/rmaity/test_demo/" + env_file
    out = subprocess.Popen(". %s; env" % script, stdout=subprocess.PIPE, shell=True)
    output = out.communicate()[0]
    environment_var = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(environment_var)
    time.sleep(5)

def create_stack_test(stack_name, yaml_name):
    if not create_stack(stack_name, yaml_name):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    if stack_create_status == "Stack CREATE completed successfully":
        return validate_ip_vnf_multinw(stack_name)
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_with_snapshot_test(stack_name, yaml_name):
    if not create_stack(stack_name, yaml_name):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    if stack_create_status == "Stack CREATE completed successfully":
        return validate_ip_vnf_multinw(stack_name)
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_multi_network_test(stack_name, yaml_name):
    if not create_stack(stack_name, yaml_name):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    if stack_create_status == "Stack CREATE completed successfully":
        if validate_ip_vnf_multinw(stack_name):
            print "server ip validation pass"
            return True
        else:
            return False
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_multi_network_multi_server_test(stack_name, yaml_name):
    if not create_stack(stack_name, yaml_name):
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

def multi_network_multi_server_icmp_test(stack_name):
    set_environment("demo-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)

    login_ip = validate_ip_vnf_multistack(stack_name)

    result = test_icmp_traffic(login_ip[0], login_ip[1])

    return result

def multi_network_multi_server_iperf3_traffic_test(stack_name):
    set_environment("demo-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)

    login_ip = validate_ip_vnf_multistack(stack_name)

    result = test_iperf3_traffic(login_ip[0], login_ip[1])

    return result

def upgrade_stack_test(stack_name, new_yaml):
    if not upgrade_stack(stack_name, new_yaml):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    return True if stack_create_status == "Stack UPDATE completed successfully" else False

def downgrade_stack_test(stack_name, new_yaml):
    if not downgrade_stack(stack_name, new_yaml):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    return True if stack_create_status == "Stack UPDATE completed successfully" else False

def delete_stack_test(stack_name):
    retVal = delete_stack(stack_name)
    if not retVal == None:
        print "stack deletion failed: " + retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('stackShow', stack_name, "noStack")
    return stack_create_status == "Stack not found: " + stack_name + "\n"

def delete_stack_multi_server_test(stack_name):
    retVal = delete_stack(stack_name)
    if not retVal == None:
        print "stack deletion failed: " + retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('stackShow', stack_name, "noStack")
    return stack_create_status == "Stack not found: " + stack_name + "\n"

def delete_server_test(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = delete_server(server_name)
    if not retVal == "\n":
        print "server deletion failed: " + retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "noStack")
    return stack_create_status == "No server with a name or ID of '%s' exists.\n" % server_name

def soft_reboot_stack_test(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = reboot_server(server_name, 'soft')
    if retVal != "Complete\n":
        print "server soft reboot failed", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    print "stack_create_status", stack_create_status
    return stack_create_status == "ACTIVE"

def soft_reboot_stack_multi_network_test(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = reboot_server(server_name, 'soft')
    if retVal != "Complete\n":
        print "server soft reboot failed", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    print "stack_create_status", stack_create_status
    if validate_ip_vnf_multistack(stack_name):
        print "server ip validation PASS"
    else:
        print "server ip validation failed"
        return False
    return stack_create_status == "ACTIVE"

def hard_reboot_server_test(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = reboot_server(server_name, 'hard')
    if retVal != "Complete\n":
        print "server hard reboot failed", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "ACTIVE"

def create_snapshot_test(stack_name, snapshot_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    if not create_snapshot(server_name, snapshot_name):
        return False
    time.sleep(30)
    stack_create_status = parse_json('imageShow', snapshot_name, "status")
    return stack_create_status == "active"

def delete_snapshot_test(snapshot_name):
    retVal = delete_snapshot(snapshot_name)
    if not retVal == None:
        print "snapshot deletion failed", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('imageShow', snapshot_name, "noStack")
    return stack_create_status == "Could not find resource " + snapshot_name + "\n"

def pause_server_test(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = pause_server(server_name)
    if not retVal == None:
        print "server pause failed: ", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "PAUSED"

def unpause_server_test(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = unpause_server(server_name)
    if not retVal == None:
        print "server unpause failed: ", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "ACTIVE"

def suspend_server_test(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = suspend_server(server_name)
    if not retVal == None:
        print "server suspend failed: ", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "SUSPENDED"

def resume_server_test(stack_name):
        server_name = parse_json('stackShow', stack_name, "server_name")
        retVal = resume_server(server_name)
        if not retVal == None:
            print "server resume failed: ", retVal
            return False
        time.sleep(30)
        stack_create_status = parse_json('serverShow', server_name, "status")
        return stack_create_status == "ACTIVE"

def create_image(image_name):
    status = True
    cmd = "openstack image create --disk-format=qcow2  --file=/home/test/automation/rmaity/test_demo/image/cirros-0.3.5-x86_64-disk.img " + image_name
    print "command: ", cmd
    out = exec_sys_command(cmd)
    if out.find(image_name) != -1:
        print "Image - " + image_name + " -- successfully created"
    else:
        status = False
    return status

def delete_image(image_name):
    status = True
    cmd = "openstack image delete " + image_name
    out = exec_sys_command(cmd)
    if out.find(image_name) == None:
        print "Image - " + image_name + " -- successfully deleted"
    else:
        status = False
    return status

def create_image_test(image_name):
    if not create_image(image_name):
        return False
    time.sleep(30)
    return 'PASS'

def delete_image_test(image_name):
    if not delete_image(image_name):
        return False
    time.sleep(30)
    return 'PASS'

def create_network(network_name, subnet):
    status = True
    cmd1 = "openstack network create --share --enable " + network_name
    cmd2 = "openstack subnet create " + network_name + " --network " + network_name + " --subnet-range " + subnet + "/24"
    cmd3 = "openstack subnet show " + network_name
    print "cmd1: ", cmd1
    print "cmd2: ", cmd2
    output1 = exec_sys_command(cmd1)
    if output1.find(network_name) != -1:
        exec_sys_command(cmd2)
        out = exec_sys_command(cmd3)
        if out.find(network_name) != -1:
            print "Network - " + network_name + " -- successfully created"
        else:
            status = False
    else:
        status = False
    return status

def delete_network(network_name):
    status = True
    cmd = "openstack network delete " + network_name
    out = exec_sys_command(cmd)
    if out.find(network_name) == None:
        print "network - " + network_name + " -- successfully deleted"
    else:
        status = False
    return status

def create_network_test(network_name):
    if not create_network(network_name, '11.1.1.0'):
        return False
    time.sleep(30)
    return 'PASS'

def delete_network_test(network_name):
    if not delete_network(network_name):
        return False
    time.sleep(30)
    return 'PASS'

def get_float_ip(multi_nw_name):
    ost_cmd = "openstack server list | grep %s-server" % multi_nw_name
    print "Command: %s" % ost_cmd
    output = exec_sys_command(ost_cmd)
    try:
        float_ip = output.split('|')[4].split(',')[1].split(';')[0].split()[0]
        print "Floatting IP: %s " % float_ip
        return float_ip
    except:
        print "Please check stack creation. No floating IP found"
        return False

def get_multi_float_ip(multi_stack_name):
    float_ip = []
    ost_cmd = "openstack server list | grep %s-server1" % multi_stack_name
    print "Command1: %s" % ost_cmd
    output = exec_sys_command(ost_cmd)
    try:
        float_ip.append(output.split('|')[4].split(',')[1].split(';')[0].split()[0])
        print "Floatting IP: %s " % float_ip[0]
    except:
        print "Please check stack creation. No floating IP found"
        return False

    ost_cmd = "openstack server list | grep %s-server2" % multi_stack_name
    print "Command2: %s" % ost_cmd
    output = exec_sys_command(ost_cmd)

    try:
        float_ip.append(output.split('|')[4].split(',')[1].split(';')[0].split()[0])
        print "Floatting IP: %s " % float_ip[0]
        return float_ip
    except:
        print "Please check stack creation. one or more floating IP NOT found"
        return False

'''
def validate_ip_vnf_multinw(multi_nw_name):
    ost_cmd = "openstack server list | grep %s-server" % multi_nw_name
    print "Command: %s" % ost_cmd
    output = exec_sys_command(ost_cmd)
    server_name = output.split('|')[2].split()[0]
    login_ip = output.split('|')[4].split(',')[1].split(';')[0].split()[0]

    ip_float = login_ip
    print "IP Float: %s " % ip_float
    #c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
    c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
    try:
        c1.connect()
    except:
        print "first connection failed"
        time.sleep(180)
        #c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
        c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
        c1.connect()
        print "Connection Successful"
        c1.disconnect()
    return login_ip
'''
def validate_ip_vnf_multinw(multi_nw_name):
    ip_float = get_float_ip(multi_nw_name)
    if (ip_float):
        #c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
        c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
        try:
            c1.connect()
        except:
            print "first connection failed"
            time.sleep(180)
            #c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
            c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
            c1.connect()
            print "Connection Successful"
            c1.disconnect()
        return ip_float
    else:
        print "IP verification Failed"
        return False

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

    exact_server_name = [exact_server_name1, exact_server_name2]
    print "Login IP: %s" %login_ip

    for idx, server_name in enumerate(exact_server_name):
        ip_float = login_ip[idx]
        print "IP Float: %s " % ip_float
        #c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
        c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
        try:
            c1.connect()
        except:
            print "first connection failed"
            time.sleep(180)
            #c1 = SSHConnection(IP=ip_float, username="ubuntu", ssh_key="/home/test/automation/rmaity/test_demo/key234demo.pem")
            c1 = SSHConnection(IP=ip_float, username="ubuntu", password="ubuntu")
            c1.connect()
            print "Connection Successful"
        c1.disconnect()
    return login_ip

def run_check_cmd(handle, cmd, pattern):
    handle.execute_command(cmd)
    if cmd.find("ping") == -1:
        time.sleep(15)
    else:
        time.sleep(2)
    if handle.conn.rc.before.find(pattern) != -1:
        return True
    else:
        return  False

def intf_ip(stack_name):
    ost_cmd5 = "openstack server show " + stack_name + " --format json | grep addresses"
    print "show_server_command for intf ip: ", ost_cmd5
    output = exec_sys_command(ost_cmd5).strip()
    ipset = util_findhost.get_ip_set(output)
    return ipset

def run_nt_check_cmd(handle, cmd, pattern):
    handle.execute_command(cmd)
    if cmd.find("ping") == -1:
        time.sleep(15)
    else:
        time.sleep(2)
    if handle.conn.rc.before.find(pattern) == -1:
        return True
    else:
        return False

def setup_vnf_vm(handle):
    handle.execute_command("sudo chmod 777 /etc/resolv.conf")
    handle.execute_command("sudo echo 'nameserver 8.8.8.8' >> /etc/resolv.conf")
    time.sleep(5)
    handle.execute_command("ping -c 3 www.google.com")
    if handle.conn.rc.before.find("0% packet loss") != -1:
        print "check internet 1: ", handle.conn.rc.before
        print("VM1 - Connected to Google.com")

def show_stack(stack_name):
    ost_cmd2 = "openstack stack show " + stack_name + " | grep 'output_value: " + stack_name + "' | awk ' { print $4 }'"
    print "show_stack_command: ", ost_cmd2
    output = exec_sys_command(ost_cmd2).strip()
    return output

def route_add(handle, cmd_rt_add):
    handle.execute_command(cmd_rt_add)

def vnf_infrastructure_setup(vm1_name, vm2_name, vm3_name):
    network = {"net1":"10.11.1.0", "net2":"10.12.1.0"}

    yml_name = ['yaml/ubuntu1.yml', 'yaml/vyos.yml', 'yaml/ubuntu2.yml']
    set_environment("admin-openrc")
    time.sleep(5)

    for network_name, subnet in network.items():
        status = create_network(network_name, subnet)
        if status:
            pass

    set_environment("admin-openrc")
    time.sleep(5)

    if (create_stack_test(vm1_name, yml_name[0])):
        print ("SUCCESS: Stack %s created successfully" %vm1_name)
        time.sleep(30)
    else:
        print ("FAILED: Stack %s creation failed; exiting test!!" %vm1_name)
        sys.exit()

    if (create_stack_test(vm2_name, yml_name[1])):
        print ("SUCCESS: Stack %s created successfully" %vm2_name)
        time.sleep(30)
    else:
        print ("FAILED: Stack %s creation failed; exiting test!!" %vm2_name)
        sys.exit()

    if (create_stack_test(vm3_name, yml_name[2])):
        print ("SUCCESS: Stack %s created successfully" %vm3_name)
        time.sleep(30)
    else:
        print ("FAILED: Stack %s creation failed; exiting test!!" %vm3_name)
        sys.exit()

    stack_name_1 = show_stack(vm1_name)
    print "stack_name_1: ", stack_name_1

    stack_name_2 = show_stack(vm2_name)
    print "stack_name_2: ", stack_name_2

    stack_name_3 = show_stack(vm3_name)
    print "stack_name_3: ", stack_name_3

    time.sleep(10)

    # vm_name.extend([stack_name_1, stack_name_2, stack_name_3])

    op1 = intf_ip(stack_name_1)
    print "op1 :: ", op1
    login_ip_vm_1 = op1[0].strip()
    print "login_ip_vm_1: ", login_ip_vm_1

    op3 = intf_ip(stack_name_2)
    print "op3 :: ", op3
    login_ip_vm_2 = op3[0].strip()
    print "login_ip_vm_2: ", login_ip_vm_2

    op4 = intf_ip(stack_name_3)
    print "op4 :: ", op4
    login_ip_vm_3 = op4[0].strip()
    print "login_ip_vm_3: ", login_ip_vm_3

    op1 = intf_ip(stack_name_1)
    print "op1 :: ", op1
    configure_ip_vm_1 = op1[1].strip()
    print "configure_ip_vm_1: ", configure_ip_vm_1

    op7 = intf_ip(stack_name_2)
    print "op7 :: ", op7
    configure_ip1_vm_2 = op7[1].strip()
    print "configure_ip1_vm_2: ", configure_ip1_vm_2

    op8 = intf_ip(stack_name_2)
    print "op8 :: ", op8
    configure_ip2_vm_2 = op8[2].strip()
    print "configure_ip2_vm_2: ", configure_ip2_vm_2

    op10 = intf_ip(stack_name_3)
    print "op10 :: ", op10
    configure_ip1_vm_3 = op10[1].strip()
    print "configure_ip1_vm_3: ", configure_ip1_vm_3

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    os.system("> /home/execution/.ssh/known_hosts")

    time.sleep(240)
    print login_ip_vm_1, login_ip_vm_2, login_ip_vm_3, configure_ip_vm_1, \
        configure_ip1_vm_2, configure_ip2_vm_2, configure_ip1_vm_3
    '''
    vm_ip.extend(
        [login_ip_vm_1, login_ip_vm_2, login_ip_vm_3, configure_ip_vm_1,
         configure_ip1_vm_2, configure_ip2_vm_2, configure_ip1_vm_3])

    vm_detail.extend(
        [login_ip_vm_1, login_ip_vm_2, login_ip_vm_3, configure_ip_vm_1,
         configure_ip1_vm_2, configure_ip2_vm_2, configure_ip1_vm_3])

    return vm_detail
    '''

def test_vm_config(login_ip1, login_ip2, login_ip3, conf_ip1_vm2, conf_ip2_vm2, vm1_name, vm2_name, vm3_name):

    c1 = SSHConnection(IP=login_ip1, username="ubuntu", password="ubuntu")
    c3 = SSHConnection(IP=login_ip3, username="ubuntu", password="ubuntu")
    time.sleep(30)

    con_handle = [c1, c3]

    if c1.connect() and c3.connect():
        time.sleep(30)
        c1.execute_command("ifconfig -a | grep ^e")
        print "intf detail 2 ::: ", c1.conn.rc.before
        intf_v1 = c1.conn.rc.before
        intf_list_v1 = util_findhost.get_intf(intf_v1)
        print "intf_list_v1 ::: ", intf_list_v1
        time.sleep(5)

        c3.execute_command("ifconfig -a | grep ^e")
        print "intf detail 3 ::: ", c3.conn.rc.before
        intf_v3 = c3.conn.rc.before
        intf_list_v3 = util_findhost.get_intf(intf_v3)
        print "intf_list_v3 ::: ", intf_list_v3
        time.sleep(5)

        for con in con_handle:
            setup_vnf_vm(con)

        time.sleep(5)

        vm1_rt = ["sudo route add -net 10.12.1.0/24 gw " + conf_ip1_vm2]
        route_add(c1, vm1_rt)
        
        vm3_rt = ["sudo route add -net 10.11.1.0/24 gw " + conf_ip2_vm2]
        route_add(c3, vm3_rt)
        
        logging.info("SSH to VM2")
        i=1
        while(i<=50):
            try:
                # VM2 = vyos_config(login_ip2)
                break
            except:
                i += 1
                print ("ssh timeout. Try %s times untill it is connected" % (10-i))
                time.sleep(10)

        logging.info("Configure RIPv2 in VM2")
        # VM2.configure(['set interfaces loopback address 1.1.1.1/32','set protocols rip network 10.11.1.0/24',
        #                'set protocols rip network 10.12.1.0/24', 'set protocols rip redistribute connected'])
                      
        logging.info("Sleeping 30 seconds for RIP to come up")
        time.sleep(30)
        
        c1.disconnect()
        c3.disconnect()

def test_icmp_traffic(login_ip1, login_ip3):
    status = True
    c1 = SSHConnection(IP=login_ip1, username="ubuntu", password="ubuntu")
    c3 = SSHConnection(IP=login_ip3, username="ubuntu", password="ubuntu")
    if c1.connect() and c3.connect():
        c3.execute_command("ifconfig ens5")
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

def multi_network_multi_server_http_traffic_test(stack_name):
    set_environment("demo-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)

    login_ip = validate_ip_vnf_multistack(stack_name)

    result = test_http_traffic(login_ip[0], login_ip[1])

    return result

def test_http_traffic(login_ip1, login_ip3):
    status = True
    c1 = SSHConnection(IP=login_ip1, username="ubuntu", password="ubuntu")
    c3 = SSHConnection(IP=login_ip3, username="ubuntu", password="ubuntu")
    if c1.connect() and c3.connect():
        c3.execute_command("ifconfig ens5")
        eth1_detail = c3.conn.rc.before
        c3_eth1_ip = util_findhost.search_host(eth1_detail)

        c1.execute_command("ifconfig ens5")
        eth1_detail = c1.conn.rc.before
        c1_eth1_ip = util_findhost.search_host(eth1_detail)

        print "c3_eth1_ip :", c3_eth1_ip
        cmd = "i=0; while [ $i -lt 10 ]; do wget http://" + c3_eth1_ip + ";sleep 1; $i=$i+1;done"
        #pat = "HTTP request sent, awaiting response... 200 OK"
        pat = "200 OK"

        cmd1 = 'sudo tcpdump -nqt -s 0 -A -i ens4 port 80 | grep "IP ' + c1_eth1_ip + '"'
        pat1 = c1_eth1_ip
        check1 = run_check_cmd(c1, cmd, pat)
        check2 = run_check_cmd(c3, cmd1, pat1)
        if check1 and check2:
            print "Verification of traffic test before disabling http -- Successful"
        else:
            status = False
            print "Verification of traffic test before disabling icmp -- Failed."
        c1.disconnect()
        c3.disconnect()
        return status

def test_iperf3_traffic(login_ip1, login_ip3):
    status = True
    c1 = SSHConnection(IP=login_ip1, username="ubuntu", password="ubuntu")
    c3 = SSHConnection(IP=login_ip3, username="ubuntu", password="ubuntu")
    if c1.connect() and c3.connect():
        c3.execute_command("ifconfig ens5")
        eth1_detail = c3.conn.rc.before
        c3_eth1_ip = util_findhost.search_host(eth1_detail)
        '''
        print "c3_eth1_ip :", c3_eth1_ip
        cmd = "ping -c 3 " + c3_eth1_ip
        pat = "0% packet loss"
        check1 = run_check_cmd(c1, cmd, pat)
        print "the value of icmp check1 is:", check1
        if check1:
            print "Verification of Ping test before disabling icmp -- Successful"
        else:
            status = False
            print "Verification of Ping test before disabling icmp -- Failed."
        '''
        logging.info("VM1 is client and VM3 is server")
        traffic_iperf3(login_ip1, c3_eth1_ip, "server")
        traffic_iperf3(login_ip3, c3_eth1_ip, "client")

        c1.disconnect()
        c3.disconnect()
        return status

def traffic_iperf3(host, server_ip, mode):
    # k = paramiko.RSAKey.from_private_key_file("/userkey.pem")
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("connecting to %s"%host)
    H.connect( hostname = host, username = "ubuntu", password="ubuntu" )
    logging.info("connected to %s"%host)
    if mode=="client":
        stdin , stdout, stderr = H.exec_command("iperf3 -c %s"%server_ip)
        result=stdout.read()
        logging.info(result)
        m=re.search(b'.*\s+([0-9\.]+)\s+(\w+)\s+([0-9\.]+)\s+\w+/sec\s+\d+\s+sender', result,re.M)
        n=re.search(b'.*\s+([0-9\.]+)\s+(\w+)\s+([0-9\.]+)\s+\w+/sec\s+receiver', result,re.M)
        if float(m.group(1))>0:
            logging.info("Client %s had sent %s%s traffic"%(host,m.group(1),m.group(2)))
        else:
            logging.error("Client %s had sent %s%s traffic"%(host,m.group(1),m.group(2)))

        if float(n.group(1))>0:
            logging.info("Client %s had received %s%s traffic"%(host,n.group(1),n.group(2)))
        else:
            logging.error("Client %s had received %s%s traffic"%(host,n.group(1),n.group(2)))
    else:
        stdin , stdout, stderr = H.exec_command("iperf3 -s -D")
        logging.info("iperf3 server started successfully")
        
    H.close()


set_environment("demo-openrc")
def test_complete():
    pass




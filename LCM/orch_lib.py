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
from subprocess import call
from netmiko.ssh_exception import NetMikoTimeoutException
# import nfv_lib
import re

import sys

def exec_sys_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    if out:
        return out
    if err:
        return err
	
def create_stack(stack_name, yaml_path, heat_tmplt, mgmt_nw, image, flavor, key, network_id = None, network_id2 = None):
    ost_cmd = 'openstack stack create -t %s%s %s ' % (yaml_path, heat_tmplt, stack_name)
    if mgmt_nw or image or flavor or key:
        ost_cmd = ost_cmd + ' --parameter "'
        if mgmt_nw:
            ost_cmd = ost_cmd + 'NetID=%s;' % mgmt_nw
        if network_id:
            ost_cmd = ost_cmd + 'NetID2=%s;' % network_id
        if network_id2:
            ost_cmd = ost_cmd + 'NetID3=%s;' % network_id2
        if image:
            ost_cmd = ost_cmd + 'IMAGE=%s;' % image
        if flavor:
            ost_cmd = ost_cmd + 'FLAVOR=%s;' % flavor
        if key:
            ost_cmd = ost_cmd + 'KEY=%s;' % key
        ost_cmd = ost_cmd[:-1] + '"'

    logging.info("create vm command: %s" % ost_cmd)
    output = exec_sys_command(ost_cmd)
    return False if output.find(stack_name) == -1 else True

def upgrade_stack(stack_name, yaml_path, heat_tmplt, image, flavor):
    ost_cmd = 'openstack stack update -t %s%s %s ' % (yaml_path, heat_tmplt, stack_name)
    if image or flavor:
        ost_cmd = ost_cmd + ' --parameter "'
        if image != None:
            ost_cmd = ost_cmd + 'IMAGE=%s;' % image
        if flavor:
            ost_cmd = ost_cmd + 'FLAVOR=%s;' % flavor
        ost_cmd = ost_cmd[:-1] + '"'

    logging.info("Upgrade vm command: %s" % ost_cmd)
    output = exec_sys_command(ost_cmd)
    return False if output.find(stack_name) == -1 else True

def downgrade_stack(stack_name, yaml_path, heat_tmplt, image, flavor):
    ost_cmd = 'openstack stack update -t %s%s %s ' % (yaml_path, heat_tmplt, stack_name)
    if image or flavor:
        ost_cmd = ost_cmd + ' --parameter "'
        if image != None:
            ost_cmd = ost_cmd + 'IMAGE=%s;' % image
        if flavor:
            ost_cmd = ost_cmd + 'FLAVOR=%s;' % flavor
        ost_cmd = ost_cmd[:-1] + '"'

    logging.info("Downgrade vm command: %s" % ost_cmd)
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

def set_environment(env_file):
    out = subprocess.Popen(". %s; env" % env_file, stdout=subprocess.PIPE, shell=True)
    output = out.communicate()[0]
    environment_var = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(environment_var)
    time.sleep(5)

def create_stack_test(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, key_loc, username, password):
    if not create_stack(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status

    if stack_create_status == "Stack CREATE completed successfully":
        key = key_loc + key + '.pem'
        return validate_ip_vnf_multinw(stack_name, username, key, password)
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_with_snapshot_test(stack_name, yaml_path, yaml_name, mngt_nw, network_id, image, flavor, key, key_loc, username, password):
    if not create_stack(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, network_id):
        return False
    time.sleep(80)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status
    if stack_create_status == "Stack CREATE completed successfully":
        key = key_loc + key + '.pem'
        if validate_ip_vnf_multinw(stack_name, username, key, password):
            print "server ip validation pass"
            return True
        else:
            return False
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_multi_network_test(stack_name, yaml_path, yaml_name, mngt_nw, network_id, image, flavor, key, key_loc, username, password):
    if not create_stack(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, network_id):
        return False
    time.sleep(80)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status
    if stack_create_status == "Stack CREATE completed successfully":
        key = key_loc + key + '.pem'
        if validate_ip_vnf_multinw(stack_name, username, key, password):
            print "server ip validation pass"
            return True
        else:
            return False
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_multi_network_multi_server_test(stack_name, yaml_path, yaml_name, mngt_nw, network_id, image, flavor, key, key_loc, username, password):
    if not create_stack(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, network_id):
        return False
    print "Sleep for 60 sec"
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status
    if stack_create_status == "Stack CREATE completed successfully":
        key = key_loc + key + '.pem'
        if validate_ip_vnf_multistack(stack_name, username, key, password):
            print "server ip validation pass"
            return True
        else:
            return False
    else:
        print "stack_create_status is:", stack_create_status
        return False

def multi_network_multi_server_icmp_test(stack_name, username, key_loc, key, password):
    print "stack_name : %s " %stack_name
    print "Sleep for 5 sec"
    time.sleep(5)

    key = key_loc + key + '.pem'

    print "multi_network_multi_server_icmp_test key: ", key

    login_ip = get_ip_vnf_multistack(stack_name, username, key, password)

    if login_ip:
        result = test_icmp_traffic(login_ip[0], login_ip[1], username, key, password)
    else:
        print "Getting floating IP address FAILED"
        return False

    return result

def multi_network_multi_server_iperf3_traffic_test(stack_name, username, key_loc, key, password):
    print "stack_name : %s " %stack_name
    time.sleep(5)

    key = key_loc + key + '.pem'

    login_ip = get_ip_vnf_multistack(stack_name, username, key, password)

    result = test_iperf3_traffic(login_ip[0], login_ip[1])

    return result

def upgrade_stack_test(stack_name, yaml_path, new_yaml, image = None, flavor = None):
    if not upgrade_stack(stack_name, yaml_path, new_yaml, image, flavor):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    return True if stack_create_status == "Stack UPDATE completed successfully" else False

def downgrade_stack_test(stack_name, yaml_path, new_yaml, image = None, flavor = None):
    if not downgrade_stack(stack_name, yaml_path, new_yaml, image, flavor):
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

def soft_reboot_stack_multi_network_test(stack_name, username, key_loc, key, password):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = reboot_server(server_name, 'soft')
    key = key_loc + key + '.pem'

    if retVal != "Complete\n":
        print "server soft reboot failed", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    print "stack_create_status", stack_create_status
    if validate_ip_vnf_multistack(stack_name, username, key, password):
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
    if stack_create_status == "active":
        return True
    else:
        return False

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

def create_image(image_name, image_file):
    exec_sys_command("openstack image list")
    status = True
    cmd = "openstack image create --disk-format=qcow2  --file=%s %s " % (image_file, image_name)
    logging.info("command: %s" % cmd)
    out = exec_sys_command(cmd)
    if out.find(image_name) != -1:
        logging.info("Image - %s -- successfully created" %image_name)
    else:
        status = False
    return status

def delete_image(image_name):
    status = True
    cmd = "openstack image delete " + image_name
    print "Openstack command: ", cmd
    out = exec_sys_command(cmd)
    if not out:
        print "Image - " + image_name + " -- successfully deleted"
    else:
        status = False
    return status

def create_image_test(image_name, image_file):
    exec_sys_command("openstack image list")
    if not create_image(image_name, image_file):
        return False
    time.sleep(10)
    return True

def delete_image_test(image_name):
    if not delete_image(image_name):
        return False
    time.sleep(10)
    return True

def create_network(network_name, subnet):
    status = True
    cmd1 = "openstack network create --share --enable " + network_name
    cmd2 = "openstack subnet create " + network_name + " --network " + network_name + " --subnet-range " + subnet
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
    if not out:
        print "network - " + network_name + " -- successfully deleted"
    else:
        status = False
    return status

def create_network_test(network_name, subnet):
    if not create_network(network_name, subnet):
        return False
    time.sleep(30)
    return True

def delete_network_test(network_name):
    if not delete_network(network_name):
        return False
    time.sleep(30)
    return True

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

def validate_ip_vnf_multinw(multi_nw_name, usrname, key, password):
    ip_float = get_float_ip(multi_nw_name)
    if ip_float:
        print "key: ", key
        k = paramiko.RSAKey.from_private_key_file(key)
        H = paramiko.SSHClient()
        H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for n in range(20):
            try:
                if key:
                    H.connect(hostname = ip_float, username = usrname, pkey = k)
                else:
                    H.connect(hostname = ip_float, username = usrname, password=password)
                print "SSH Connection Successful"
                return True
            except:
                print "SSH Connection Failed"
                print "Sleep for 20 seconds"
                time.sleep(20)
                if n <= 20:
                    continue
                else:
                    print "IP verification Failed"
                    return False
 
def validate_ip_vnf_multistack(multi_stack_name, usrname, key, password):
    login_ip = []
    print "Sleep for 30 sec"
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

    exact_server_name = [exact_server_name1, exact_server_name2]
    print "Login IP: %s" %login_ip
    print "Sleep for 60 sec"
    time.sleep(60)

    k = paramiko.RSAKey.from_private_key_file(key)
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    for idx, server_name in enumerate(exact_server_name):
        ip_float = login_ip[idx]
        print "IP Float: %s " % ip_float
        for n in range(20):
            try:
                try:
                    H.connect(hostname = ip_float, username = usrname, password=password)
                except:
                    H.connect(hostname = ip_float, username = usrname, pkey = k)
                print "SSH Connection Successful for ", ip_float
                break
            except:
                print "SSH Connection Failed"
                print "Sleep for 20 seconds"
                time.sleep(20)
                if n <= 20:
                    continue
                else:
                    print "IP verification Failed"
                    return False
    return login_ip

def get_ip_vnf_multistack(multi_stack_name, usrname, key, password):
    login_ip = []
    print "Sleep for 30 sec"
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

    exact_server_name = [exact_server_name1, exact_server_name2]
    print "Login IP: %s" %login_ip

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

def test_icmp_traffic(login_ip1, login_ip3, usrname, key, password):
    status = True
    print "test_icmp_traffic key: ", key
    try:
        c1 = SSHConnection(IP=login_ip1, username=usrname, password=password)
        c3 = SSHConnection(IP=login_ip3, username=usrname, password=password)
    except:
        c1 = SSHConnection(IP=login_ip1, username=usrname, ssh_key=key)
        c3 = SSHConnection(IP=login_ip3, username=usrname, ssh_key=key)
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

def multi_network_multi_server_http_traffic_test(stack_name, username, key_loc, key, password):
    print "stack_name : %s " %stack_name
    time.sleep(5)

    key = key_loc + key + '.pem'

    login_ip = get_ip_vnf_multistack(stack_name, username, key, password)

    result = test_http_traffic(login_ip[0], login_ip[1], username, key, password)

    return result

def test_http_traffic(login_ip1, login_ip3, usrname, key, password):
    status = True
    try:
        c1 = SSHConnection(IP=login_ip1, username=usrname, password=password)
        c3 = SSHConnection(IP=login_ip3, username=usrname, password=password)
    except:
        c1 = SSHConnection(IP=login_ip1, username=usrname, ssh_key=key)
        c3 = SSHConnection(IP=login_ip3, username=usrname, ssh_key=key)

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
            print "Verification of traffic test before disabling http -- Failed."
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


#set_environment("demo-openrc")
def test_complete():
    pass




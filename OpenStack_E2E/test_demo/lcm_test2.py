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
from subprocess import call
from netmiko.ssh_exception import NetMikoTimeoutException
import re
import os.path
import sys
from orch_lib2 import *
#import iptc
import telnetlib
from scp import SCPClient
import socket

def set_environment(env_file):
    out = subprocess.Popen(". %s; env" % env_file, stdout=subprocess.PIPE, shell=True)
    output = out.communicate()[0]
    environment_var = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(environment_var)
    time.sleep(5)

def system_pre_check_test():
    status = True
    cmd1 = "df -h / | awk 'END {print}'| awk '{print $4}'"
    output1 = exec_sys_command(cmd1)
    print "Size of Hard disk: ", output1
    if int(output1.split('G')[0]) > 200:
        print "Hard disk check PASSED"
    else:
        print "Hard disk check FAILED"
        return False

    cmd2 = "free -g Mem | awk 'NR==2 {print}'|awk '{print $2}'"
    output2 = exec_sys_command(cmd2)
    print "Size of RAM: ", output2
    if int(output2) > 8:
        print "RAM Size check PASSED"
    else:
        print "RAM Size check FAILED"
        return False

    cmd3 = "cat /proc/cpuinfo | grep processor | wc -l"
    output3 = exec_sys_command(cmd3)
    print "Number of Processor Available: ", output3
    if int(output3) >= 4 :
        print "Number of Processor Available check PASSED"
    else:
        print "Number of Processor Available check FAILED"
        return False
    return status

def create_local(password):
    loc_content = """[[local|localrc]]
    HOST_IP=192.168.203.6
    SERVICE_HOST=$HOST_IP
    MYSQL_HOST=$HOST_IP
    RABBIT_HOST=$HOST_IP
    GLANCE_HOSTPORT=$HOST_IP:9292
    ADMIN_PASSWORD=%s
    DATABASE_PASSWORD=$ADMIN_PASSWORD
    RABBIT_PASSWORD=$ADMIN_PASSWORD
    SERVICE_PASSWORD=$ADMIN_PASSWORD
    NOVNC_BRANCH=v0.6.0

    ## Neutron options
    Q_USE_SECGROUP=True
    FLOATING_RANGE="192.168.203.0/26"
    IPV4_ADDRS_SAFE_TO_USE="10.0.0.0/22"
    Q_FLOATING_ALLOCATION_POOL=start=192.168.203.35,end=192.168.203.42
    PUBLIC_NETWORK_GATEWAY="192.168.203.1"
    PUBLIC_INTERFACE=eno1

    # Open vSwitch provider networking configuration
    Q_USE_PROVIDERNET_FOR_PUBLIC=True
    OVS_PHYSICAL_BRIDGE=br-ex
    PUBLIC_BRIDGE=br-ex
    OVS_BRIDGE_MAPPINGS=public:br-ex

    enable_service h-eng h-api h-api-cfn h-api-cw
    enable_plugin heat https://git.openstack.org/openstack/heat stable/ocata   """ %password

    try:
        exec_sys_command("sudo chown -R stack:stack /opt/stack")
        logging.info("Create local.conf")
        file_new = open(r"/opt/stack/local.conf", "w+")
        file_new.write(loc_content)
        file_new.close()
        logging.info("local.conf is CREATED")
        exec_sys_command("sudo chmod -R 777 /opt/stack")
        return True
    except:
        print "local.conf is FAILED to Create"
        return False

def clone_stable_image(version):
    status = True
    try:
        logging.info("Clone Openstack version %s" %version)
        cmd = "git clone https://git.openstack.org/openstack-dev/devstack -b stable/%s" %version
        exec_sys_command(cmd, cwd="/opt/stack/")
        exec_sys_command("sudo chown -R stack:stack /opt/stack")
        exec_sys_command("sudo chown -R stack:stack /opt/stack/*/*")
        time.sleep(60)
        logging.info("Clone Openstack version %s is COMPLETED" %version)
        exec_sys_command("sudo chmod -R 777 /opt/stack")
        exec_sys_command("sudo chmod 777 /opt/stack/*.*")
    except:
        logging.info("Clone Openstack version %s is FAILED" %version)
        return False

    if os.path.isfile("/opt/stack/devstack/stack.sh"):
        print "Stack.sh file is available to Install"
    else:
        print "Stack.sh file is NOT Available. Clone Openstack version %s is FAILED" %version
        sys.exit()
    return status

def install_openstack(IP, username, password):
    try:
        logging.info("Install Openstack")
        #exec_sys_command("cp /opt/stack/local.conf /opt/stack/devstack/")
        exec_sys_command("cp /home/testpc/local.conf /opt/stack/devstack/")
        exec_sys_command("sudo chown -R stack:stack /opt/stack")
        exec_sys_command("sudo chown -R stack:stack /opt/stack/*/*")
        subprocess.call(["nohup", "/opt/stack/devstack/stack.sh"])
        logging.info("Install Openstack COMPLETED")
        return True
    except:
        print "Openstack installation Failed"
        return False

def uninstall_openstack(IP, username, password):
    try:
        subprocess.call(["nohup", "/opt/stack/devstack/unstack.sh"])
        subprocess.call(["nohup", "/opt/stack/devstack/clean.sh"])
        print ("Openstack Uninstall is IN PROGRESS. Sleep 30 Sec.")
        exec_sys_command("rm -rf /opt/stack/*")
        return True
    except:
        print "Openstack uninstallation Failed"
        return False

def verify_heat_services_test():
    if not verify_dev_services('heat'):
        return False
    time.sleep(5)
    return True

def verify_nova_services_test():
    if not verify_dev_services('nova'):
        return False
    time.sleep(5)
    return True

def verify_nova_legacy_services_test():
    if not verify_dev_services('nova_legacy'):
        return False
    time.sleep(5)
    return True

def verify_cinder_services_test():
    if not verify_dev_services('cinder'):
        return False
    time.sleep(5)
    return True

def verify_glance_services_test():
    if not verify_dev_services('glance'):
        return False
    time.sleep(5)
    return True

def verify_neutron_services_test():
    if not verify_dev_services('neutron'):
        return False
    time.sleep(5)
    return True

def verify_cinderv3_services_test():
    if not verify_dev_services('cinderv3'):
        return False
    time.sleep(5)
    return True

def verify_cinderv2_services_test():
    if not verify_dev_services('cinderv2'):
        return False
    time.sleep(5)
    return True

def verify_placement_services_test():
    if not verify_dev_services('placement'):
        return False
    time.sleep(5)
    return True

def verify_keystone_services_test():
    status = True
    service_name = 'keystone'
    sh_cmd = "openstack service list"
    output0 = exec_sys_command(sh_cmd)
    if output0.find(service_name) != -1:
        print "Openstack service %s exists" %service_name
        cmd1 = "openstack service show %s" %service_name
        print "cmd1: ", cmd1
        new_cmd = cmd1 + " | awk 'NR==4 {print}' | awk '{print $4}'"
        out1 = exec_sys_command(new_cmd)
        if out1 == 'True\n':
            print "Openstack service %s is ACTIVE" %service_name
        else:
            print "Openstack service %s is NOT ACTIVE" %service_name
            return False
    else:
        print "openstack service %s doesn't exist" %service_name
        return False
    return status

def manage_existing_router_and_network():
    status = True
    sh_nw_cmd = "openstack network list"
    print sh_nw_cmd
    out = exec_sys_command(sh_nw_cmd)
    print out
    sh_rtr_cmd = "openstack router list"
    print sh_rtr_cmd
    out2 = exec_sys_command(sh_rtr_cmd)
    print out2

    cmd1 = "openstack router set --disable router1"
    exec_sys_command(cmd1)

    cmd4 = "openstack router remove subnet router1 ipv6-private-subnet"
    exec_sys_command(cmd4)
    cmd5 = "openstack router remove subnet router1 private-subnet"
    exec_sys_command(cmd5)
    cmd7 = "openstack network delete private"
    exec_sys_command(cmd7)

    cmd2 = "openstack router remove subnet router1 ipv6-public-subnet"
    exec_sys_command(cmd2)
    cmd3 = "openstack router remove subnet router1 public-subnet"
    exec_sys_command(cmd3)
    cmd6 = "openstack network delete public"
    exec_sys_command(cmd6)

    cmd8 = "openstack router delete router1"
    exec_sys_command(cmd8)


    sh_nw_cmd = "openstack network list"
    print sh_nw_cmd
    out = exec_sys_command(sh_nw_cmd)
    print out
    sh_rtr_cmd = "openstack router list"
    print sh_rtr_cmd
    out2 = exec_sys_command(sh_rtr_cmd)
    print out2

    cmd1 = "openstack router set --disable router1"
    exec_sys_command(cmd1)

    cmd4 = "openstack router remove subnet router1 ipv6-private-subnet"
    exec_sys_command(cmd4)
    cmd5 = "openstack router remove subnet router1 private-subnet"
    exec_sys_command(cmd5)
    cmd7 = "openstack network delete private"
    exec_sys_command(cmd7)

    cmd2 = "openstack router remove subnet router1 ipv6-public-subnet"
    exec_sys_command(cmd2)
    cmd3 = "openstack router remove subnet router1 public-subnet"
    exec_sys_command(cmd3)
    cmd6 = "openstack network delete public"
    exec_sys_command(cmd6)

    cmd8 = "openstack router delete router1"
    exec_sys_command(cmd8)
    cmd6 = "openstack network delete public"
    exec_sys_command(cmd6)
    cmd7 = "openstack network delete private"
    exec_sys_command(cmd7)

    try:
        sh_cmd1 = "openstack network list --name public"
        print sh_cmd1
        output0 = exec_sys_command(sh_cmd1)
        if output0.find('public') != -1:
            print "Existing Public Network couldn't be deleted"
            return False
        else:
            print "Existing Public Network is Deleted"

        sh_cmd2 = "openstack network list --name private"
        print sh_cmd2
        output0 = exec_sys_command(sh_cmd2)
        if output0.find('private') != -1:
            print "Existing Private Network couldn't be deleted"
            return False
        else:
            print "Existing Private Network is Deleted"

        sh_cmd3 = "openstack router list --name router1"
        print sh_cmd3
        output0 = exec_sys_command(sh_cmd3)
        if output0.find('router1') != -1:
            print "Existing Router couldn't be deleted"
            return False
        else:
            print "Existing Router is Deleted"
        return status
    except:
        print "One or more Openstack services are NOT ACTIVE"
        return False

def create_public_network_test(network_name, subnet, ip_alloc_pool_start, ip_alloc_pool_end):
    if not create_public_network(network_name, subnet, ip_alloc_pool_start, ip_alloc_pool_end):
        return False
    time.sleep(30)
    return True

def delete_router_test(router_name):
    if not delete_router(router_name):
        return False
    time.sleep(30)
    return True

def create_router_test(router_name, public_net_name, mgmt_nw):
    if not create_router(router_name, public_net_name, mgmt_nw):
        return False
    time.sleep(30)
    return True

def create_security_group_test(sec_name):
    if not create_sec_grp(sec_name):
        return False
    time.sleep(30)
    return True

def delete_security_group_test(sec_name):
    if not delete_sec_grp(sec_name):
        return False
    time.sleep(30)
    return True

def create_stack_test(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, key_loc, username, password, sec_name):
    if not create_stack(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, sec_name):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status

    if stack_create_status == "Stack CREATE completed successfully":
        key = key_loc + key + '.pem'
        return validate_ip_vm_multinw(stack_name, username, key, password)
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_with_snapshot_test(stack_name, yaml_path, yaml_name, mngt_nw, network_id, image, flavor, key, key_loc, username, password, sec_name):
    if not create_stack(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, sec_name, network_id):
        return False
    time.sleep(80)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status
    if stack_create_status == "Stack CREATE completed successfully":
        key = key_loc + key + '.pem'
        if validate_ip_vm_multinw(stack_name, username, key, password):
            print "server ip validation pass"
            return True
        else:
            return False
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_multi_network_test(stack_name, yaml_path, yaml_name, mngt_nw, network_id, image, flavor, key, key_loc, username, password, sec_name):
    if not create_stack(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, sec_name, network_id):
        return False
    time.sleep(80)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status
    if stack_create_status == "Stack CREATE completed successfully":
        key = key_loc + key + '.pem'
        if validate_ip_vm_multinw(stack_name, username, key, password):
            print "server ip validation pass"
            return True
        else:
            return False
    else:
        print "stack_create_status is:", stack_create_status
        return False

def create_stack_multi_network_multi_server_test(stack_name, yaml_path, yaml_name, mngt_nw, network_id, image, flavor, key, key_loc, username, password, sec_name):
    if not create_stack(stack_name, yaml_path, yaml_name, mngt_nw, image, flavor, key, sec_name, network_id):
        return False
    print "Sleep for 60 sec"
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status
    if stack_create_status == "Stack CREATE completed successfully":
        key = key_loc + key + '.pem'
        if validate_ip_vm_multistack(stack_name, username, key, password):
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

    login_ip = get_ip_vm_multistack(stack_name, username, key, password)

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

    login_ip = get_ip_vm_multistack(stack_name, username, key, password)

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
    if validate_ip_vm_multistack(stack_name, username, key, password):
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

def create_keypairs_test(key_name):
    exec_sys_command("openstack keypair list")
    if not create_keypairs(key_name):
        return False
    time.sleep(10)
    return True

def delete_keypairs_test(key_name):
    if not delete_keypairs(key_name):
        return False
    time.sleep(10)
    return True

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

    login_ip = get_ip_vm_multistack(stack_name, username, key, password)

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
    # k = paramiko.RSAKey.from_private_key_file("/home/testpc/automation/rmaity/test_demo/loginkey.pem")
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

def add_allowed_add_pair(port_list):
    for port in port_list:
        ost_cmd = "openstack port list | grep %s" % port
        #print "Command1: %s" % ost_cmd
        output = exec_sys_command(ost_cmd)
        try:
            id = output.split('|')[1].split(' ')[1]
            ost_cmd1 = "openstack port set --allowed-address ip-address=0.0.0.0/0 %s" % id
            #print "Command2: %s" % ost_cmd1
            output = exec_sys_command(ost_cmd1)
        except:
            print "Please check port creation. No private IP found"
            return False
    return True

def ospf_functional(stack_name, yaml_path, yaml_name, key, key_loc, sec_name):
    usrname = 'ubuntu'
    password = 'ubuntu'
    key = key_loc + key + '.pem'
    print "key %s" % key
     
    if not create_stack_functional(stack_name, yaml_path, yaml_name, sec_name):
        return False
    print "Sleep for 60 sec"
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    print "stack_create_status: ", stack_create_status

    logging.info("sleep for sometime before the devices comes up")
    logging.info("start")
    time.sleep(60)
    logging.info("sleep")
    
    float_ip, net_mngt, pvt_ip = get_multi_ip_functional(stack_name)
    print "Floating IPs: Server1 - %s, Server2 - %s, Server3 - %s, Server4 - %s" % (float_ip[0], float_ip[1], float_ip[2], float_ip[3])
    print "net_mngt %s: " % net_mngt
    print "pvt_ip %s: " % pvt_ip

    ip_s1 = float_ip[0]
    ip_s2 = float_ip[1]
    ip_s3 = float_ip[2]
    ip_s4 = float_ip[3]

    logging.info("\nAdd allowed address pair for each private interfaces\n")
    sp1=add_allowed_add_pair(pvt_ip)
    try :
      assert sp1 == 1,"Add allowed address pair for one or more private interfaces FAILED"
    except AssertionError as error:
      print(error)
    
    ping_test(ip_s1)
    ping_test(ip_s2)
    ping_test(ip_s3)
    ping_test(ip_s4)
   
    #### delete_iptables proc is not working for imort issue
    ''' 
    logging.info("Delete DROP rules from iptables")
    #for ip in ('20.1.1.10','20.1.1.8','10.10.1.12','40.1.1.14','10.10.1.9','40.1.1.10'):
    for idx, ip in enumerate(pvt_ip):
        delete_iptables(ip)
    '''
    
    logging.info("\nTaking host R1 and configuring quagga\n")
    i=1
    while(i<=50):
      try:
         sp1=connect_host_configure_quagga(ip_s2, net_mngt[1], "/zebra1.conf", "/ospfd1.conf")
         if sp1==0:
           return sp1
         else:
           break
      except Exception as e:
            i+=1
            print(e)
            print ("ssh timeout. Try %s times untill it is connected"%(10-i))
            time.sleep(10)

    logging.info("\nTaking host R2 and configuring quagga\n")
    i=1
    while(i<=50):
      try:
        sp2=connect_host_configure_quagga(ip_s3, net_mngt[2], "/zebra2.conf", "/ospfd2.conf")
        if sp2==0:
          return sp2
        else:
          break
      except Exception as e:
            i+=1
            print ("ssh timeout. Try %s times untill it is connected"%(10-i))
            time.sleep(10)
        
    logging.info("\nTaking host R1 and configuring interfaces\n")
    sp1=connect_configure_interface(ip_s2, 2601, pvt_ip[1], pvt_ip[2])
    try :
      assert sp1 == 1,"Configuring host R1 interface failed"
    except AssertionError as error:
      print(error)

    logging.info("\nTaking host R2 and configuring interfaces\n")
    sp2=connect_configure_interface(ip_s3, 2601, pvt_ip[3], pvt_ip[4])
    try :
      assert sp2 == 1,"Configuring host R2 interface failed"
    except AssertionError as error:
      print(error)

    logging.info("\nTaking host H1 and configuring interfaces\n")
    sp3=connect_configure_1interface(ip_s1, pvt_ip[0], pvt_ip[1], 1)
    try :
      assert sp3 == 1,"Configuring host H1 interface failed"
    except AssertionError as error:
      print(error)

    logging.info("\nTaking host H2 and configuring interfaces\n")
    sp4=connect_configure_1interface(ip_s4, pvt_ip[5], pvt_ip[4], 2)
    try :
      assert sp4 == 1,"Configuring host H2 interface failed"
    except AssertionError as error:
      print(error)

    logging.info("\nTaking host R1 and configuring ospf\n")
    connect_configure_ospf(ip_s2, 2604, 1)

    logging.info("\nTaking host R2 and configuring ospf\n")
    connect_configure_ospf(ip_s3, 2604, 2)
      
    logging.info("\nSleeping 60 seconds for ospf to come up\n")
    time.sleep(60)
    
    logging.info("\nCheck ospf status on R1 and R2\n")
    sp = connect_verify_ospf(ip_s2, ip_s3)
    try :
      assert sp == 1,"OSPF verification failed"
    except AssertionError as error:
      print(error)

    #PING
    logging.info("\nTESTCASE 1 : Ping Testcase\n")
    logging.info("\nVerify ping from H1->H2\n")
    tc1_sp1=connect_host_verify_ping(ip_s1, pvt_ip[5])
    try :
      assert tc1_sp1 == 1,"ping from H1->H2 failed"
    except AssertionError as error:
      print(error)

    logging.info("\nVerify ping from H2->H1\n")
    tc1_sp2=connect_host_verify_ping(ip_s4, pvt_ip[0])
    try :
      assert tc1_sp2 == 1,"ping from H2->H1 failed"
    except AssertionError as error:
      print(error)

    #IPERF
    logging.info("\nTESTCASE 2 : Traffic Testcase\n")

    logging.info("\nConnect Host1 and Configure Iperf3\n")
    tc1_sp1=connect_host_configure_iperf3(ip_s1)
    try :
      assert tc1_sp1 == 1,"Iperf3 Configuration in Host1 FAILED"
    except AssertionError as error:
      print(error)

    logging.info("\nConnect Host2 and Configure Iperf3\n")
    tc1_sp2=connect_host_configure_iperf3(ip_s4)
    try :
      assert tc1_sp2 == 1,"Iperf3 Configuration in Host2 FAILED"
    except AssertionError as error:
      print(error)

    logging.info("\nH1 is client and H2 is server\n")
    connect_host_verify_with_iperf3(ip_s4, pvt_ip[5], "server")
    tc2_sp1=connect_host_verify_with_iperf3(ip_s1, pvt_ip[5], "client")
    try :
      assert tc2_sp1 == 1,"Traffic from H1->H2 failed"
    except AssertionError as error:
      print(error)

    logging.info("\nH2 is client and H1 is server\n")
    connect_host_verify_with_iperf3(ip_s1, pvt_ip[0], "server")
    tc2_sp2=connect_host_verify_with_iperf3(ip_s4, pvt_ip[0], "client")
    try :
      assert tc2_sp2 == 1,"Traffic from H2->H1 failed"
    except AssertionError as error:
      print(error)

    logging.info("\nTESTCASE 3 : Continuous traffic Testcase\n")
    logging.info("\nH1 is client and H2 is server\n")
    connect_host_verify_with_iperf3(ip_s4, pvt_ip[5],"server")
    tc3_sp1=connect_host_verify_with_iperf3(ip_s1, pvt_ip[5],"client",'continuous')
    try :
      assert tc3_sp1 == 1,"Traffic from H1->H2 failed"
    except AssertionError as error:
      print(error)

    logging.info("\nH2 is client and H1 is server\n")
    connect_host_verify_with_iperf3(ip_s1, pvt_ip[0],"server")
    tc3_sp2=connect_host_verify_with_iperf3(ip_s4, pvt_ip[0],"client",'continuous')
    try :
      assert tc3_sp2 == 1,"Traffic from H2->H1 failed"
    except AssertionError as error:
      print(error)
    logging.info("\nProceeding to cleanup\n")
    return 1

def ospf_functional_test(stack_name, yaml_path, yaml_name, key, key_loc, sec_name):
    if not ospf_functional(stack_name, yaml_path, yaml_name, key, key_loc, sec_name):
        return False
    time.sleep(10)
    return True

def ping_test(host):
    i=1
    while(i<=50):
       ping_out=os.popen("ping %s -c 5" % host).read()
       check=re.search(r'(\d+)%\s+packet loss', ping_out, re.I|re.S)
       if int(check.group(1)) == 0:
           print ("Device is reachable now connect to the device")
           break
       else:
            i+=1
            print ("Device is not reachable..sleep for sometime")
            time.sleep(10)
            continue

def connect_host_configure_iperf3(host):
    k = paramiko.RSAKey.from_private_key_file("/home/testpc/automation/rmaity/test_demo/loginkey.pem")
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("connecting to %s"%host)
    H.connect( hostname = host, username = "ubuntu", pkey = k )
    logging.info("connected to %s"%host)
    logging.info("Configuring iperf3 in the given host %s"% host)
    stdin , stdout, stderr = H.exec_command("sudo apt install iperf3")
    op=stdout.read()
    logging.info("%s"%op)

def connect_host_configure_quagga(host,re_ip,fil_name1,fil_name2):
    k = paramiko.RSAKey.from_private_key_file("/home/testpc/automation/rmaity/test_demo/loginkey.pem")
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("connecting to %s"%host)
    H.connect( hostname = host, username = "ubuntu", pkey = k )
    logging.info("connected to %s"%host)
    logging.info("Configuring quagga in the given host %s"% host)
    stdin , stdout, stderr = H.exec_command("sudo apt-get update")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo lsof /var/lib/dpkg/lock")
    op=stdout.read()
    logging.info("%s"%op)
    m=re.search(r'(\d+)\s+root', op, re.I|re.S)
    if m:
        logging.error("remove the lock")
        prod_id=m.group(1)
        prod_id=int(prod_id)
        stdin , stdout, stderr = H.exec_command("sudo kill -9 %s" % prod_id)
        op=stdout.read()
        logging.info("%s"%op)
    else:
        logging.info("lock is not there")
    stdin , stdout, stderr = H.exec_command("sudo apt-get install quagga quagga-doc traceroute")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo cp /usr/share/doc/quagga/examples/zebra.conf.sample /etc/quagga/zebra.conf")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo cp /usr/share/doc/quagga/examples/ospfd.conf.sample /etc/quagga/ospfd.conf")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo chown quagga.quaggavty /etc/quagga/*.conf")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo chmod 777 /etc/quagga/*.conf")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo sed -i s'/zebra=no/zebra=yes/' /etc/quagga/daemons")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo sed -i s'/ospfd=no/ospfd=yes/' /etc/quagga/daemons")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo sed -i s'/127.0.0.1/%s/' /etc/quagga/debian.conf" % re_ip)
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo chmod 777 /etc/quagga")
    op=stdout.read()
    logging.info("%s"%op)
    scp = SCPClient(H.get_transport())
    scp.put('%s' % fil_name1,'/etc/quagga/ospfd.conf')
    scp.put('%s' % fil_name2,'/etc/quagga/zebra.conf')
    scp.close()
    stdin , stdout, stderr = H.exec_command("sudo /etc/init.d/quagga restart")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo service quagga status")
    op=stdout.read()
    logging.info("%s"%op)
    check1=re.search(r'/usr/lib/quagga/zebra.*?%s' % re_ip, op, re.I|re.S)
    check2=re.search(r'/usr/lib/quagga/ospfd.*?%s' % re_ip, op, re.I|re.S)
    if check1 and check2:
      logging.info("Quagga router started successfully in host %s" % re_ip)
      return 1
    else :
      logging.info("Quagga router failed to start in host %s" % re_ip)
      return 0

def connect_host_configure_openvpn(host,re_ip,fil_name1,fil_name2,log_file):
    k = paramiko.RSAKey.from_private_key_file("/home/testpc/automation/rmaity/test_demo/loginkey.pem")
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("connecting to %s"%host)
    #H.connect( hostname = host, username = "ubuntu", password = "ubuntu" )
    H.connect( hostname = host, username = "ubuntu", pkey = k )
    logging.info("connected to %s"%host)
    logging.info("Configuring quagga in the given host %s"% host)
    stdin , stdout, stderr = H.exec_command("sudo apt-get update")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo lsof /var/lib/dpkg/lock")
    op=stdout.read()
    logging.info("%s"%op)
    m=re.search(r'(\d+)\s+root', op, re.I|re.S)
    if m:
        logging.error("remove the lock")
        prod_id=m.group(1)
        prod_id=int(prod_id)
        stdin , stdout, stderr = H.exec_command("sudo kill -9 %s" % prod_id)
        op=stdout.read()
        logging.info("%s"%op)
    else:
        logging.info("lock is not there")
    if 'server' in fil_name1:
      stdin , stdout, stderr = H.exec_command("sudo route add -net 10.10.1.0/24 gw 20.1.1.8")
      op=stdout.read()
      logging.info("%s"%op)
      stdin , stdout, stderr = H.exec_command("sudo route add -net 40.1.1.0/24 gw 20.1.1.8")
      op=stdout.read()
      logging.info("%s"%op)
    else:
      stdin , stdout, stderr = H.exec_command("sudo route add -net 20.1.1.0/24 gw 40.1.1.10")
      op=stdout.read()
      logging.info("%s"%op)
      stdin , stdout, stderr = H.exec_command("sudo route add -net 10.10.1.0/24 gw 40.1.1.10")
      op=stdout.read()
      logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo apt-get install -y openvpn")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo chmod 777 /etc/openvpn")
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo chmod 777 /var/log")
    op=stdout.read()
    logging.info("%s"%op)
    new_name=fil_name1.strip('/')
    stdin , stdout, stderr = H.exec_command("touch /etc/openvpn/%s" % new_name)
    op=stdout.read()
    time.sleep(10)
    scp = SCPClient(H.get_transport())
    scp.put('%s' % fil_name1,'/etc/openvpn/%s' % new_name)
    scp.put('%s' % fil_name2,'/home/ubuntu/')
    scp.close()
    stdin , stdout, stderr = H.exec_command("sudo openvpn /etc/openvpn/%s >> /var/log/%s" % (new_name,log_file))

def verify_openvpn(host,re_ip,fil_name1,log_file):
    k = paramiko.RSAKey.from_private_key_file("/home/testpc/automation/rmaity/test_demo/loginkey.pem")
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("connecting to %s"%host)
    #H.connect( hostname = host, username = "ubuntu", password = "ubuntu" )
    H.connect( hostname = host, username = "ubuntu", pkey = k )
    logging.info("connected to %s"%host)
    logging.info("Configuring quagga in the given host %s"% host)
    stdin , stdout, stderr = H.exec_command("ps -ef | grep vpn")
    op=stdout.read()
    logging.info("%s"%op)
    check1=re.search(r'sudo openvpn /etc/openvpn/%s' % fil_name1, op, re.I|re.S)
    if check1:
      logging.info("openvpn started successfully in host %s" % re_ip)
      logging.info("Now check the %s" % log_file)
      stdin , stdout, stderr = H.exec_command("cat /var/log/%s" % log_file)
      op=stdout.read()
      logging.info("%s"%op)
      check = re.search(r'Initialization Sequence Completed', op, re.I|re.S)
      if check:
        logging.info("openvpn initialization completed successfully in host %s" % re_ip)
        return 1
      else :
        logging.info("openvpn initialization failed in host %s" % re_ip)
        return 0
    else :
      logging.info("openvpn failed to start in host %s" % re_ip)
      logging.info("Now check the %s" % log_file)
      stdin , stdout, stderr = H.exec_command("cat /var/log/%s" % log_file)
      op=stdout.read()
      return 0

def connect_configure_interface(host,port,ip1,ip2):
    telnet=telnetlib.Telnet()
    telnet.open("%s" % host,"%s" % port)
    out = telnet.read_until(">", 5)
    logging.info("%s"%out)
    telnet.write("en\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("configure terminal\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("ip forwarding\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("interface ens4\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("ip address %s/24\n" % ip1)
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("no shut\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("interface ens5\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("ip address %s/24\n" % ip2)
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("no shut\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("end\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("show interface ens4\n")
    out1 = telnet.read_until("#", 5)
    logging.info("%s"%out1)
    telnet.write("show interface ens5\n")
    out2 = telnet.read_until("#", 5)
    logging.info("%s"%out2)
    check1=re.search(r'ens4 is up.*%s' % ip1, out1, re.I|re.S)
    check2=re.search(r'ens5 is up.*%s' % ip2, out2, re.I|re.S)
    if check1 and check2 :
      logging.info("interfaces configured successfully in host %s" % host)
      telnet.close()
      return 1
    else :
      logging.info("failed to confiugre interfaces in host %s" % host)
      telnet.close()
      return 0

def connect_configure_1interface(host, ip1, ip2, idx):
    k = paramiko.RSAKey.from_private_key_file("/home/testpc/automation/rmaity/test_demo/loginkey.pem")
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("connecting to %s"%host)
    H.connect( hostname = host, username = "ubuntu", pkey = k )
    logging.info("connected to %s"%host)
    logging.info("Configuring interafce in the given host %s"% host)
    stdin , stdout, stderr = H.exec_command("sudo ifconfig ens4 %s netmask 255.255.255.0 up" % ip1)
    op=stdout.read()
    logging.info("%s"%op)
    stdin , stdout, stderr = H.exec_command("sudo ifconfig ens4")
    op1=stdout.read()
    logging.info("%s"%op1)
    if idx == 1:
        stdin , stdout, stderr = H.exec_command("sudo route add -net 10.10.1.0/24 gw %s" %ip2)
        op2=stdout.read()
        logging.info("%s"%op2)
        stdin , stdout, stderr = H.exec_command("sudo route add -net 40.1.1.0/24 gw %s" %ip2)
        op3=stdout.read()
        logging.info("%s"%op3)
        print "**************"
    else:
        stdin , stdout, stderr = H.exec_command("sudo route add -net 10.10.1.0/24 gw %s" %ip2)
        op2=stdout.read()
        logging.info("%s"%op2)
        stdin , stdout, stderr = H.exec_command("sudo route add -net 20.1.1.0/24 gw %s" %ip2)
        op3=stdout.read()
        logging.info("%s"%op3)

def connect_configure_bgp(host,port):
    telnet=telnetlib.Telnet()
    telnet.open("%s" % host,"%s" % port)
    out = telnet.read_until(">", 5)
    logging.info("%s"%out)
    telnet.write("en\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("configure terminal\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    if '22' in host:
     telnet.write("router bgp 1\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)
     telnet.write("bgp router-id 1.1.1.1\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)
     telnet.write("neighbor 10.10.1.9 remote-as 2\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)
     telnet.write("address-family ipv4 unicast\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)
     telnet.write("network 20.1.1.0/24\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)        
    if '24' in host:
     telnet.write("router bgp 2\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)
     telnet.write("bgp router-id 2.2.2.2\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)
     telnet.write("neighbor 10.10.1.12 remote-as 1\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)
     telnet.write("address-family ipv4 unicast\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out)
     telnet.write("network 40.1.1.0/24\n")
     out = telnet.read_until("#", 5)
     logging.info("%s"%out) 
    telnet.write("end\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.close()

def connect_verify_bgp():
    telnet=telnetlib.Telnet()
    telnet.open("192.168.203.22",2605)
    out = telnet.read_until(">", 5)
    logging.info("%s"%out)
    telnet.write("en\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("show bgp ipv4 unicast\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("show ip bgp neighbors 10.10.1.9\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    check1= re.search(r'BGP state = Established, up', out, re.I|re.S)
    telnet.close()
    telnet.open("192.168.203.24",2605)
    out = telnet.read_until(">", 5)
    logging.info("%s"%out)
    telnet.write("en\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("show bgp ipv4 unicast\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("show ip bgp neighbors 10.10.1.12\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    check2 = re.search(r'BGP state = Established, up', out, re.I|re.S)
    telnet.close()
    if check1 and check2 :
      logging.info("BGP neighborship is up in both hosts")
      return 1
    else :
      logging.info("BGP neighborship is not up in both hosts")
      return 0

def connect_host_verify_ping(host,dst_ip):
    k = paramiko.RSAKey.from_private_key_file("/home/testpc/automation/rmaity/test_demo/loginkey.pem")
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("connecting to %s"%host)
    #H.connect( hostname = host, username = "ubuntu", password = "ubuntu" )
    H.connect( hostname = host, username = "ubuntu", pkey = k )
    logging.info("connected to %s"%host)
    logging.info("Executing ping to Destination %s from Host %s"%(dst_ip,host)) 
    stdin , stdout, stderr = H.exec_command("ping -c 5 {}".format(dst_ip))
    ping=stdout.read()
    logging.info("%s"%ping)
    H.close()
    m=re.search(b'100% packet loss',ping)
    if m:
        logging.error("Ping fails to Destination %s from Host %s"%(dst_ip,host))
        return 0
    else:
        logging.info("Ping success to Destination %s from Host %s"%(dst_ip,host)) 
        return 1

def connect_host_verify_with_iperf3(host,server_ip,mode,traffic='single'):
    k = paramiko.RSAKey.from_private_key_file("/home/testpc/automation/rmaity/test_demo/loginkey.pem")
    H = paramiko.SSHClient()
    H.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    logging.info("connecting to %s"%host)
    #H.connect( hostname = host, username = "ubuntu", password = "ubuntu" )
    H.connect( hostname = host, username = "ubuntu", pkey = k )
    logging.info("connected to %s"%host)
    if 'single' in traffic :
       traffic_cli = "iperf3 -c %s -b 30K"%server_ip
    else :
       traffic_cli = "iperf3 -c %s -b 10M -t 65 -O 5 -u"%server_ip
    if mode=="client":
        stdin , stdout, stderr = H.exec_command("%s"%traffic_cli)
        time.sleep(10)
        result=stdout.read()
        logging.info(result)
        if 'single' in traffic:
          m=re.search(b'.*\s+([0-9\.]+)\s+(\w+)\s+([0-9\.]+)\s+\w+/sec\s+\d+\s+sender', result,re.M)
          n=re.search(b'.*\s+([0-9\.]+)\s+(\w+)\s+([0-9\.]+)\s+\w+/sec\s+receiver', result,re.M)
          if float(m.group(1))>0:
            logging.info("Client %s had sent %s%s traffic"%(host,m.group(1),m.group(2)))
          else:
            logging.error("Client %s had sent %s%s traffic"%(host,m.group(1),m.group(2))) 
            return 0
          if float(n.group(1))>0:
            logging.info("Server %s had received %s%s traffic"%(host,n.group(1),n.group(2)))
          else:
            logging.error("Server %s had received %s%s traffic"%(host,n.group(1),n.group(2)))
            return 0
          if float(m.group(1))-2<=float(n.group(1))<=float(m.group(1))+2:
            logging.info("PASS: Client %s had received %s%s traffic which is within threshold range of sent traffic %s%s"%(host,n.group(1),n.group(2),m.group(1),m.group(2)))
            return 1
          else:
            #logging.error("FAIL: Client %s had received %s%s traffic which is not within threshold range of sent traffic %s%s"%(host,n.group(1),n.group(2),m.group(1),m.group(2)))
            return 0
        else:
           check = re.search(r'(0.00-65.*)', result)
           if check :
             output = check.group()
             check1 = re.search(r'((([0-9]+.[0-9]+)|([0-9]+))%)', output)
             lost_value=check1.group()
             lost_value=float(lost_value.strip('%'))
             check2 = re.search(r'(([0-9]+.[0-9]+)\sms)', output)
             jit_value=check2.group()
             jit_value=float(jit_value.strip(' ms'))
             check3 = re.search(r'(([0-9]+.[0-9]+)\sMbits/sec)', output)
             bw_value=check3.group()
             bw_value=float(bw_value.strip(' Mbits\/sec'))
             if lost_value <= 15 and jit_value < 15 and bw_value > 9.5:
               logging.info("PASS: As expected the bandwidth %s,Jitter %s,lost datagrams %s are in threshold range"%(bw_value,jit_value,lost_value))
               return 1
             else :
               logging.error("FAIL: As expected the bandwidth ,Jitter ,lost datagrams are not in threshold range")
               logging.error("EXPECTED: bandwidth 9.5,Jitter less than 15,lost datagrams less than 15")
               logging.error("ACTUAL: bandwidth %s,Jitter %s,lost datagrams %s"%(bw_value,jit_value,lost_value))
               return 0
           else :
             logging.error("FAIL: couldnt retrieve the traffic statistics")
             return 0
    else:
        stdin , stdout, stderr = H.exec_command("iperf3 -s -D")
        logging.info("iperf3 server started successfully")
    H.close()

def delete_iptables(ip):
    table = iptc.Table(iptc.Table.FILTER)
    for chain in table.chains:
        for rule in chain.rules:
            if rule.src == '%s/255.255.255.255'%ip:
                call(["iptables", "-D", "%s"%chain.name, "2"])

def connect_configure_ospf(host, port, idx):
    telnet=telnetlib.Telnet()
    telnet.open("%s" % host,"%s" % port)
    out = telnet.read_until(">", 5)
    logging.info("%s"%out)
    telnet.write("en\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("configure terminal\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("router ospf\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    if idx == 1:
     rid = '1.1.1.1'
     ip1 = '20.1.1.0/24'
     ip2 = '10.10.1.0/24'
    else:
     rid = '2.2.2.2'
     ip1 = '10.10.1.0/24'
     ip2 = '40.1.1.0/24'
    telnet.write("router-id %s\n" % rid)
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("network %s area 0\n" % ip1)
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("network %s area 0\n" % ip2)
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("end\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.close()

def connect_verify_ospf(ip1, ip2):
    telnet=telnetlib.Telnet()
    telnet.open(ip1, 2604)
    out = telnet.read_until(">", 5)
    logging.info("%s"%out)
    telnet.write("en\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("show ip ospf neighbor\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    check1= re.search(r'%s.*FULL' % '2.2.2.2', out, re.I|re.S)
    telnet.close()
    telnet.open(ip2, 2604)
    out = telnet.read_until(">", 5)
    logging.info("%s"%out)
    telnet.write("en\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    telnet.write("show ip ospf neighbor\n")
    out = telnet.read_until("#", 5)
    logging.info("%s"%out)
    check2 = re.search(r'%s.*FULL' % '1.1.1.1', out, re.I|re.S)
    telnet.close()
    if check1 and check2 :
      logging.info("OSPF neighborship is up in both hosts")
      return 1
    else :
      logging.info("OSPF neighborship is not up in both hosts")
      return 0












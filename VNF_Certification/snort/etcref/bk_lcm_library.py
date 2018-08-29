import util_findhost
from util_connection import SSHConnection
import time
import os
import subprocess
import json

def exec_sys_command(cmd):
    #return os.popen(cmd).read()
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    if out:
	return out
    if err:
	return err
	
def create_stack(stack_name, heat_tmplt):
    ost_cmd = 'openstack stack create -t /home/test/automation/lcm/yaml/' + heat_tmplt + ' ' + stack_name
    print "create vm command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return False if output.find(stack_name) == -1 else True

def update_stack(stack_name, heat_tmplt):
    ost_cmd = 'openstack stack update -t /home/test/automation/lcm/yaml/' + heat_tmplt + ' ' + stack_name
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
    ost_cmd = "openstack server image create %s --name %s" %(server_name, snapshot_name)
    print "Create snapshot command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
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
    print ip_set
    if ';' in ip_set:
	ip2 = ip_set.split(';')[0].split("=")[1]
	ip_set = ip_set.split(';')[1]
    else:
	ip2 = None
    ip = ip_set.split(',')[0].split("=")[1]
    ip_float = ip_set.split(',')[1]
    subprocess.call(["cp", "/dev/null", "/home/test/.ssh/known_hosts"])
    c1 = SSHConnection(IP=ip_float, username="debian", ssh_key="/home/test/automation/lcm/key234demo.pem")
    try:
	c1.connect()
    except:
	print "first connection failed"
	time.sleep(180)
        c1 = SSHConnection(IP=ip_float, username="debian", ssh_key="/home/test/automation/lcm/key234demo.pem")
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
    script = "/home/test/automation/lcm/" + env_file
    out = subprocess.Popen(". %s; env" % script, stdout=subprocess.PIPE, shell=True)
    output = out.communicate()[0]
    environment_var = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(environment_var)
    time.sleep(5)

def vnf_create_instance(stack_name):
    if not create_stack(stack_name, 'vnf.yml'):
	return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    if stack_create_status == "Stack CREATE completed successfully":
	return validate_ip_vnf(stack_name)
    else:
	print "stack_create_status is:", stack_create_status
	return False

def vnf_create_instance_multinet(stack_name):
    if not create_stack(stack_name, 'vnf2.yml'):
        return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    if stack_create_status == "Stack CREATE completed successfully":
        if not validate_ip_vnf(stack_name):
	    print "server ip validation failed"
	    return False
	if not vnf_delete_stack(stack_name):
	    print "stack deletion failed"
	    return False
	else:
	    return True
    else:
	print "stack_create_status is:", stack_create_status
	return False

def vnf_update_instance(stack_name):
    if not update_stack(stack_name, 'vnf_update.yml'):
	return False
    time.sleep(60)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    return True if stack_create_status == "Stack UPDATE completed successfully" else False

def vnf_delete_stack(stack_name):
    retVal = delete_stack(stack_name)
    if not retVal == None:
        print "stack deletion failed: " + retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('stackShow', stack_name, "noStack")
    return stack_create_status == "Stack not found: " + stack_name + "\n"

def vnf_delete_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = delete_server(server_name)
    if not retVal == "\n":
        print "server deletion failed: " + retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "noStack")
    return stack_create_status == "No server with a name or ID of '%s' exists.\n" % server_name

def vnf_soft_reboot_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = reboot_server(server_name, 'soft')
    if retVal != "Complete\n":
	print "server soft reboot failed", retVal
	return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    print "stack_create_status", stack_create_status
    return stack_create_status == "ACTIVE"

def vnf_hard_reboot_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = reboot_server(server_name, 'hard')
    if retVal != "Complete\n":
        print "server hard reboot failed", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "ACTIVE"

def vnf_create_snapshot(stack_name, snapshot_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    if not create_snapshot(server_name, snapshot_name):
        return False
    time.sleep(30)
    stack_create_status = parse_json('imageShow', snapshot_name, "status")
    return stack_create_status == "active"

def vnf_delete_snapshot(snapshot_name):
    retVal = delete_snapshot(snapshot_name)
    if not retVal == None:
        print "snapshot deletion failed", retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('imageShow', snapshot_name, "noStack")
    return stack_create_status == "Could not find resource " + snapshot_name + "\n"

def vnf_pause_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = pause_server(server_name)
    if not retVal == None:
	print "server pause failed: ", retVal
	return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "PAUSED"

def vnf_unpause_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = unpause_server(server_name)
    if not retVal == None:
	print "server unpause failed: ", retVal
	return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "ACTIVE"

def vnf_suspend_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = suspend_server(server_name)
    if not retVal == None:
	print "server suspend failed: ", retVal
	return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "SUSPENDED"

def vnf_resume_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    retVal = resume_server(server_name)
    if not retVal == None:
	print "server resume failed: ", retVal
	return False
    time.sleep(30)
    stack_create_status = parse_json('serverShow', server_name, "status")
    return stack_create_status == "ACTIVE"
'''
def vnf_migrate_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    migrate_server(server_name)
    time.sleep(30)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    return stack_create_status

def vnf_live_migrate_server(stack_name):
    server_name = parse_json('stackShow', stack_name, "server_name")
    live_migrate_server(server_name)
    time.sleep(30)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    return stack_create_status
'''
set_environment("demo-openrc")
def test_complete():
    pass



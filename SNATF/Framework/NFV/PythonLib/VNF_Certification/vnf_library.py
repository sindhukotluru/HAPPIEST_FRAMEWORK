import pexpect
import util_findhost
from util_connection import SSHConnection
import time
import os
import subprocess
import json
import re
import iptc

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

def upgrade_stack(stack_name, heat_tmplt):
    ost_cmd = 'openstack stack update -t /home/test/automation/lcm/yaml/' + heat_tmplt + ' ' + stack_name
    print "create vm command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    return False if output.find(stack_name) == -1 else True

def downgrade_stack(stack_name, heat_tmplt):
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
    ip_login = ip_set.split(',')[1]
    if ip2:
	subprocess.call(["sudo", "dhclient", "eth1"])
    subprocess.call(["cp", "/dev/null", "/home/test/.ssh/known_hosts"])
    c1 = SSHConnection(IP=ip_login, username="ubuntu", ssh_key="/home/test/automation/lcm/key234demo.pem")
    try:
	c1.connect()
    except:
	print "first connection failed"
	time.sleep(180)
        c1 = SSHConnection(IP=ip_login, username="ubuntu", ssh_key="/home/test/automation/lcm/key234demo.pem")
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


login_ip = []
s_ns = []

def validate_ip_vnf_multistack(multi_stack_name):
    set_environment("admin-openrc")
    global login_ip
    global s_ns
    ns_handler = []
    nw = {}
    cmd = []
    for idx in range(3):
        ost_cmd = "openstack server list | grep %s-server%s" % (multi_stack_name, idx+1) 
        output = exec_sys_command(ost_cmd)
        server_name = output.split('|')[2].split()[0]
        login_ip.append(output.split('|')[4].split(';')[0].split('=')[1].rstrip())       
	if 'server2' in server_name:
	    s2_ip2 = output.split('|')[4].split(';')[1].split('=')[1].split(',')[0]
	ip_login = login_ip[idx]
	op = os.popen('sudo ip netns | grep qdhcp').read()
	ns = [i.split(" ")[0] for i in op.rstrip('\n').split('\n')]
	tempCmd = 'sudo ip netns exec %s bash' %(ns[idx])
	ns_handler.append(pexpect.spawn(tempCmd))
	cmd = ["ifconfig | grep 'Bcast'"]
	ifLine = get_pexpect_op(ns_handler[idx], cmd, prompt=".*\#")
	nwRe = re.search('\d+\.\d+\.\d+', ifLine)
	nw[ns[idx]] = nwRe.group(0)
   
    login_ip.append(s2_ip2)

    for idx in range(3):
	if nw[ns[idx]] in login_ip[0]:
	    s1_ns = ns_handler[idx]
	if nw[ns[idx]] in login_ip[3]:
	    tempCmd = 'sudo ip netns exec %s bash' %(ns[idx])
	    ns_handler.append(pexpect.spawn(tempCmd))
	    s2_ns = ns_handler[-1]
        if nw[ns[idx]] in login_ip[2]:
            s3_ns = ns_handler[idx]

    #server 1 login
    login_ns(s1_ns, login_ip[0])
    #server 2 login
    login_ns(s2_ns, login_ip[3])
    #server 3 login
    login_ns(s3_ns, login_ip[2])
    #Basic Scenario	
    #cmd = ["sudo su"]
#    cmd = ["sudo dhclient"]
#    cmd.append("sudo sysctl -w net.ipv4.ip_forward=1")
#    print get_pexpect_op(s2_ns, cmd, prompt=".*\$")
#    cmd = ["sudo route del default gw 192.168.101.1"]
#    cmd.append("sudo route add default gw %s" %login_ip[1])
#    print get_pexpect_op(s1_ns, cmd, prompt=".*\$")	
#    cmd = ["sudo route del default gw 192.168.102.1"]
#    cmd.append("sudo route add default gw %s" %login_ip[3])
#    print get_pexpect_op(s3_ns, cmd, prompt=".*\$")
           
#    for ip in login_ip:
#	delete_iptables(ip)
#    print "---------------------------", login_ip
    s_ns = [s1_ns, s2_ns, s3_ns]
    return login_ip, s_ns

def delete_iptables(ip):
    table = iptc.Table(iptc.Table.FILTER)
    for chain in table.chains:
        for rule in chain.rules:
            if rule.src == '%s/255.255.255.255'%ip:
                subprocess.call(["sudo", "iptables", "-D", "%s"%chain.name, "2"])

def login_ns(nsName, loginIp):

    cmd = ["sudo ssh -o StrictHostKeyChecking=no -i key.pem ubuntu@%s" %loginIp]
    #op = get_pexpect_op(nsName, cmd, ".*\$")

    op = get_pexpect_op(nsName, cmd, prompt=".*\$")

    print op

def get_pexpect_op(handler, cmd, prompt=".*[#$]"):
    for i in cmd:
        handler.sendline(i)
        handler.sendline("\r")
	time.sleep(5)
        handler.expect(prompt)
    return handler.after
#ICMP test	 
def test_icmp_traffic():
    print "--------ICMP TEST STARTED----------"
    cmd1 = ["sudo ping -c 3 " + login_ip[2]]
    cmd2 = ["sudo ping -c 3 " + login_ip[0]]
    #print s_ns[0] 
    op1 = get_pexpect_op(s_ns[0], cmd1)
    #prompt=".*\$"
    op2 = get_pexpect_op(s_ns[2], cmd2)
    print op1
    print op2
    pat = " 0% packet loss"
    if pat in op1 and pat in op2:
	return True
    else:
	return False
#ICMP RULE ADD
def test_rule_write(rule):
    print "--------Rule Addition STARTED----------"
#    login_ns(s2_ns, login_ip[3])
#    rule = '''\"drop icmp 192.168.102.3 any -> \$HOME_NET any (msg:"ICMP test detected"; GID:1; sid:50000001; rev:001; classtype:icmp-event;)
#drop icmp \$HOME_NET any -> 192.168.102.3 any (msg:"ICMP test detected"; GID:1; sid:50000001; rev:001; classtype:icmp-event;)\"'''
    cmd1 = ["sudo echo %s > /etc/snort/rules/local.rules" %rule]
    cmd2 = ["cat /etc/snort/rules/local.rules"]
    op1 = get_pexpect_op(s_ns[1], cmd1)
    op2 = get_pexpect_op(s_ns[1], cmd2)
    print op1
    print op2
    if " Connection timed out" in op1:
	return True
    else:
	return False

#start firewall
def test_up_firewall():
    print "------------------STARTING FIREWALL-------------------------"
    cmd3 = ["sudo snort -A console -q -c /etc/snort/snort.conf -Q &"]
    print cmd3
    op3 = get_pexpect_op(s_ns[1], cmd3, prompt=".*")
    #(?!(.*\#))
    time.sleep(10)
    pat4 = " Caught Int-Signal"
    if pat4 not in op3:
	return True
    else:
	return False

#HTTP TEST
def test_http_traffic():
    print "--------HTTP TEST STARTED----------"
    cmd1 = ["curl http://www.google.com "]
    op1 = get_pexpect_op(s_ns[0], cmd1, prompt=".*\$")
    print op1
    pat = " Connection refused"
    if pat not in op1:
	return True
    else:
	return False

#shutdown firewall
def test_down_firewall():
    print "--------FIREWALL SHUTDOWN----------"
    cmd4 = ["sudo killall snort"]
    op4 = get_pexpect_op(s_ns[1], cmd4, prompt=".*\$")
    time.sleep(5)
    pat4 = " Caught Int-Signal"
    if pat4 not in op4:
        return True
    else:
	return False

#inline mode
def test_check_inline():
    print "-----CHECKING INLINE MODE INFO-----"
    cmd5 = ["sudo snort --daq-list"]
    op5 = get_pexpect_op(s_ns[1], cmd5, prompt=".*\$")
    print op5
    pat5 = "afpacket(v5): live inline"
    if pat5 in op5:
        return True
    else:
	return False
#inline-test test mode
def test_check_inline_test():
    print "-----CHECKING INLINE TEST MODE INFO-----"
    cmd = ["sudo snort -vde --enable-inline-test"]
    print "------------>", cmd
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    print "output is --------------->",op
    time.sleep(5)
    print op
    pat = "Enable Inline Test Mode"
    if pat in op:
        return True
    else:
	return False
#sniffer mode
def test_check_sniffer():
    print "-----ACTIVATING SNIFFER MODE-----"
    cmd = ["sudo snort -vde"]
    print "------------>", cmd
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    print "output is --------------->",op
    time.sleep(5)
    print op
    pat = "Commencing packet processing"
    if pat in op:
        return True
    else:
	return False
#NIDS mode
def test_check_NIDS():
    print "-----ACTIVATING NIDS MODE-----"
    cmd = ["sudo snort -dev -l ./log -h 192.168.101.0/24 -c /etc/snort/snort.conf"]
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    time.sleep(5)
    print op
    pat = "Running in IDS mode"
    if pat in op:
        return True
    else:
	return False
#NIDS read mode
def test_check_NIDS_read():
    print "-----ACTIVATING NIDS READ MODE-----"
    cmd = ["ls /home/ubuntu/log/ | awk 'END {print}'"]
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    re1 = re.search("snort.log.[0-9]+", op)
    op1 = re1.group(0)
    cmd1 = ["sudo snort -dvr /home/ubuntu/log/"+op1]
    op2 = get_pexpect_op(s_ns[1], cmd1, prompt=".*\$")
    print op2
    pat = "pcap DAQ configured to read-file"
    if pat in op2:
        return True
    else:
	return False
#packet logger mode
def test_check_pkt_logger():
    print "-----ACTIVATING PACKET LOGGER MODE-----"
    cmd = ["sudo snort -dev -l ./log"]
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*")
    time.sleep(5)
    print op
    pat = "Running in packet logging mode"
    if pat in op:
        return True
    else:
	return False
#log file check
def check_log_file():
    print "-----FIND LOG FILES-----"
    cmd = ["ls /home/ubuntu/log/"]
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    print op
    pat = "snort.log"
    if pat in op:
        return True
    else:
	return False
#SSH Test
def test_check_ssh():
    print "-----Initiating SSH Connection-----"
    cmd = ["sudo ssh ubuntu@"+ login_ip[0]]
    print "command is-------->",cmd
    op = get_pexpect_op(s_ns[2], cmd, prompt=".*\$")
    print op
    pat = " Connection refused"
    if pat in op:
        return True
    else:
	return False
#MALWARE TEST
def test_malware():
    print "--------MALWARE TEST STARTED----------"
    cmd1 = ["sudo wget https://secure.eicar.org/eicar.com.txt "]
    op1 = get_pexpect_op(s_ns[0], cmd1, prompt=".*\$")
    print op1
    pat = " connected"
    if pat not in op1:
	return True
    else:
	return False

def set_environment(env_file):
    script = "/home/test/automation/lcm/" + env_file
    #os.system("sudo su")
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

def vnf_delete_stack(stack_name):
    retVal = delete_stack(stack_name)
    if not retVal == None:
        print "stack deletion failed: " + retVal
        return False
    time.sleep(30)
    stack_create_status = parse_json('stackShow', stack_name, "noStack")
    return stack_create_status == "Stack not found: " + stack_name + "\n"

def vnf_create_multistack(stack_name):
    set_environment("admin-openrc")
    if not create_stack(stack_name, 'ubuntu_multiserver.yml'):
        return False
    #time.sleep(120)
    #if not create_stack(stack_name, 'ubuntu_multiserver1.yml'):
    #    return False
    #time.sleep(120)
    stack_create_status = parse_json('stackShow', stack_name, "stack_status_reason")
    if stack_create_status == "Stack CREATE completed successfully":
	return True
	
#        if validate_ip_vnf_multistack(stack_name):
#            print "server ip validation PASS"
#            return True
#        else:
#            print "server ip validation failed"
#            return False
	
    else:
        print "stack_create_status is:", stack_create_status
        return False

#ICMP TEST ALLOW
def vnf_allow_icmp_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack(stack_name)
    time.sleep(5)
    time.sleep(5)    
    rule = '''\"alert icmp 192.168.102.3 any -> \$HOME_NET any (msg:"ICMP test detected"; GID:1; sid:50000001; rev:001; classtype:icmp-event;)
alert icmp \$HOME_NET any -> 192.168.102.3 any (msg:"ICMP test detected"; GID:1; sid:50000001; rev:001; classtype:icmp-event;)\"'''
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    result = test_icmp_traffic()
    time.sleep(5)
#    vnf_firewall_down(stack_name)
    test_down_firewall()
    time.sleep(5)
    return result

#ICMP TEST ALLOW
def vnf_icmp_alldrop_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack(stack_name)    
    rule = '''\"drop icmp 192.168.102.3 any -> \$HOME_NET any (msg:"ICMP test detected"; GID:1; sid:50000001; rev:001; classtype:icmp-event;)
drop icmp \$HOME_NET any -> 192.168.102.3 any (msg:"ICMP test detected"; GID:1; sid:50000001; rev:001; classtype:icmp-event;)\"'''
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    result = test_icmp_traffic()
    time.sleep(5)
#    vnf_firewall_down(stack_name)
    test_down_firewall()
    time.sleep(5)
    return result

#ICMP TEST BLOCK
def vnf_block_icmp_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    rule = '''\"drop icmp 192.168.102.3 any -> \$HOME_NET any (msg:"ICMP test detected"; GID:1; sid:50000001; rev:001; classtype:icmp-event;)
drop icmp \$HOME_NET any -> 192.168.102.3 any (msg:"ICMP test detected"; GID:1; sid:50000001; rev:001; classtype:icmp-event;)\"'''
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
#    result = test_icmp_traffic(login_ip, s_ns)
    result = test_icmp_traffic()
    time.sleep(5)
#    vnf_firewall_down(stack_name)
    test_down_firewall()
    time.sleep(5)
    return result

#http test allow
def vnf_http_allow_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    rule = '''\"alert tcp \$HOME_NET any -> any 80 (msg:"Warning!!, A host is trying to access /admin"; sid:1002355; rev:2; classtype:web-application-activity;)\"'''
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    result = test_http_traffic()
    time.sleep(5)
#    vnf_firewall_down(stack_name)
    test_down_firewall()
    time.sleep(5)
    return result

#http test block
def vnf_http_block_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    rule = '''\"drop tcp \$HOME_NET any -> any 80 (msg:"Warning!!, A host is trying to access /admin"; sid:1002355; rev:2; classtype:web-application-activity;)\"'''
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    result = test_http_traffic()
    time.sleep(5)
#    vnf_firewall_down(stack_name)
    test_down_firewall()
    time.sleep(5)
    return result
#####################################################################################################################
###########################################----HTTP test in multi----################################################
#####################################################################################################################
#login_ip = []
#s_ns = []

def validate_ip_vnf_multistack1(multi_stack_name):
    set_environment("admin-openrc")
    global login_ip
    global s_ns
    ns_handler = []
    nw = {}
    cmd = []
    for idx in range(3):
        ost_cmd = "openstack server list | grep %s-server%s" % (multi_stack_name, idx+1) 
        output = exec_sys_command(ost_cmd)
        server_name = output.split('|')[2].split()[0]
        login_ip.append(output.split('|')[4].split(';')[0].split('=')[1].rstrip())       
	if 'server2' in server_name:
	    s2_ip2 = output.split('|')[4].split(';')[1].split('=')[1].split(',')[0]
	ip_login = login_ip[idx]
	op = os.popen('sudo ip netns | grep qdhcp').read()
	ns = [i.split(" ")[0] for i in op.rstrip('\n').split('\n')]
	tempCmd = 'sudo ip netns exec %s bash' %(ns[idx])
	ns_handler.append(pexpect.spawn(tempCmd))
	cmd = ["ifconfig | grep 'Bcast'"]
	ifLine = get_pexpect_op(ns_handler[idx], cmd, prompt=".*\#")
	nwRe = re.search('\d+\.\d+\.\d+', ifLine)
	nw[ns[idx]] = nwRe.group(0)
  
    login_ip.append(s2_ip2)

    for idx in range(3):
	if nw[ns[idx]] in login_ip[0]:
	    s1_ns = ns_handler[idx]

	if nw[ns[idx]] in login_ip[3]:
	    tempCmd = 'sudo ip netns exec %s bash' %(ns[idx])
	    ns_handler.append(pexpect.spawn(tempCmd))
	    s2_ns = ns_handler[-1]

        if nw[ns[idx]] in login_ip[2]:
            s3_ns = ns_handler[idx]

    s_ns = [s1_ns, s2_ns, s3_ns]
    return login_ip, s_ns

def run_conf(stack_name):
    #Multiple hosts covering single firewall interface
    #server 2 login
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    login_ns(s_ns[1], login_ip[3])
    cmd = ["sudo dhclient"]
    cmd.append("sudo sysctl -w net.ipv4.ip_forward=1")
    print get_pexpect_op(s_ns[1], cmd)
    #server 1 login
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    login_ns(s_ns[0], login_ip[0])    
    cmd = ["sudo route del default gw 192.168.101.1"]
    cmd.append("sudo route add default gw %s" %login_ip[1])
    print get_pexpect_op(s_ns[0], cmd)
    #server 3 login
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[2])
    time.sleep(5)	
    cmd = ["sudo route del default gw 192.168.101.1"]
    cmd.append("sudo route add default gw %s" %login_ip[1])
    print get_pexpect_op(s_ns[2], cmd)
    
    for ip in login_ip:
	delete_iptables(ip)

def test_http_traffic1(s_ns,login_ip):
    print "--------HTTP TEST STARTED----------"
    cmd = ["curl http://www.facebook.com"]
    op = get_pexpect_op(s_ns, cmd, prompt=".*\$")
    print op
    return op
    pat = " Connection refused"
    if pat not in op:
	return True
    else:
	return False
#TESTCASE 1
def vnf_allow1_http_test_multi(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
#    run_conf(stack_name)
#    time.sleep(5)
    rule = '''\"alert tcp 192.168.101.5 any -> any 80 (msg:"Http request detected"; sid:1002355; rev:2; classtype:web-application-activity;)
drop tcp 192.168.101.3 any -> any 80 (msg:"Http request detected"; sid:1002356; rev:2; classtype:web-application-activity;)\"'''
    login_ns(s_ns[1], login_ip[3])
    time.sleep(5)
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[0])
    time.sleep(5)
    result = test_http_traffic1(s_ns[0],login_ip[0])
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[2])
    time.sleep(5)
    result1 = test_http_traffic1(s_ns[0],login_ip[2])
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    login_ns(s_ns[1], login_ip[3])
    cmd = ["sudo killall snort"]
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    time.sleep(5)
    return result, result1
#TESTCASE 2
def vnf_block1_http_test_multi(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
#    run_conf()
#    time.sleep(5)
    rule = '''\"drop tcp 192.168.101.5 any -> any 80 (msg:"Http request detected"; sid:1002355; rev:2; classtype:web-application-activity;)
alert tcp 192.168.101.3 any -> any 80 (msg:"Http request detected"; sid:1002356; rev:2; classtype:web-application-activity;)\"'''
    login_ns(s_ns[1], login_ip[3])
    time.sleep(5)
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[0])
    time.sleep(5)
    result = test_http_traffic1(s_ns[0],login_ip[0])
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[2])
    time.sleep(5)
    result1 = test_http_traffic1(s_ns[0],login_ip[2])
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    login_ns(s_ns[1], login_ip[3])
    cmd = ["sudo killall snort"]
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    time.sleep(5)
    return result, result1
#TESTCASE 3
def vnf_allallow_http_test_multi(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
#    run_conf()
#    time.sleep(5)
    rule = '''\"alert tcp \$HOME_NET any -> any 80 (msg:"Http request detected"; sid:1002355; rev:2; classtype:web-application-activity;)\"'''
    login_ns(s_ns[1], login_ip[3])
    time.sleep(5)
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[0])
    time.sleep(5)
    result = test_http_traffic1(s_ns[0],login_ip[0])
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[2])
    time.sleep(5)
    result1 = test_http_traffic1(s_ns[0],login_ip[2])
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    login_ns(s_ns[1], login_ip[3])
    cmd = ["sudo killall snort"]
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    time.sleep(5)
    return result, result1
#TESTCASE 4
def vnf_allblock_http_test_multi(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
#    run_conf()
#    time.sleep(5)
    rule = '''\"drop tcp \$HOME_NET any -> any 80 (msg:"Http request detected"; sid:1002355; rev:2; classtype:web-application-activity;)\"'''
    login_ns(s_ns[1], login_ip[3])
    time.sleep(5)
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[0])
    time.sleep(5)
    result = test_http_traffic1(s_ns[0],login_ip[0])
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    time.sleep(5)
    login_ns(s_ns[0], login_ip[2])
    time.sleep(5)
    result1 = test_http_traffic1(s_ns[0],login_ip[2])
    time.sleep(5)
    login_ip, s_ns = validate_ip_vnf_multistack1(stack_name)
    login_ns(s_ns[1], login_ip[3])
    cmd = ["sudo killall snort"]
    op = get_pexpect_op(s_ns[1], cmd, prompt=".*\$")
    time.sleep(5)
    return result, result1
#####################################################################################################################
#INLINE MODE
def vnf_inline_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
#    login_ip, s_ns = validate_ip_vnf_multistack(stack_name)
    result = test_check_inline()
    time.sleep(5)
    return result

#INLINE TEST MODE
def vnf_inline_testmode_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    result = test_check_inline_test()
    time.sleep(5)
    vnf_firewall_down(stack_name)
    time.sleep(5)
    return result

#SNIFFER MODE
def vnf_sniffer_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    result = test_check_sniffer()
    time.sleep(5)
    vnf_firewall_down(stack_name)
    time.sleep(5)
    return result

#NIDS MODE
def vnf_NIDS_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    result = test_check_NIDS()
    time.sleep(5)
    vnf_firewall_down(stack_name)
    time.sleep(5)
    return result

#NIDS READ MODE
def vnf_NIDS_read_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    result = test_check_NIDS_read()
    time.sleep(5)
    return result

#PACKET LOGGER MODE
def vnf_pkt_logger_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    test_check_pkt_logger()
    time.sleep(5)
    vnf_firewall_down(stack_name)
    time.sleep(5)
    result = check_log_file()
    return result

#SSH TEST
def vnf_ssh_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    rule = '''\"drop tcp 192.168.102.3 any -> \$HOME_NET 22 (msg:"Potential SSH Brute Force Attack"; GID:1; sid:2001219; rev:4; classtype:attempted-dos; resp:rst_all;)\"'''
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    result = test_check_ssh()
    time.sleep(5)
#    vnf_firewall_down(stack_name)
    test_down_firewall()
    time.sleep(3)
    return result    

#MALWARE TEST
def vnf_malware_test(stack_name):
    set_environment("admin-openrc")
    print "stack_name : %s " %stack_name
    time.sleep(5)
    rule = '''\"drop tcp \$HOME_NET any -> any any (msg:"Warning!!, A host is trying to access /admin"; sid:1002355; rev:2; classtype:web-application-activity;)\"'''
    test_rule_write(rule)
    time.sleep(5)
    vnf_firewall_up(stack_name)
    time.sleep(5)
    result = test_malware()
    time.sleep(5)
#    vnf_firewall_down(stack_name)
    test_down_firewall()
    time.sleep(3)
    return result    

#START FIREWALL
def vnf_firewall_up(stack_name):
    set_environment("admin-openrc")
    result = test_up_firewall()
    time.sleep(5)
    return result

#STOP FIREWALL
def vnf_firewall_down(stack_name):
    set_environment("admin-openrc")
    login_ip, s_ns = validate_ip_vnf_multistack(stack_name)
    time.sleep(5)
    result = test_down_firewall()
    time.sleep(5)
    return result

set_environment("admin-openrc")
def test_complete():
    pass


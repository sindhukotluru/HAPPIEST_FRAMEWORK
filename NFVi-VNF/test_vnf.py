import util_findhost
from util_connection import SSHConnection
import time
import os
import pexpect
import subprocess
from pexpect import pxssh

debug = True


def dlog(log):
    if debug:
        print log


def exec_sys_command(cmd):
    import os
    return os.popen(cmd).read()


def create_stack(stack_name, heat_tmplt):
    status = True
    ost_cmd = 'openstack stack create -t /home/execution/' + heat_tmplt + ' ' + stack_name
    print "create vm command: ", ost_cmd
    output = exec_sys_command(ost_cmd)
    if output.find(stack_name) != -1:
        pass
    else:
        status = False
    return status


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


def create_image(image_name):
    status = True
    cmd = "openstack image create --disk-format=vhdx  --file=/home/execution/lvm.vhdx" + image_name
    out = exec_sys_command(cmd)
    if out.find(image_name) != -1:
        print "Image - " + image_name + " -- successfully created"
    else:
        status = False
    return status


def show_stack(stack_name):
    ost_cmd2 = "openstack stack show " + stack_name + " | grep 'output_value: " + stack_name + "' | awk ' { print $4 }'"
    print "show_stack_command: ", ost_cmd2
    output = exec_sys_command(ost_cmd2).strip()
    return output


def delete_stack(vm_name):
    os.system("openstack stack delete --yes " + vm_name)


def intf_ip(stack_name):
    ost_cmd5 = "openstack server show " + stack_name + " --format json | grep addresses"
    print "show_server_command for intf ip: ", ost_cmd5
    output = exec_sys_command(ost_cmd5).strip()
    ipset = util_findhost.get_ip_set(output)
    return ipset


def show_server(stack_name, num):
    ost_cmd3 = "openstack server show " + stack_name + " | grep addresses | awk ' { print $" + str(num) + " } '"
    print "show_server_command: ", ost_cmd3
    output = exec_sys_command(ost_cmd3).strip()
    return output


def run_set_cmd(handle, cmd):
    status = handle.execute_command(cmd)
    return status


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


def set_intf(handle, cmd_eth_ip):
    handle.execute_command(cmd_eth_ip)


def route_add(handle, cmd_rt_add):
    handle.execute_command(cmd_rt_add)


def en_ip_fwd(handle, cmd_ipfwd):
    handle.execute_command(cmd_ipfwd)


def cmd_exec(handle, cmd_x):
    handle.execute_command(cmd_x)


def set_environment(env_file):
    script = "/home/execution/" + env_file
    out = subprocess.Popen(". %s; env" % script, stdout=subprocess.PIPE, shell=True)
    output = out.communicate()[0]
    environment_var = dict((line.split("=", 1) for line in output.splitlines()))
    os.environ.update(environment_var)


def vnf_infrastructure_setup(vm1_name, vm2_name, vm3_name, vm4_name, vm5_name, vm6_name):
    vm_ip = []
    vm_name = []
    vm_detail = []
    network = {"priv1":"192.168.1.0", "priv2":"192.168.2.0", "priv3":"192.168.3.0", "priv4":"192.168.4.0", \
               "priv5":"192.168.5.0", "private":"10.0.0.0"}

    image_list = ["ubuntu"]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    set_environment("admin-openrc")
    time.sleep(5)

    for network_name, subnet in network.items():
        status = create_network(network_name, subnet)
        if status:
            pass

    #for image in image_list:
     #   status = create_image(image)
      #  if status:
       #     pass

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    set_environment("demo-openrc")

    # os.environ['OS_PROJECT_DOMAIN_NAME'] = 'Default'
    # os.environ['OS_USER_DOMAIN_NAME'] = 'Default'
    # os.environ['OS_PROJECT_NAME'] = 'demo'
    # os.environ['OS_USERNAME'] = 'demo'
    # os.environ['OS_PASSWORD'] = 'admin123'
    # os.environ['OS_AUTH_URL'] = 'http://10.22.20.174:35357/v3'
    # os.environ['OS_IDENTITY_API_VERSION'] = '3'
    # os.environ['OS_IMAGE_API_VERSION'] = '2'

    time.sleep(5)

    create_stack(vm1_name, 'client1.yml')
    time.sleep(30)

    create_stack(vm2_name, 'fw.yml')
    time.sleep(30)

    create_stack(vm3_name, 'ha.yml')
    time.sleep(30)

    create_stack(vm4_name, 'client2.yml')
    time.sleep(30)

    create_stack(vm5_name, 'server1.yml')
    time.sleep(30)

    create_stack(vm6_name, 'server2.yml')
    time.sleep(30)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stack_name_1 = show_stack(vm1_name)
    print "stack_name_1: ", stack_name_1

    stack_name_2 = show_stack(vm2_name)
    print "stack_name_2: ", stack_name_2

    stack_name_3 = show_stack(vm3_name)
    print "stack_name_3: ", stack_name_3

    stack_name_4 = show_stack(vm4_name)
    print "stack_name_4: ", stack_name_4

    stack_name_5 = show_stack(vm5_name)
    print "stack_name_5: ", stack_name_5

    stack_name_6 = show_stack(vm6_name)
    print "stack_name_6: ", stack_name_6
    time.sleep(10)

    vm_name.extend([stack_name_1, stack_name_2, stack_name_3, stack_name_4, stack_name_5, stack_name_6])

    #    #KD: The above code can be written like this
    #    stack_name={}
    #    for x in xrange(1, 7):
    #        key = 'stack_name_' + str(x)
    #        vm = 'vm' + str(x) + '_name'
    #        stack_name[key] = show_stack(str(vm)
    #    # to retrieve value
    #    for value in xrange(1, 7)
    #        key = 'stack_name_' + str(value)
    #        print stack_name[key]


    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    op5 = intf_ip(stack_name_1)
    login_ip_vm_1 = op5[0].strip()
    print "login_ip_vm_1: ", login_ip_vm_1

    op3 = intf_ip(stack_name_2)
    print "op3 :: ", op3
    login_ip_vm_2 = op3[0].strip()
    print "login_ip_vm_2: ", login_ip_vm_2

    op4 = intf_ip(stack_name_3)
    print "op4 :: ", op4
    login_ip_vm_3 = op4[0].strip()
    print "login_ip_vm_3: ", login_ip_vm_3

    op13 = intf_ip(stack_name_4)
    login_ip_vm_4 = op13[0].strip()
    print "login_ip_vm_4: ", login_ip_vm_4

    op15 = intf_ip(stack_name_5)
    login_ip_vm_5 = op15[0].strip()
    print "login_ip_vm_5: ", login_ip_vm_5

    op17 = intf_ip(stack_name_6)
    login_ip_vm_6 = op17[0].strip()
    print "login_ip_vm_6: ", login_ip_vm_6

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

    op9 = intf_ip(stack_name_2)
    print "op9 :: ", op9
    configure_ip3_vm_2 = op9[3].strip()
    print "configure_ip3_vm_2: ", configure_ip3_vm_2

    op10 = intf_ip(stack_name_3)
    print "op10 :: ", op10
    configure_ip1_vm_3 = op10[1].strip()
    print "configure_ip1_vm_3: ", configure_ip1_vm_3

    op11 = intf_ip(stack_name_3)
    print "op11 :: ", op11
    configure_ip2_vm_3 = op11[2].strip()
    print "configure_ip2_vm_3: ", configure_ip2_vm_3

    op12 = intf_ip(stack_name_3)
    print "op12 :: ", op12
    configure_ip3_vm_3 = op12[3].strip()
    print "configure_ip3_vm_3: ", configure_ip3_vm_3

    op19 = intf_ip(stack_name_4)
    print "op19 :: ", op19
    configure_ip_vm_4 = op19[1].strip()
    print "configure_ip_vm_4: ", configure_ip_vm_4

    op21 = intf_ip(stack_name_5)
    print "op21 :: ", op21
    configure_ip_vm_5 = op21[1].strip()
    print "configure_ip_vm_5: ", configure_ip_vm_5

    op23 = intf_ip(stack_name_6)
    print "op23 :: ", op23
    configure_ip_vm_6 = op23[1].strip()
    print "configure_ip_vm_6: ", configure_ip_vm_6

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    os.system("> /home/execution/.ssh/known_hosts")

    time.sleep(240)
    print login_ip_vm_1, login_ip_vm_2, login_ip_vm_3, login_ip_vm_4, login_ip_vm_5, login_ip_vm_6, configure_ip_vm_1, \
        configure_ip1_vm_2, configure_ip2_vm_2, configure_ip3_vm_2, configure_ip1_vm_3, configure_ip2_vm_3, \
        configure_ip3_vm_3, configure_ip_vm_4, configure_ip_vm_5, configure_ip_vm_6

    vm_ip.extend(
        [login_ip_vm_1, login_ip_vm_2, login_ip_vm_3, login_ip_vm_4, login_ip_vm_5, login_ip_vm_6, configure_ip_vm_1,
         configure_ip1_vm_2, configure_ip2_vm_2, configure_ip3_vm_2, configure_ip1_vm_3, configure_ip2_vm_3,
         configure_ip3_vm_3, configure_ip_vm_4, configure_ip_vm_5, configure_ip_vm_6])

    vm_detail.extend(
        [login_ip_vm_1, login_ip_vm_2, login_ip_vm_3, login_ip_vm_4, login_ip_vm_5, login_ip_vm_6, configure_ip_vm_1,
         configure_ip1_vm_2, configure_ip2_vm_2, configure_ip3_vm_2, configure_ip1_vm_3, configure_ip2_vm_3,
         configure_ip3_vm_3, configure_ip_vm_4, configure_ip_vm_5, configure_ip_vm_6, stack_name_1, stack_name_2,
         stack_name_3, stack_name_4, stack_name_5, stack_name_6])

    return vm_detail


def test_conf_vm(login_ip1, login_ip2, login_ip3, login_ip4, login_ip5, login_ip6, conf_ip_vm1, conf_ip1_vm2,
                 conf_ip2_vm2, conf_ip3_vm2, conf_ip1_vm3, conf_ip2_vm3, conf_ip3_vm3, conf_ip_vm4, conf_ip_vm5,
                 conf_ip_vm6, vm1_name, vm2_name, vm3_name, vm4_name, vm5_name, vm6_name):

    c1 = SSHConnection(IP=login_ip1, username="mininet", password="mininet")
    #c2 = SSHConnection(IP=login_ip2, username="ubuntu", ssh_key="/home/execution/mykey.pem")
    #c3 = SSHConnection(IP=login_ip3, username="ubuntu", ssh_key="/home/execution/mykey.pem")
    c2 = SSHConnection(IP=login_ip2, username="ubuntu", password="ubuntu")
    c3 = SSHConnection(IP=login_ip3, username="ubuntu", password="ubuntu")
    c4 = SSHConnection(IP=login_ip4, username="mininet", password="mininet")
    c5 = SSHConnection(IP=login_ip5, username="mininet", password="mininet")
    c6 = SSHConnection(IP=login_ip6, username="mininet", password="mininet")
    time.sleep(30)

    con_handle = [c1, c2, c3, c4, c5, c6]

    if c1.connect() and c2.connect() and c3.connect() and c4.connect() and c5.connect() and c6.connect():
        time.sleep(30)
        c2.execute_command("ifconfig -a | grep ^e")
        print "intf detail 2 ::: ", c2.conn.rc.before
        intf_v2 = c2.conn.rc.before
        intf_list_v2 = util_findhost.get_intf(intf_v2)
        print "intf_list_v2 ::: ", intf_list_v2
        time.sleep(5)

        c3.execute_command("ifconfig -a | grep ^e")
        print "intf detail 3 ::: ", c3.conn.rc.before
        intf_v3 = c3.conn.rc.before
        intf_list_v3 = util_findhost.get_intf(intf_v3)
        print "intf_list_v3 ::: ", intf_list_v3
        time.sleep(5)

        vm1_set_eth1 = "sudo ifconfig eth1 " + conf_ip_vm1 + " netmask 255.255.255.0 up"

        vm2_set_eth1 = "sudo ifconfig " + intf_list_v2[1] + " " + conf_ip1_vm2 + " netmask 255.255.255.0 up"
        vm2_set_eth2 = "sudo ifconfig " + intf_list_v2[2] + " " + conf_ip2_vm2 + " netmask 255.255.255.0 up"
        vm2_set_eth3 = "sudo ifconfig " + intf_list_v2[3] + " " + conf_ip3_vm2 + " netmask 255.255.255.0 up"

        vm3_set_eth1 = "sudo ifconfig " + intf_list_v3[1] + " " + conf_ip1_vm3 + " netmask 255.255.255.0 up"
        vm3_set_eth2 = "sudo ifconfig " + intf_list_v3[2] + " " + conf_ip2_vm3 + " netmask 255.255.255.0 up"
        vm3_set_eth3 = "sudo ifconfig " + intf_list_v3[3] + " " + conf_ip3_vm3 + " netmask 255.255.255.0 up"

        vm4_set_eth1 = "sudo ifconfig eth1 " + conf_ip_vm4 + " netmask 255.255.255.0 up"
        vm5_set_eth1 = "sudo ifconfig eth1 " + conf_ip_vm5 + " netmask 255.255.255.0 up"
        vm6_set_eth1 = "sudo ifconfig eth1 " + conf_ip_vm6 + " netmask 255.255.255.0 up"

        for con in con_handle:
            setup_vnf_vm(con)

        time.sleep(5)

        set_intf(c1, vm1_set_eth1)

        set_intf(c2, vm2_set_eth1)
        set_intf(c2, vm2_set_eth2)
        set_intf(c2, vm2_set_eth3)

        set_intf(c3, vm3_set_eth1)
        set_intf(c3, vm3_set_eth2)
        set_intf(c3, vm3_set_eth3)

        set_intf(c4, vm4_set_eth1)

        set_intf(c5, vm5_set_eth1)

        set_intf(c6, vm6_set_eth1)
        time.sleep(5)

        vm1_rt = ["sudo route add -net 192.168.1.0/24 gw " + conf_ip2_vm2,
                  "sudo route add -net 192.168.2.0/24 gw " + conf_ip2_vm2,
                  "sudo route add -net 192.168.3.0/24 gw " + conf_ip2_vm2,
                  "sudo route add -net 192.168.5.0/24 gw " + conf_ip2_vm2]

        vm2_rt = ["sudo route add -net 192.168.2.0/24 gw " + conf_ip1_vm3,
                  "sudo route add -net 192.168.3.0/24 gw " + conf_ip1_vm3,
                  "sudo service fwbuilder restart"]

        vm3_rt = ["sudo route add -net 192.168.4.0/24 gw " + conf_ip1_vm2,
                  "sudo route add -net 192.168.5.0/24 gw " + conf_ip1_vm2]

        vm4_rt = ["sudo route add -net 192.168.1.0/24 gw " + conf_ip3_vm2,
                  "sudo route add -net 192.168.2.0/24 gw " + conf_ip3_vm2,
                  "sudo route add -net 192.168.3.0/24 gw " + conf_ip3_vm2,
                  "sudo route add -net 192.168.4.0/24 gw " + conf_ip3_vm2]

        vm5_rt = ["sudo route add -net 192.168.1.0/24 gw " + conf_ip2_vm3,
                  "sudo route add -net 192.168.3.0/24 gw " + conf_ip2_vm3,
                  "sudo route add -net 192.168.4.0/24 gw " + conf_ip2_vm3,
                  "sudo route add -net 192.168.5.0/24 gw " + conf_ip2_vm3]

        vm6_rt = ["sudo route add -net 192.168.1.0/24 gw " + conf_ip3_vm3,
                  "sudo route add -net 192.168.2.0/24 gw " + conf_ip3_vm3,
                  "sudo route add -net 192.168.4.0/24 gw " + conf_ip3_vm3,
                  "sudo route add -net 192.168.5.0/24 gw " + conf_ip3_vm3]

        for rt in vm1_rt:
            route_add(c1, rt)

        for rt in vm2_rt:
            route_add(c2, rt)

        for rt in vm3_rt:
            route_add(c3, rt)

        for rt in vm4_rt:
            route_add(c4, rt)

        for rt in vm5_rt:
            route_add(c5, rt)

        for rt in vm6_rt:
            route_add(c6, rt)

        add_ip_fwd = ["sudo chmod 777 /etc/sysctl.conf",
                      "sudo sysctl -w net.ipv4.ip_forward=1",
                      "sudo sed -i.bak s/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/g /etc/sysctl.conf"]

        for con1 in con_handle:
            for cmd in add_ip_fwd:
                en_ip_fwd(con1, cmd)


        haproxy_conf = ["sudo chmod 777 /etc/haproxy/haproxy.cfg",
                        "sudo chmod 777 /etc/default/haproxy",
                        "sudo chmod 777 /etc/hosts",
                        "sudo sed -i.bak s/ENABLED=0/ENABLED=1/g /etc/default/haproxy",
                        "sudo sed -i.bak s/server VM1  VM1IP:PORT/server " + vm5_name + "  " + conf_ip_vm5 + ":80/g /etc/haproxy/haproxy.cfg",
                        "sudo sed -i.bak s/server VM2  VM2IP:PORT/server " + vm6_name + "  " + conf_ip_vm6 + ":80/g /etc/haproxy/haproxy.cfg",
                        "sudo sed -i.bak s/bind BINDIP:PORT/bind " + conf_ip1_vm3 + ":80/g /etc/haproxy/haproxy.cfg",
                        "sudo echo " + conf_ip1_vm3 + " " + vm3_name + " >> /etc/hosts",
                        "sudo echo " + conf_ip_vm5 + " " + vm5_name + " >> /etc/hosts",
                        "sudo echo " + conf_ip_vm6 + " " + vm6_name + " >> /etc/hosts",
                        "sudo service haproxy restart"]

        s1_conf = ["sudo chmod 777 /etc/hosts",
                   "sudo chmod 777 /var/www/html/index.html",
                   "sudo echo " + conf_ip1_vm3 + " " + vm3_name + " >> /etc/hosts",
                   "sudo echo " + conf_ip_vm5 + " " + vm5_name + " >> /etc/hosts",
                   "sudo echo " + conf_ip_vm6 + " " + vm6_name + " >> /etc/hosts",
                   "sudo sed -i.bak s/VMNAME:VMIP/" + vm5_name + ":" + conf_ip_vm5 + "/g /var/www/html/index.html",
                   "sudo service networking restart",
                   "sudo service apache2 restart",
                   "sudo ufw allow 80/tcp",
                   "sudo ufw reload"]

        s2_conf = ["sudo chmod 777 /etc/hosts",
                   "sudo chmod 777 /var/www/html/index.html",
                   "sudo echo " + conf_ip1_vm3 + " " + vm3_name + " >> /etc/hosts",
                   "sudo echo " + conf_ip_vm5 + " " + vm5_name + " >> /etc/hosts",
                   "sudo echo " + conf_ip_vm6 + " " + vm6_name + " >> /etc/hosts",
                   "sudo sed -i.bak s/VMNAME:VMIP/" + vm6_name + ":" + conf_ip_vm6 + "/g /var/www/html/index.html",
                   "sudo service networking restart",
                   "sudo service apache2 restart",
                   "sudo ufw allow 80/tcp",
                   "sudo ufw reload"]

        for cmd in haproxy_conf:
            cmd_exec(c3, cmd)

        for cmd in s1_conf:
            cmd_exec(c5, cmd)

        for cmd in s2_conf:
            cmd_exec(c6, cmd)

        c1.disconnect()
        c2.disconnect()
        c3.disconnect()
        c4.disconnect()
        c5.disconnect()
        c6.disconnect()


def get_vm_ip(vm1_name, vm2_name, vm3_name, vm4_name, vm5_name, vm6_name):
    vm_ip = []
    os.environ['OS_PROJECT_DOMAIN_NAME'] = 'Default'
    os.environ['OS_USER_DOMAIN_NAME'] = 'Default'
    os.environ['OS_PROJECT_NAME'] = 'demo'
    os.environ['OS_USERNAME'] = 'demo'
    os.environ['OS_PASSWORD'] = 'rootroot'
    os.environ['OS_AUTH_URL'] = 'http://10.22.20.51:35357/v3'
    os.environ['OS_IDENTITY_API_VERSION'] = '3'
    os.environ['OS_IMAGE_API_VERSION'] = '2'
    time.sleep(5)

    stack_name_1 = show_stack(vm1_name)
    print "stack_name_1: ", stack_name_1

    stack_name_2 = show_stack(vm2_name)
    print "stack_name_2: ", stack_name_2

    stack_name_3 = show_stack(vm3_name)
    print "stack_name_3: ", stack_name_3

    stack_name_4 = show_stack(vm4_name)
    print "stack_name_4: ", stack_name_4

    stack_name_5 = show_stack(vm5_name)
    print "stack_name_5: ", stack_name_5

    stack_name_6 = show_stack(vm6_name)
    print "stack_name_6: ", stack_name_6
    time.sleep(5)

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    op5 = intf_ip(stack_name_1)
    login_ip_vm_1 = op5[0].strip()
    print "login_ip_vm_1: ", login_ip_vm_1

    op3 = intf_ip(stack_name_2)
    print "op3 :: ", op3
    login_ip_vm_2 = op3[0].strip()
    print "login_ip_vm_2: ", login_ip_vm_2

    op4 = intf_ip(stack_name_3)
    print "op4 :: ", op4
    login_ip_vm_3 = op4[0].strip()
    print "login_ip_vm_3: ", login_ip_vm_3

    op13 = intf_ip(stack_name_4)
    login_ip_vm_4 = op13[0].strip()
    print "login_ip_vm_4: ", login_ip_vm_4

    op15 = intf_ip(stack_name_5)
    login_ip_vm_5 = op15[0].strip()
    print "login_ip_vm_5: ", login_ip_vm_5

    op17 = intf_ip(stack_name_6)
    login_ip_vm_6 = op17[0].strip()
    print "login_ip_vm_6: ", login_ip_vm_6

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

    op9 = intf_ip(stack_name_2)
    print "op9 :: ", op9
    configure_ip3_vm_2 = op9[3].strip()
    print "configure_ip3_vm_2: ", configure_ip3_vm_2

    op10 = intf_ip(stack_name_3)
    print "op10 :: ", op10
    configure_ip1_vm_3 = op10[1].strip()
    print "configure_ip1_vm_3: ", configure_ip1_vm_3

    op11 = intf_ip(stack_name_3)
    print "op11 :: ", op11
    configure_ip2_vm_3 = op11[2].strip()
    print "configure_ip2_vm_3: ", configure_ip2_vm_3

    op12 = intf_ip(stack_name_3)
    print "op12 :: ", op12
    configure_ip3_vm_3 = op12[3].strip()
    print "configure_ip3_vm_3: ", configure_ip3_vm_3

    op19 = intf_ip(stack_name_4)
    print "op19 :: ", op19
    configure_ip_vm_4 = op19[1].strip()
    print "configure_ip_vm_4: ", configure_ip_vm_4

    op21 = intf_ip(stack_name_5)
    print "op21 :: ", op21
    configure_ip_vm_5 = op21[1].strip()
    print "configure_ip_vm_5: ", configure_ip_vm_5

    op23 = intf_ip(stack_name_6)
    print "op23 :: ", op23
    configure_ip_vm_6 = op23[1].strip()
    print "configure_ip_vm_6: ", configure_ip_vm_6

    print login_ip_vm_1, login_ip_vm_2, login_ip_vm_3, login_ip_vm_4, login_ip_vm_5, login_ip_vm_6, configure_ip_vm_1, \
        configure_ip1_vm_2, configure_ip2_vm_2, configure_ip3_vm_2, configure_ip1_vm_3, configure_ip2_vm_3, \
        configure_ip3_vm_3, configure_ip_vm_4, configure_ip_vm_5, configure_ip_vm_6

    vm_ip.extend(
        [login_ip_vm_1, login_ip_vm_2, login_ip_vm_3, login_ip_vm_4, login_ip_vm_5, login_ip_vm_6, configure_ip_vm_1,
         configure_ip1_vm_2, configure_ip2_vm_2, configure_ip3_vm_2, configure_ip1_vm_3, configure_ip2_vm_3,
         configure_ip3_vm_3, configure_ip_vm_4, configure_ip_vm_5, configure_ip_vm_6])
    return vm_ip


def test_traffic_icmp_success(login_ip1, login_ip5):
    status = True
    c1 = SSHConnection(IP=login_ip1, username="mininet", password="mininet")
    c5 = SSHConnection(IP=login_ip5, username="mininet", password="mininet")
    if c1.connect() and c5.connect():
        c5.execute_command("ifconfig ens4")
        eth1_detail = c5.conn.rc.before
        c5_eth1_ip = util_findhost.search_host(eth1_detail)
        print "c5_eth1_ip :", c5_eth1_ip
        cmd = "ping -c 3 " + c5_eth1_ip
        pat = "0% packet loss"
        check1 = run_check_cmd(c1, cmd, pat)
        print "the value of icmp check1 is:", check1
        if check1:
            print "Verification of Ping test before disabling icmp -- Successful"
        else:
            status = False
            print "Verification of Ping test before disabling icmp -- Failed."

        c1.disconnect()
        c5.disconnect()
        return status


def test_traffic_icmp_failure(login_ip1, login_ip5):
    status = True
    print "After Blocking ICMP Traffic in FW-Builder"
    c1 = SSHConnection(IP=login_ip1, username="mininet", password="mininet")
    c5 = SSHConnection(IP=login_ip5, username="mininet", password="mininet")
    if c1.connect() and c5.connect():
        c5.execute_command("ifconfig ens4")
        eth1_detail = c5.conn.rc.before
        c5_ens4_ip = util_findhost.search_host(eth1_detail)
        print "c5_ens4_ip :", c5_ens4_ip
        cmd = "ping -c 3 " + c5_ens4_ip
        pat = "100% packet loss"
        check2 = run_check_cmd(c1, cmd, pat)
        print "the value of icmp check2 is:", check2
        if check2:
            print "Verification of Ping test after disabling icmp -- Successful"
        else:
            status = False
            print "Verification of Ping test after disabling icmp -- Failed."
        c1.disconnect()
        c5.disconnect()
        return status


def test_traffic_http_success(login_ip1, login_ip5):
    status = True
    c1 = SSHConnection(IP=login_ip1, username="mininet", password="mininet")
    c5 = SSHConnection(IP=login_ip5, username="mininet", password="mininet")
    if c1.connect() and c5.connect():
        c5.execute_command("ifconfig ens4")
        eth1_detail = c5.conn.rc.before
        c5_eth1_ip = util_findhost.search_host(eth1_detail)

        c1.execute_command("ifconfig ens4")
        eth1_detail = c1.conn.rc.before
        c1_eth1_ip = util_findhost.search_host(eth1_detail)

        print "c5_eth1_ip :", c5_eth1_ip
        cmd = "i=0; while [ $i -lt 10 ]; do wget http://" + c5_eth1_ip + ";sleep 1; $i=$i+1;done"
        #pat = "HTTP request sent, awaiting response... 200 OK"
        pat = "200 OK"

        cmd1 = 'sudo tcpdump -nqt -s 0 -A -i ens4 port 80 | grep "IP ' + c1_eth1_ip + '"'
        pat1 = c1_eth1_ip
        check1 = run_check_cmd(c1, cmd, pat)
        check2 = run_check_cmd(c5, cmd1, pat1)
        if check1 and check2:
            print "Verification of traffic test before disabling http -- Successful"
        else:
            status = False
            print "Verification of traffic test before disabling icmp -- Failed."
        c1.disconnect()
        c5.disconnect()
        return status


def test_traffic_http_failure(login_ip1, login_ip5):
    status = True
    print "After Blocking HTTP Traffic in FW-Builder"
    c1 = SSHConnection(IP=login_ip1, username="mininet", password="mininet")
    c5 = SSHConnection(IP=login_ip5, username="mininet", password="mininet")
    if c1.connect() and c5.connect():
        c5.execute_command("ifconfig ens4")
        eth1_detail = c5.conn.rc.before
        c5_eth1_ip = util_findhost.search_host(eth1_detail)

        c1.execute_command("ifconfig ens4")
        eth1_detail = c1.conn.rc.before
        c1_eth1_ip = util_findhost.search_host(eth1_detail)

        print "c5_eth1_ip :", c5_eth1_ip
        #cmd = "i=0; while [ $i -lt 10 ]; do wget http://" + c5_eth1_ip + ";sleep 1; $i=$i+1;done"
        cmd = "wget http://" + c5_eth1_ip
        print "cmd",cmd
        #pat = "HTTP request sent, awaiting response... 200 OK"
        pat = "200 OK"
        cmd1 = 'sudo tcpdump -nqt -s 0 -A -i ens4 port 80 | grep "IP ' + c1_eth1_ip + '"'
        pat1 = c1_eth1_ip
        check1 = run_nt_check_cmd(c1, cmd, pat)
        print "check1", check1

        check2 = run_nt_check_cmd(c5, cmd1, pat1)
        print "check2", check2
        if check1 and check2:
            print "Verification of traffic test after disabling http -- Successful"
        else:
            status = False
            print "Verification of traffic test after disabling http -- Failed."
        c1.disconnect()
        c5.disconnect()
        return status


def test_load_balance(login_ip1, login_ip3, login_ip5, login_ip6):
    status = True
    print "Load balancing on HAPROXY"
    c1 = SSHConnection(IP=login_ip1, username="mininet", password="mininet")
    c3 = SSHConnection(IP=login_ip3, username="ubuntu", password="ubuntu")
    c5 = SSHConnection(IP=login_ip5, username="mininet", password="mininet")
    c6 = SSHConnection(IP=login_ip6, username="mininet", password="mininet")

    if c1.connect() and c3.connect() and c5.connect() and c6.connect():
        c1.execute_command("ifconfig ens4")
        eth1_detail = c1.conn.rc.before
        c1_eth1_ip = util_findhost.search_host(eth1_detail)

        c3.execute_command("ifconfig ens4")
        ens4_detail = c3.conn.rc.before
        c3_ens4_ip = util_findhost.search_host(ens4_detail)

        c3.execute_command("ifconfig ens5")
        ens5_detail = c3.conn.rc.before
        c3_ens5_ip = util_findhost.search_host(ens5_detail)

        c3.execute_command("ifconfig ens6")
        ens6_detail = c3.conn.rc.before
        c3_ens6_ip = util_findhost.search_host(ens6_detail)

        c5.execute_command("ifconfig ens4")
        eth1_detail = c5.conn.rc.before
        c5_eth1_ip = util_findhost.search_host(eth1_detail)

        c6.execute_command("ifconfig ens4")
        eth1_detail = c6.conn.rc.before
        c6_eth1_ip = util_findhost.search_host(eth1_detail)

        print "c1_eth1_ip:", c1_eth1_ip
        print "c3_ens4_ip:", c3_ens4_ip
        print "c3_ens5_ip:", c3_ens5_ip
        print "c3_ens6_ip:", c3_ens6_ip
        print "c5_eth1_ip:", c5_eth1_ip
        print "c6_eth1_ip:", c6_eth1_ip

        cmd = "i=0; while [ $i -lt 10 ]; do wget http://" + c3_ens4_ip + ";sleep 1; $i=$i+1;done"
        #cmd = "i=0; while [ $i -lt 10 ]; do curl http://" + c3_ens4_ip + ";sleep 1; $i=$i+1;done"
        pat = "HTTP request sent, awaiting response... 200 OK"
        #pat = "index.html*"

        cmd1 = 'sudo tcpdump -nqt -s 0 -A -i ens4 port 80 | grep "IP ' + c3_ens5_ip + '"'
        pat1 = "IP " + c3_ens5_ip + ""

        cmd2 = 'sudo tcpdump -nqt -s 0 -A -i ens4 port 80 | grep "IP ' + c3_ens6_ip + '"'
        pat2 = "IP " + c3_ens6_ip + ""

        check1 = run_check_cmd(c1, cmd, pat)
        check2 = run_check_cmd(c5, cmd1, pat1)
        check3 = run_check_cmd(c6, cmd2, pat2)

        print "pat:", pat
        print "pat1:", pat1
        print "pat2:", pat2

        print "check1:", check1
        print "check2:", check2
        print "check3:", check3
        if check1 and check2 and check3:
        #if check2 and check3:
            print "Verification of load balancing traffic test completed -- Successful"
        else:
            status = False
            print "Verification of load balancing traffic test not complete -- Failed."
        c1.disconnect()
        c3.disconnect()
        c5.disconnect()
        c6.disconnect()
        return status


def test_traffic_ftp_success(login_ip1, login_ip5):
    status = True
    print "FTP traffic testing"
    c1 = SSHConnection(IP=login_ip1, username="mininet", password="mininet")
    c5 = SSHConnection(IP=login_ip5, username="mininet", password="mininet")


    if c1.connect() and c5.connect():
        c1.execute_command("ifconfig ens4")
        eth1_detail = c1.conn.rc.before
        c1_eth1_ip = util_findhost.search_host(eth1_detail)

        c5.execute_command("ifconfig ens4")
        eth1_detail = c5.conn.rc.before
        c5_eth1_ip = util_findhost.search_host(eth1_detail)
        print "c1_eth1_ip:", c1_eth1_ip
        print "c5_eth1_ip:", c5_eth1_ip

        cmd = "sh a.sh"
        # pat = "HTTP request sent, awaiting response... 200 OK"
        pat = "*transferred*"

        cmd1 = 'sudo tcpdump -nqt -s 0 -A -i eth1 port 21 | grep "IP ' + c1_eth1_ip + '"'
        pat1 = "IP "+ c1_eth1_ip

        check1 = run_check_cmd(c1, cmd, pat)
        check2 = run_check_cmd(c5, cmd1, pat1)
        #check3 = run_nt_check_cmd(c6, cmd2, pat2)

        print "check1:", check1
        print "check2:", check2
        #print "check3:", check3
        if check1 and check2:
            print "Verification of ftp traffic test completed -- Successful"
        else:
            status = False
            print "Verification of ftp traffic test not complete -- Failed."
        c1.disconnect()
        c5.disconnect()
        return status


def test_traffic_telnet_success(login_ip1, login_ip5):
    status = True
    print "Telnet traffic testing"
    c1 = SSHConnection(IP=login_ip1, username="mininet", password="mininet")
    c5 = SSHConnection(IP=login_ip5, username="mininet", password="mininet")


    if c1.connect() and c5.connect():
        c1.execute_command("ifconfig ens4")
        eth1_detail = c1.conn.rc.before
        c1_eth1_ip = util_findhost.search_host(eth1_detail)
        #c1.execute_command("sudo sh -c 'echo 'telnet stream tcp nowait telnetd /usr/sbin/tcpd /usr/sbin/in.telnetd' >> /etc/inetd.conf''")
        c1.execute_command("sudo /etc/init.d/xinetd restart")

        c5.execute_command("ifconfig ens4")
        eth1_detail = c5.conn.rc.before
        c5_eth1_ip = util_findhost.search_host(eth1_detail)
        #c5.execute_command("sudo sh -c 'echo 'telnet stream tcp nowait telnetd /usr/sbin/tcpd /usr/sbin/in.telnetd' >> '/etc/inetd.conf''")
        c5.execute_command("sudo /etc/init.d/xinetd restart")

        cmd5 = 'sudo tcpdump -nqt -s 0 -A -i eth1 port 23 | grep "IP ' + c1_eth1_ip + '"'
        pat5 = "IP " + c1_eth1_ip

        c1.execute_command("telnet " + c5_eth1_ip)
        if c1.conn.rc.before.find(":") != -1:
            c1.execute_command("mininet")
            if c1.conn.rc.before.find(":") != -1:
                c1.execute_command("mininet")
        time.sleep(2)
        c5.execute_command(cmd5)
        time.sleep(5)
        if c5.conn.rc.before.find(pat5) != -1:
            print "SUCCESS"
        else:
            status = False
            print "FAILED"

        c1.disconnect()
        c5.disconnect()
        return status



def install_devstack(IP, username, password):
    loc_content = """[[local|localrc]]
    ADMIN_PASSWORD=admin123
    DATABASE_PASSWORD=$ADMIN_PASSWORD
    RABBIT_PASSWORD=$ADMIN_PASSWORD
    SERVICE_PASSWORD=$ADMIN_PASSWORD
    NOVNC_BRANCH=v0.6.0

    enable_service h-eng h-api h-api-cfn h-api-cw
    enable_plugin heat https://git.openstack.org/openstack/heat stable/newton """

    SSH_NEWKEY = 'Are you sure you want to continue connecting'
    file_new = open(r"/home/stack/local.conf", "w+")
    file_new.write(loc_content)
    file_new.close()
    try:
        connection = SSHConnection(IP=IP, username=username, password=password)
        if connection.connect():
            connection.conn.rc.sendline("sudo chmod -R 777 /home/stack")
            connection.conn.rc.sendline("sudo apt-get install -y git")
            connection.conn.rc.sendline("sudo echo \"nameserver 8.8.8.8\" >> /etc/resolv.conf")
            connection.conn.rc.sendline("git clone https://git.openstack.org/openstack-dev/devstack -b stable/newton")
            time.sleep(60)
            connection.conn.rc.sendline("sudo pip install appdirs --upgrade")
            connection.conn.rc.sendline("cd devstack")
            connection.conn.rc.sendline("sudo chmod -R 777 /home/stack")
            connection.conn.rc.sendline("sudo chmod -R 777 /home/stack/*.*")
            connection.conn.rc.sendline("cp /home/stack/local.conf .")
            i = connection.conn.rc.expect([SSH_NEWKEY, 'password:', pexpect.EOF])
            if i == 0:
                connection.conn.rc.sendline('yes')
                i = connection.conn.rc.expect([SSH_NEWKEY, 'password:', pexpect.EOF])
            else:
                pass
            connection.conn.rc.sendline(password)
            connection.conn.rc.sendline("nohup ./stack.sh &")
            time.sleep(4800)
            connection.conn.rc.logout()
    except pxssh.ExceptionPxssh, e:
        print "pxssh failed on login."
        print str(e)




def test_complete():
    pass



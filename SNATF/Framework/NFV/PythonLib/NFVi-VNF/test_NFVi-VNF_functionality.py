import test_vnf

vm1 = 'client1'
vm2 = 'fw'
vm3 = 'ha'
vm4 = 'client2'
vm5 = 'server1'
vm6 = 'server2'
install_ip = "10.22.20.51"
user = "execution"
pswd = "execution"


# Installation of Devstack
#test_vnf.install_devstack(install_ip, user, pswd)


# Devstack VM Infrastructure set up
#vm_ip, vm_name = test_vnf.vnf_infrastructure_setup(vm1, vm2, vm3, vm4, vm5, vm6)
#print "vm_ip: ", vm_ip
#print "vm_name: ", vm_name
#vm_name=['server','client1', 'fw', 'ha', 'client2', 'server1','server2']
#vm_ip=['172.24.4.4', '172.24.4.7', '172.24.4.11', '172.24.4.2', '172.24.4.14', '172.24.4.12', '192.168.4.12', '192.168.1.6', '192.168.4.4', '192.168.5.5', '192.168.1.8', '192.168.2.11', '192.168.3.4', '192.168.5.11', '192.168.2.4', '192.168.3.11']

# VM Configuration
#status1 = test_vnf.test_conf_vm(vm_ip[0], vm_ip[1], vm_ip[2], vm_ip[3], vm_ip[4], vm_ip[5], vm_ip[6], vm_ip[7],
 #                                vm_ip[8], vm_ip[9], vm_ip[10], vm_ip[11], vm_ip[12], vm_ip[13], vm_ip[14], vm_ip[15],
  #                               vm_name[1], vm_name[2], vm_name[3], vm_name[4], vm_name[5], vm_name[6])

# Get VM IP
#ipset = test_vnf.get_vm_ip(vm1, vm2, vm3, vm4, vm5, vm6)

#print "ipset: ", ipset

ipset=['172.24.4.4', '172.24.4.7', '172.24.4.11', '172.24.4.2', '172.24.4.14', '172.24.4.12', '192.168.4.12', '192.168.1.10', '192.168.4.3', '192.168.5.12', '192.168.1.8', '192.168.2.11', '192.168.3.4', '192.168.5.11', '192.168.2.4', '192.168.3.11']

# Check ICMP Success
#status3 = test_vnf.test_traffic_icmp_success(ipset[0], ipset[4])

# Check ICMP Failure
#status4 = test_vnf.test_traffic_icmp_failure(ipset[0], ipset[4])

# Check HTTP Success
# status5 = test_vnf.test_traffic_http_success(ipset[0], ipset[4])

#Check HTTP Failure
status6 = test_vnf.test_traffic_http_failure(ipset[0], ipset[4])

# Check Load Balance Success
#status7 = test_vnf.test_load_balance(ipset[0], ipset[2], ipset[4], ipset[5])

# Check FTP Traffic
#status8 = test_vnf.test_traffic_ftp_success(ipset[0], ipset[4])
# status9 = test_vnf.test_traffic_telnet_success(ipset[0],ipset[4])


# if status1 and status3 and status4 and status5 and status6 and status7 and status8:
# if status9:
#     print "All Tests Successfully PASSED"

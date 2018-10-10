import os

### Mandatory Parameters ###
devstack_ip      = '192.168.203.6'
devstack_user    = 'testpc'
devstack_pass    = 'test123'
devstack_version = 'ocata'

public_key = "loginkey"
public_nw  = "net_mngt"
flavor     = "ds1G"
ug_flavor  = "m1.small"
username   = "cirros"
password   = "cubswin:)"
key_loc    = "/home/testpc/automation/rmaity/test_demo/"
auth       = "/home/testpc/automation/rmaity/test_demo/admin-openrc"

image_file    = "/home/testpc/automation/rmaity/test_demo/image/cirros-0.3.5-x86_64-disk.img"
image_name    = "cirros_test"
#base_image = "ubuntu_test"
#base_image = "LxCIPtable"
base_image = "cirros_test"
base_image2 = "ubuntu_r"
upgrade_image = "ubuntu_r"

### Optional Parameters ###

#Yaml files
yaml_loc   = "/home/testpc/automation/rmaity/test_demo/yaml/"
yaml_name  = "ubuntu_oneNW.yml"
yaml2_name = "ubuntu_multiNW.yml"
yaml3_name = "ubuntu_multiserver.yml"

snap_yaml_name = "ubuntu_snap.yml"
ug_yaml_name   = "ug_ubuntu_multiNW.yml"
dg_yaml_name   = "dg_ubuntu_multiNW.yml"

#Stack Names
stack_name  = "single_stack_vm"
stack2_name = "multinw_stack_vm"
stack3_name = "multi_stack_vm"
snap_stack_name = "multinw_snap_stack_vm"

snapshot_name  = "snap_image"
network_name   = "net001"
network_name2  = "net002"
network_subnet   = "11.1.1.0/24"
network_subnet2  = "11.2.1.0/24"
mgmt_subnet      = "20.1.1.0/24"
floating_ip_nw   = "public"
public_net_subnet   = "192.168.203.0/26"
ip_alloc_pool_start = "192.168.203.35"
ip_alloc_pool_end   = "192.168.203.42"
sec_name = "open"
router_name = "router1"



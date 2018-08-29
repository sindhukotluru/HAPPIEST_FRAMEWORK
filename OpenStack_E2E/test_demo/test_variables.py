import os

### Mandatory Parameters ###
stack_ip      = '192.168.203.6'
stack_user    = 'testpc'
stack_pass    = 'test123'
stack_version = 'ocata'

public_key = "loginkey"
public_nw  = "public"
mgmt_nw    = "net_mngt"
sec_name   = "open"
router_name= "router1"
flavor     = "m1.medium"
ug_flavor  = "m1.large"
username   = "ubuntu"
password   = "ubuntu"
key_loc    = "/home/testpc/automation/rmaity/test_demo/robot/suite/vnf/"
auth       = "/home/testpc/automation/rmaity/test_demo/admin-openrc"

image_file    = "/home/testpc/automation/rmaity/test_demo/image/xenial-server-cloudimg-amd64-disk1.img"
image_file2    = "/home/testpc/automation/rmaity/test_demo/image/trusty-server-cloudimg-amd64-disk1.img"
image_name    = "ubuntu.16.04"
#base_image    = "ubuntu.16.04"
dgrade_image  = "ubuntu.14.04"

### Optional Parameters ###

#Yaml files
yaml_loc   = "/home/testpc/automation/rmaity/test_demo/yaml/"
yaml_name  = "ubuntu_oneNW.yml"
yaml2_name = "ubuntu_multiNW.yml"
yaml3_name = "ubuntu_multiserver.yml"
yaml4_name = "ospf.yml"

snap_yaml_name = "ubuntu_snap.yml"
ug_yaml_name   = "ug_ubuntu_multiNW.yml"
dg_yaml_name   = "dg_ubuntu_multiNW.yml"

#Stack Names
stack_name  = "single_stack_vm"
stack2_name = "multinw_stack_vm"
stack3_name = "multi_stack_vm"
stack4_name = "stack"
snap_stack_name = "multinw_snap_stack_vm"

snapshot_name  = "snap_image"
network_name   = "net001"
network_name2  = "net002"
network_name3  = "net003"
network_subnet   = "20.1.1.0/24"
network_subnet2  = "10.1.1.0/24"
network_subnet3  = "40.1.1.0/24"
mgmt_subnet      = "10.10.10.0/24"
public_net_subnet   = "192.168.203.0/26"
ip_alloc_pool_start = "192.168.203.35"
ip_alloc_pool_end   = "192.168.203.42"



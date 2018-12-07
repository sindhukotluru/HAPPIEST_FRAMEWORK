import os

### Mandatory Parameters ###

public_key = "loginkey"
public_nw  = "net_mngt"
flavor     = "20gb"
ug_flavor  = "30gb"
username   = "ubuntu"
password   = "ubuntu"
key_loc    = "/home/testpc/automation/rmaity/test_demo/"
auth       = "/home/testpc/automation/rmaity/test_demo/admin-openrc"

image_file    = "/home/testpc/automation/rmaity/test_demo/image/ubuntu-16.04-server-cloudimg-amd64-disk1.img"
image_name    = "test_image_qcow2"
base_image = "ubuntu_qcow2"
#base_image = "LxCIPtable"
#base_image = "snort"
base_image1 = "ubuntu_vhd"
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

snapshot_name = "snap_image"
network_name  = "net001"
network_name2  = "net002"
network_subnet  = "11.1.1.0/24"
network_subnet2  = "11.2.1.0/24"




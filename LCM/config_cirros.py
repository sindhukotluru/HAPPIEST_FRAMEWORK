import os

### Mandatory Parameters ###

public_key = "loginkey"
public_nw  = "net_mngt"
flavor     = "512mb"
ug_flavor  = "30gb"
username   = "cirros"
password   = "ubuntu"
path       = "/home/testpc/"
key_loc    = path + "/g/LCM/"
auth       = path + "g/LCM/admin-openrc"
#key_loc    = "~/g/LCM/"
#auth       = "~/g/LCM/admin-openrc"

image_file    = path + "g/LCM/image/cirros-0.3.5-x86_64-disk.img"
image_name    = "cirros_test"
#base_image = "ubuntu_test"
#base_image = "LxCIPtable"
base_image = "cirros_test"
base_image2 = "ubuntu_r"
upgrade_image = "ubuntu_r"

### Optional Parameters ###

#Yaml files
yaml_loc   = path + "g/LCM/yaml/"
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

"""
This Config file is specific to place OVS related input
This file is updated with new fields & values
"""

# Flow level inputs
priority = [500,1000,1500,2000]
ip_addr = ['192.168.1.10','192.168.2.10']           #src & dst pair
mac_addr = ['00:00:00:00:00:01','00:00:00:00:00:02']  #src & dst pair
ports = [1,2]

flow_inputs = {'Pri':'priority', 'iPort':'in_port', 's_Mac':'dl_src', 'd_Mac':'dl_dst','s_Nw':'nw_src','d_Nw':'nw_dst','type':'dl_type', 'Proto':'nw_proto', 'Protocol':'protocol'}  #Keep on update with rest of when any new fileds will be seen further

flow_actions = ['output','flood','drop','normal','mod_nw_tos']   #Keep on update with rest of when any new fileds will be seen further







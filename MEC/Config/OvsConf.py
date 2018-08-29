"""
This Config file is specific to place OVS related input
This file is updated with new fields & values
"""

# Flow level inputs
priority = [500,1000,1500,2000]
ip_addr = ['33.33.33.0/24','44.44.44.0/24']           #src & dst pair
mac_addr = ['12:34:56:78:90:01','21:43:65:87:09:02']  #src & dst pair
ports =[100,200]
vlans = [555,777,999]
flow_inputs = {'Pri':'priority', 'iPort':'in_port', 's_Mac':'dl_src', 'd_Mac':'dl_dst','s_Nw':'nw_src','d_Nw':'nw_dst','type':'dl_type', 'Proto':'nw_proto', 'Protocol':'protocol'}  #Keep on update with rest of when any new fileds will be seen further

flow_actions = ['output','flood','drop','NORMAL','mod_nw_tos']   #Keep on update with rest of when any new fileds will be seen further







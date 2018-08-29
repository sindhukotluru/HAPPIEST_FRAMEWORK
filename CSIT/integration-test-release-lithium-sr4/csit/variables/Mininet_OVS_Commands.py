"""
Definitions of common commands in Mininet and OVS for the system test robot suites of the
OpenDaylight project.

Authors: Sunil.Maganahalli
Edited: Many times by many people
"""

# Commands from System Prompt

# Commands from Mininet Prompt
DUMP_FLOWS_OF13 = 'dpctl dump-flows -O OpenFlow13'
DUMP_GROUPS_OF13 = 'dpctl dump-groups -O OpenFlow13'
OVS_SET_MANAGER = 'sudo ovs-vsctl set-manager ptcp:6644'



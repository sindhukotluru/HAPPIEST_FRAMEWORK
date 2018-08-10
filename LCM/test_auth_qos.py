from orch_lib import *
import sys
from random import randint

stack_name = ['Stack_Single', 'Stack_multiNW','Multi_Stack']
yaml_name = ['ubuntu_oneNW.yml','ubuntu_multiNW.yml','multi_stack.yml']

new_snap_yaml = 'ubuntu_snap.yml'
new_ug_yaml = 'ubuntu_ug.yml'
new_dg_yaml = 'ubuntu_multiNW.yml'
snapshot_name = 'StackSnap' + stack_name[1]

image_name = 'test_cirros'
network_name = 'test_nw'
if (delete_stack_test(stack_name[0])):
    print ("SUCCESS: Stack %s deleted successfully" % stack_name[0])
else:
    print ("FAILED: Stack %s deleted failed; exiting test!!" % stack_name[0])

if (create_stack_test(stack_name[0], yaml_name[0])):
    print ("SUCCESS: Stack %s created successfully" %stack_name[0])
else:
    print ("FAILED: Stack %s creation failed; exiting test!!" %stack_name[0])
    # sys.exit()

if (delete_stack_test(stack_name[0])):
    print ("SUCCESS: Stack %s deleted successfully" % stack_name[0])
else:
    print ("FAILED: Stack %s deleted failed; exiting test!!" % stack_name[0])
    # sys.exit()

if (create_stack_multi_network_test(stack_name[1], yaml_name[1])):
    print ("SUCCESS: Multi network stack %s creation successfully" %stack_name[1])
else:
    print ("FAILED: Multi network stack %s creation failed!!" %stack_name[1])
    # sys.exit()

if (create_snapshot_test(stack_name[1], snapshot_name)):
    print ("SUCCESS: Server snapshot %s creation successfully" %stack_name[1])
else:
    print ("FAILED: Server snapshot %s creation failed!!" %stack_name[1])
    # sys.exit()

if (delete_stack_test(stack_name[1])):
    print ("SUCCESS: Stack %s deleted successfully" % stack_name[1])
else:
    print ("FAILED: Stack %s deleted failed; exiting test!!" % stack_name[1])
    # sys.exit()

if (create_stack_with_snapshot_test(stack_name[1], new_snap_yaml)):
    print ("SUCCESS: Stack %s with snapshot %s created successfully" %(stack_name[1], snapshot_name))
else:
    print ("FAILED: Stack %s with snapshot %s creation failed" %(stack_name[1], snapshot_name))

if (upgrade_stack_test(stack_name, new_ug_yaml)):
    print ("SUCCESS: Stack %s upgraded successfully" %stack_name[1])
else:
    print ("FAILED: Stack %s upgradation print failed!!" %stack_name[1])

if (downgrade_stack_test(stack_name, new_dg_yaml)):
    print ("SUCCESS: Stack %s downgraded successfully" %stack_name[1])
else:
    print ("FAILED: Stack %s downgrade failed!!" %stack_name[1])

if (delete_snapshot_test(snapshot_name)):
   print ("SUCCESS: snapshot %s deletion successfully" %snapshot_name)
else:
   print ("FAILED: snapshot %s deletion failed!!" %snapshot_name)
  
if (soft_reboot_stack_test(stack_name[1])):
    print ("SUCCESS: Stack %s soft reboot successfully" %stack_name[1])
else:
    print ("FAILED: Stack %s soft reboot failed!!" %stack_name[1])

if (delete_stack_test(stack_name[1])):
   print ("SUCCESS: Stack %s deletion successfully" %stack_name[1])
else:
   print ("FAILED: server %s deletion failed!!" %stack_name[1])

if (pause_server_test(stack_name[1])):
   print ("SUCCESS: Stack %s soft reboot successfully" %stack_name[1])
else:
   print ("FAILED: Stack %s soft reboot failed!!" %stack_name[1])

if (unpause_server_test(stack_name[1])):
   print ("SUCCESS: Server %s pause successfully" %stack_name[1])
else:
   print ("FAILED: Server %s pause failed!!" %stack_name[1])

if (suspend_server_test(stack_name[1])):
   print ("SUCCESS: Server %s suspend successfully" %stack_name[1])
else:
   print ("FAILED: Server %s suspend failed!!" %stack_name[1])

if (resume_server_test(stack_name[1])):
   print ("SUCCESS: Server %s resume successfully" %stack_name[1])
else:
   print ("FAILED: Server %s resume failed!!" %stack_name[1])

if (hard_reboot_server_test(stack_name[1])):
   print ("SUCCESS: Stack %s hard reboot successfully" %stack_name[1])
else:
   print ("FAILED: Stack %s hard reboot failed!!" %stack_name[1])

if (delete_server_test(stack_name[1])):
   print ("SUCCESS: server %s deletion successfully" %stack_name[1])
else:
   print ("FAILED: server %s deletion failed!!" %stack_name[1])

if (create_stack_multi_network_multi_server_test(stack_name[2], yaml_name[2])):
    print ("SUCCESS: Multi network stack %s creation successfully" %stack_name[2])
else:
    print ("FAILED: Multi network stack %s creation failed!!" %stack_name[2])
    # sys.exit()

if (soft_reboot_stack_multi_network_test(stack_name[2])):
    print ("SUCCESS: Stack %s soft reboot successfully" %stack_name[2])
else:
    print ("FAILED: Stack %s soft reboot failed!!" %stack_name[2])

if (delete_stack_multi_server_test(stack_name[2])):
   print ("SUCCESS: Stack %s deletion successfully" %stack_name[2])
else:
   print ("FAILED: server %s deletion failed!!" %stack_name[2])

'''
if (create_image_test(image_name)):
    print ("SUCCESS: Image %s created successfully" %image_name)
else:
    print ("FAILED: Image %s creation failed!!" %image_name)

if (delete_image_test(image_name)):
    print ("SUCCESS: Image %s deleted successfully" % image_name)
else:
    print ("FAILED: Image %s deleted failed!!" % image_name)

if (create_network_test(network_name)):
    print ("SUCCESS: Network %s created successfully" %network_name)
else:
    print ("FAILED: Network %s creation failed!!" %network_name)

if (delete_network_test(network_name)):
    print ("SUCCESS: Network %s deleted successfully" % network_name)
else:
    print ("FAILED: Network %s deleted failed!!" % network_name)
'''



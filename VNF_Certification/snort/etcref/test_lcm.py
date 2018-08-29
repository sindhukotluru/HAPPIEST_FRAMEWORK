from lcm_library import *
import sys
from random import randint

suffix = str(randint(100,999))
stack_name = 'Stack' + suffix
snapshot_name = 'StackSnap' + suffix

if (vnf_create_instance(stack_name)):
   print "SUCCESS: stack created successfully"
else:
   print "stack creation failed; exiting test!!"
   sys.exit()
'''
if (vnf_create_instance_multinet('multi'+stack_name)):
   print "SUCCESS: multi network stack creation/validation/deletion successfully"
else:
   print "multi network stack creation/validation/deletion failed!!"
   sys.exit()

if (vnf_upgrade_instance(stack_name)):
   print "SUCCESS: stack upgraded successfully"
else:
   print "stack upgradation failed"

if (vnf_downgrade_instance(stack_name)):
   print "SUCCESS: stack downgraded successfully"
else:
   print "stack downgradation failed"

if (vnf_soft_reboot_server(stack_name)):
   print "SUCCESS: stack soft reboot successful"
else:
   print "stack soft reboot failed!!"

if (vnf_hard_reboot_server(stack_name)):
   print "SUCCESS: stack hard reboot successful"
else:
   print "stack hard reboot failed!!"
   
if (vnf_create_snapshot(stack_name, snapshot_name)):
   print "SUCCESS: server snapshot creation successful"
else:
   print "server snapshot creation failed!!"
   
if (vnf_delete_snapshot(snapshot_name)):
   print "SUCCESS: snapshot deletion successful"
else:
   print "snapshot deletion failed!!"
   
if (vnf_pause_server(stack_name)):
   print "SUCCESS: stack soft reboot successful"
else:
   print "stack soft reboot failed!!"
   
if (vnf_unpause_server(stack_name)):
   print "SUCCESS: server pause successful"
else:
   print "server pause failed!!"

if (vnf_suspend_server(stack_name)):
   print "SUCCESS: server suspend successful"
else:
   print "server suspend failed!!"
   
if (vnf_resume_server(stack_name)):
   print "SUCCESS: server resume successful"
else:
   print "server resume failed!!"
#if (vnf_migrate_server(stack_name)):
#   print "SUCCESS: server migration successful"
#else:
#   print "server migration failed!!"
#   
#if (vnf_live_migrate_server(stack_name)):
#   print "SUCCESS: server live migration successful"
#else:
#   print "server live migration failed!!"
if (vnf_delete_server(stack_name)):
   print "SUCCESS: server deletion successful"
else:
   print "server deletion failed!!"
   
if (vnf_delete_stack(stack_name)):
   print "SUCCESS: stack deletion successful"
else:
   print "server deletion failed!!"   
'''

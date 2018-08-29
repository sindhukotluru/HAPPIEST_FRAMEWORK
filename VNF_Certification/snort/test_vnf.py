from vnf_library import *
import sys
from random import randint

suffix = str(randint(100,999))
#stack_name = 'Stack' + suffix
stack_name = 'Stack123'
#stack_name = 'Stack557'
#snapshot_name = 'StackSnap' + suffix

if (vnf_create_multistack(stack_name)):
   print "SUCCESS: stack created successfully"
else:
   print "stack creation failed; exiting test!!"
   sys.exit()

if (vnf_allow_icmp_test(stack_name)):
   print "SUCCESS: icmp test successful"
else:
   print "icmp test failed"

#if (vnf_icmp_alldrop_test(stack_name)):
#   print "SUCCESS: icmp blcok successful"
#else:
#   print "icmp block failed"

#if (vnf_block_icmp_test(stack_name)):
#   print "SUCCESS: icmp test successful"
#else:
#   print "icmp test failed"

#if (vnf_http_allow_test(stack_name)):
#   print "SUCCESS: http test successful"
#else:
#   print "http test failed"

#if (vnf_http_block_test(stack_name)):
#   print "SUCCESS: http test successful"
#else:
#   print "http test failed"


#if (vnf_inline_test(stack_name)):
#   print "SUCCESS: INLINE MODE ACTIVATED"
#else:
#   print "Failed to fetch mode info"

#if (vnf_sniffer_test(stack_name)):
#   print "SUCCESS: SNIFFER MODE ACTIVATION SUCCESSFUL"
#else:
#   print "Failed to fetch mode info"

#if (vnf_ssh_test(stack_name)):
#   print "SUCCESS: SSH CONNECTION SUCCESSFULLY BLOCKED"
#else:
#   print "Failed to fetch mode info"

#if (vnf_malware_test(stack_name)):
#   print "SUCCESS: Malware Detected Connection Blocked"
#else:
#   print "Failed to block malware"

#if (vnf_pkt_logger_test(stack_name)):
#   print "SUCCESS: PACKET LOGGER MODE ACTIVATION SUCCESSFUL"
#else:
#   print "Failed to fetch mode info"

#if (vnf_NIDS_test(stack_name)):
#   print "SUCCESS: NIDS MODE ACTIVATION SUCCESSFUL"
#else:
#   print "Failed to fetch mode info"

#if (vnf_NIDS_read_test(stack_name)):
#   print "SUCCESS: NIDS READ MODE ACTIVATION SUCCESSFUL"
#else:
#   print "Failed to fetch mode info"

if (vnf_inline_testmode_test(stack_name)):
   print "SUCCESS: INILNE TEST MODE ACTIVATION SUCCESSFUL"
else:
   print "Failed to fetch mode info"
##-----------------------------------------------------------------
##if (vnf_allow1_http_test_multi(stack_name)):
##   print "SUCCESS: Server1 allowed and Server2 blocked"
##else:
##   print "Failed to assign rule"

##if (vnf_block1_http_test_multi(stack_name)):
##   print "SUCCESS: Server1 blocked and Server2 allowed"
##else:
##   print "Failed to assign rule"

##if (vnf_allallow_http_test_multi(stack_name)):
##   print "SUCCESS: Server1 and Server2 allowed"
##else:
##   print "Failed to assign rule"

##if (vnf_allblock_http_test_multi(stack_name)):
##   print "SUCCESS: Server1 nad Server2 blocked"
##else:
##   print "Failed to assign rule"
##-------------------------------------------------------------------

##if (vnf_upgrade_instance(stack_name)):
##   print "SUCCESS: stack upgraded successfully"
##else:
##   print "stack upgradation failed"

##if (vnf_delete_server(stack_name)):
##   print "SUCCESS: server deletion successful"
##else:
##   print "server deletion failed!!"
##   
##if (vnf_delete_stack(stack_name)):
##   print "SUCCESS: stack deletion successful"
##else:
##   print "server deletion failed!!"
#   


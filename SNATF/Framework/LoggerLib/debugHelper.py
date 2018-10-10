from cli_interface import SSHConnection
import sys
sys.path.append('/home/test/SNATF/TestRepository/Config')
import config,ControllerConfig
import time
import re
import pdb


debug_start_msg = "\n\n\t\t\t\t%s BASIC DEBUGGING IS STARTED %s\n"%(10*'*',10*'*')
debug_end_msg = "\n\n\t\t\t\t%s BASIC DEBUGGING IS COMPLETED %s\n"%(10*'*',10*'*')

def debug_controller_failure(ovs_obj,cntrlr_obj):
    """
    To perform the basic debug steps 
    against controller failure
    """
    ovs_obj.log_handler.writeDebuglog(debug_start_msg)
    cmd = "ovs-vsctl set-controller %s tcp:%s:%s"%(config.OVS_BRIDGE_CONF["NAME"],ControllerConfig.CONTROLLER_INFO['IP'],
                                                   ControllerConfig.CONTROLLER_INFO['PORT'])
    ovs_obj.log_handler.writeDebuglog(msg="Re-Set The Controller and check.... ")
    if ovs_obj.ovs_execute_command(cmd=cmd,prompt='#'):
        time.sleep(10)
        ovs_obj.ovs_execute_command(cmd="ovs-vsctl show", prompt='#')
        if re.search('is_connected: true',ovs_obj.resp) is None:
            ovs_obj.log_handler.writeErrorlog("Channel is not established between Controller and SWITCH !!!")
        else:
            ovs_obj.log_handler.writeInfolog("Channel is now established between Controller and SWITCH...")
        if cntrlr_obj.karaf_excute_command(cmd="netstat -npl | grep %s"%ControllerConfig.CONTROLLER_INFO['PORT'],
                                           exp_out='#'):
            #cntrlr_obj.resp = cntrlr_obj.resp
            if (ControllerConfig.CONTROLLER_INFO['PORT']+' ' not in cntrlr_obj.resp) or \
                    ('LISTEN' not in cntrlr_obj.resp) or ('java' not in cntrlr_obj.resp):
                cntrlr_obj.log_handler.writeErrorlog("Controller Container is not detected !!!")
            else:
                cntrlr_obj.log_handler.writeInfolog("Controller Container is now detected....")
        if cntrlr_obj.karaf_excute_command(cmd="netstat -npl | grep 6633", exp_out='#'):
            #cntrlr_obj.resp = cntrlr_obj.resp
            if ('6633 ' not in cntrlr_obj.resp) or ('LISTEN' not in cntrlr_obj.resp) or ('java' not in cntrlr_obj.resp):
                cntrlr_obj.log_handler.writeErrorlog("PORT 6633 is not in use by CONTROLLER, FLOWS CANT Be INSTALLED !!!")
            else:
                cntrlr_obj.log_handler.writeInfolog("PORT 6633 is now in use by CONTROLLER....")
                
        if cntrlr_obj.karaf_excute_command(cmd='ping %s -c 2'%config.SWITCH['IP'], exp_out='#'):
                if re.search(', 0% packet loss',cntrlr_obj.resp):
                    cntrlr_obj.log_handler.writeDebuglog(msg = "REACHABILITY IS PROPER....")
                else:
                    cntrlr_obj.log_handler.writeDebuglog(msg="FAILED TO REACH OVS SWITCH !!!!")
    cntrlr_obj.log_handler.writeDebuglog(debug_end_msg)

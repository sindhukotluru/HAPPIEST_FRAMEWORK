import util_findhost
from util_connection import SSHConnection
import time
import os
import pexpect
import subprocess
from pexpect import pxssh

debug = True


def dlog(log):
    if debug:
        print log

def exec_sys_command(cmd):
    import os
    return os.popen(cmd).read()

def create_local_user(rtr, login_ip, user_name, pwd, pvl_level = None):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    try:
        logging.info("Configure local username and password in router")
        vm.configure('set system login user %s' % user_name)
        vm.configure('set system login user %s authentication plaintext-password %s' % (user_name, pwd))
        if pvl_level:
            vm.configure('set system login user %s level %s' %(user_name, pvl_level))

        logging.info("Check local user config in %s" %rtr)
        vm.configure("show system login user")
        pass
    except:
        print("Create local user on %s FAILED" %rtr)
        status = False
    return status

def verify_login(rtr, login_ip, user_name, pwd, login_type):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    try:
        logging.info("Login %s with %s username-password provided" %(rtr, login_type))
        if vm.connect():
            logging.info("Verify %s user login in %s" %(login_type, rtr))
            vm.execute_command("show system login user")
            pass
        else:
            print("Verify %s user login on %s FAILED" % (login_type, rtr))
            status = False
    except:
        print("Verify %s user login on %s FAILED" %(login_type, rtr))
        status = False
    return status

def disconnect_login(rtr, login_ip, user_name, pwd, login_type):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    try:
        logging.info("Login %s with %s username-password provided" %(rtr, login_type))
        if vm.disconnect():
            logging.info("Verify %s user logout in %s SUCCESSFULL " %(login_type, rtr))
            pass
        else:
            print("Verify %s user logout on %s FAILED" % (login_type, rtr))
            status = False
    except:
        print("Verify %s user logout on %s FAILED" %(login_type, rtr))
        status = False
    return status

def create_radius_user(rtr, radius_ip, secret, port = None, timeout = None):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    try:
        logging.info("Configure RADIUS Server detail in router")
        vm.configure('set system login radius-server %s secret %s' % (radius_ip, secret))

        if port:
            vm.configure('set system login radius-server %s port %s' % (radius_ip, port))
        if timeout:
            vm.configure('set system login radius-server %s timeout %s' % (radius_ip, timeout))

        logging.info("Check RADIUS Server config in %s" %rtr)
        vm.configure("show system login radius-server %s" % radius_ip)
        pass
    except:
        print("Configure RADIUS Server detail on %s FAILED" %rtr)
        status = False
    return status

def delete_local_user(rtr, login_ip, user_name, pwd):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    try:
        logging.info("Delete local username and password in router")
        vm.configure('delete system login user %s ' % user_name)

        logging.info("Check local user config in %s DELETED" %rtr)
        vm.configure("show system login user")
        pass
    except:
        print("Delete local user on %s FAILED" %rtr)
        status = False
    return status

def delete_radius_user(rtr, radius_ip):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    try:
        logging.info("Delete RADIUS Server detail in router")
        vm.configure('delete system login radius-server %s' % radius_ip)

        logging.info("Check RADIUS Server config in %s" %rtr)
        vm.configure("show system login radius-server %s" % radius_ip)
        pass
    except:
        print("Delete RADIUS Server detail on %s FAILED" %rtr)
        status = False
    return status

def local_user_authentication_test_without_admin_privilage(login_ip, user_name, pwd, user_name2, pwd2, pvl_level, login_type):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    rtr = '%s_%s' %(user_name, login_ip)

    if vm.connect():
        status = create_local_user(rtr, login_ip, user_name2, pwd2, pvl_level) #configure local username password
        if status != True:
            return False

        status = verify_login(rtr, login_ip, user_name2, pwd2, login_type) #login with configured username password in step 1
        if status != True:
            return False

        status = disconnect_login(rtr, login_ip, user_name2, pwd2, login_type) #disconnect login session in step 2
        if status != True:
            return False

        status = delete_local_user(rtr, login_ip, user_name, pwd) #delete config done in step 1
        if status != True:
            return False

        vm.disconnect() #disconnect first login session
    else:
        print "VM connection FAILED."
        return False

def local_user_authentication_test_with_admin_privilage(login_ip, user_name, pwd, user_name2, pwd2, pvl_level, login_type):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    rtr = '%s_%s' %(user_name, login_ip)

    if vm.connect():
        status = create_local_user(rtr, login_ip, user_name2, pwd2, pvl_level) #configure local username password
        if status != True:
            return False

        status = verify_login(rtr, login_ip, user_name2, pwd2, login_type) #login with configured username password in step 1
        if status != True:
            return False

        status = disconnect_login(rtr, login_ip, user_name2, pwd2, login_type) #disconnect login session in step 2
        if status != True:
            return False

        status = delete_local_user(rtr, login_ip, user_name, pwd) #delete config done in step 1
        if status != True:
            return False

        vm.disconnect() #disconnect first login session
    else:
        print "VM connection FAILED."
        return False

def radius_user_authentication_test(login_ip, user_name, pwd, radius_ip, secret, user_name2, pwd2, port, timeout, login_type):
    status = True
    vm = SSHConnection(IP=login_ip, username=user_name, password=pwd)

    rtr = '%s_%s' %(user_name, login_ip)

    if vm.connect():
        status = create_radius_user(rtr, radius_ip, secret, port = port, timeout = timeout) #configure radius server
        if status != True:
            return False

        status = verify_login(rtr, login_ip, user_name2, pwd2, login_type) #login with configured username password in step 1
        if status != True:
            return False

        status = disconnect_login(rtr, login_ip, user_name2, pwd2, login_type) #disconnect login session in step 2
        if status != True:
            return False

        status = delete_radius_user(rtr, radius_ip) #delete config done in step 1
        if status != True:
            return False

        vm.disconnect() #disconnect first login session
    else:
        print "VM connection FAILED."
        return False


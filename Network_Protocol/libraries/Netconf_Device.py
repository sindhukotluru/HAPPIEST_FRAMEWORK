import sys
import pexpect
import getdata
import execute
import clear_buffer



class Netconf_Device:
  def __init(self):
    print("Initializing...")

  def configure_netconf(self,  Device, Interface, Action):

        device_data = getdata.get_data()
        hostname = device_data['Device_Details'][Device]['Hostname']
        Dev = Devices.Devices()
        child = Dev.connect(Device)

        if child:

            clear_buffer.flushBuffer(1, child)
            child.sendcontrol('m')
            child.sendcontrol('m')
            child.sendcontrol('m')
            flag = child.expect([hostname+'>', hostname+'#', 'Router\>', 'Router\#', \
                     pexpect.EOF, pexpect.TIMEOUT], timeout=90)
            if flag in (0, 2):
                Dev.Login(Device, child)
                if Action == 'configure':
                    configs = """
                    configure terminal
                    ip domain-name domain1.com
                    netconf ssh acl 1
                    netconf lock-time 60
                    netconf max-sessions 5
                    netconf max-message 2345
                    """ 
                    commands = configs.split('\n')
                    execute.execute(child, commands)
                    time.sleep(6)
                    child.sendcontrol('m')
                    child.sendcontrol('m')
                    clear_buffer.flushBuffer(1, child)
                    child.sendcontrol('m')
                    child.sendcontrol('m')
                    child.sendcontrol('m')
                    child.sendline("crypto key generate rsa")             
                         
                    flag = child.expect(['How many bits in the modulus [512]:>', \
                             pexpect.EOF, pexpect.TIMEOUT], timeout=90)
                    
                    if flag == 0:
                        child.sendline("1024")
                        child.sendcontrol('m')
                        return True
                    
                    elif flag in (1,2):
                        print 'console prompt did not match'
                        return False

                else:
                    unconfig = """
                    configure terminal
                    no ip domain-name domain1.com
                    no netconf ssh
                    no netconf lock-time
                    no netconf max-sessions
                    no netconf max-message
                    """
                    commands = unconfig.split('\n')
                    execute.execute(child, commands)
                    time.sleep(6)
                    child.sendcontrol('m')
                    child.sendcontrol('m')
                    child.sendline('exit')
                    child.sendcontrol('m')
                    return True
                    


      else:
          return False

  def set_IP(self, Device):
    child = self.connect(Device)
    if child:
      device_data = getdata.get_data()
      clear_buffer.flushBuffer(1, child)
      child.sendcontrol('m')
      child.expect(['R6#', pexpect.EOF, pexpect.TIMEOUT], timeout=50)
      interface = device_data['Link_Details'][Device]
      address = device_data['Device_Details'][Device][interface]
      configs = """
      enable
      configure terminal
      """
      commands = configs.split('\n')
      execute.execute(child, commands)
      child.sendcontrol('m')
      child.expect(['R6(config)#', pexpect.EOF, pexpect.TIMEOUT], timeout=50)
      configs = """
      hostname netconf1
      ip domain-name domain1.com
      crypto key generate rsa
      1024
      username user1 password user1
      interface %s
      ip address %s
      no shutdown
      exit
      exit 
      """ % (interface, address)
      commands = configs.split('\n')
      execute.execute(child, commands)
      child.sendcontrol('m')
      return True

    else:
      print 'No conenction established'
      return False


#  def ping_router(self,Device,Action,Peer_IP,Count="5"):
#    device_data = getdata.get_data()
#    IP_add = device_data['Device_Details'][Device]['ip_add']
#    Port_no = device_data['Device_Details'][Device]['port']
#    child = pexpect.spawn('telnet ' + IP_add + ' ' + Port_no)
#    clear_buffer.flushBuffer(1,child)
#    if (child):
#      child.sendcontrol('m')
#      child.sendcontrol('m')
#      flag = child.expect(['PC-1>*',pexpect.EOF,pexpect.TIMEOUT],timeout=50)
#
#      if (flag == 0):
#              configs = "ping %s -c %s " % (Peer_IP,Count)
#              commands = configs.split('\n')
#              execute.execute(child,commands)
#              resp = child.before.decode('utf-8')
#              child.sendcontrol('m')
#              child.sendcontrol('m')
#              regex = r'bytes from %s icmp_seq' %(Peer_IP)
#              if re.search(regex,resp):
#                return True
#              else:
#                return False
#
#    else:
#
#      return False
dev = Netconf_Device()

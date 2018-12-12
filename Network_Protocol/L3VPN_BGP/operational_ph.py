import re
import pexpect
import paramiko
import getdata
import execute
import Devices
import clear_buffer


def checking_operabilty(Device, command):
    device_data = getdata.get_data()
    hostname = device_data['Device_Details'][Device]['Hostname']
    Dev = Devices.Devices()
    child = Dev.connect(Device)
    if child:

      clear_buffer.flushBuffer(10, child)
      child.sendcontrol('m')
      child.sendcontrol('m')
      child.sendcontrol('m')
      flag = child.expect([hostname+'>', hostname+'#', 'Router\>', 'Router\#',\
             pexpect.EOF, pexpect.TIMEOUT], timeout=90)
      if flag in (0, 2):
        Dev.Login(Device, child)
        configs = """
        %s
        """ % (command)
        commands = configs.split('\n')
        execute.execute(child, commands)
        resp = child.before.decode('utf-8')
        child.sendcontrol('m')
        child.sendcontrol('m')
        regex = r'up'
        if re.search(regex, resp):
          return True
        else:
          return False

      if flag in (1, 3):
        configs = """
        %s
        """ % (command)
        commands = configs.split('\n')
        execute.execute(child, commands)
        resp = child.before.decode('utf-8')
        child.sendcontrol('m')
        child.sendcontrol('m')
        regex = r'up'
        if re.search(regex, resp):
          return True
        else:
          return False

      return True

    else:
      return False

def checking_operabilty_ospf(Device, command):
    device_data = getdata.get_data()
    hostname = device_data['Device_Details'][Device]['Hostname']
    Dev = Devices.Devices()
    child = Dev.connect(Device)
    if child:

      clear_buffer.flushBuffer(10, child)
      child.sendcontrol('m')
      child.sendcontrol('m')
      child.sendcontrol('m')
      flag = child.expect([hostname+'>', hostname+'#', 'Router\>', 'Router\#',\
                           pexpect.EOF, pexpect.TIMEOUT], timeout=90)
      if flag in (0, 2):
        Dev.Login(Device, child)
        configs = """
        %s
        """ % (command)
        commands = configs.split('\n')
        execute.execute(child, commands)
        resp = child.before.decode('utf-8')
        child.sendcontrol('m')
        child.sendcontrol('m')
        regex = r'FULL'
        if re.search(regex, resp):
          return True
        else:
          return False


      if flag in (1, 3):
        configs = """
        %s
        """ % (command)
        commands = configs.split('\n')
        execute.execute(child, commands)
        resp = child.before.decode('utf-8')
        child.sendcontrol('m')
        child.sendcontrol('m')
        regex = r'FULL'
        if re.search(regex, resp):
          return True
        else:
          return False

      else:
          return False

def ping_host(server, user_name, password, destination_ip, echo_count=5):

    cmd_to_execute = "timeout {0} vtysh -c 'ping {1}'".format(echo_count, destination_ip)
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.connect(server, username=user_name, password=password)
    if ssh.connect:
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(cmd_to_execute)
        output = ssh_stdout.read().decode('utf-8')
        if output:
            regex = r'bytes from %s: icmp_seq' %(destination_ip)
            if re.search(regex, output):
                return True
            else:
                return False

    else:
      return False


def ping_router(Device, Action, Peer_IP, Count="5"):
    print(Action)
    device_data = getdata.get_data()
    IP_add = device_data['Device_Details'][Device]['ip_add']
    Port_no = device_data['Device_Details'][Device]['port']
    child = pexpect.spawn('telnet ' + IP_add + ' ' + Port_no)
    clear_buffer.flushBuffer(1, child)
    if child:
      child.sendcontrol('m')
      child.sendcontrol('m')
      flag = child.expect(['PC*', pexpect.EOF, pexpect.TIMEOUT], timeout=50)

      if flag == 0:
              configs = "ping %s -c %s " % (Peer_IP, Count)
              commands = configs.split('\n')
              execute.execute(child, commands)
              resp = child.before.decode('utf-8')
              child.sendcontrol('m')
              child.sendcontrol('m')
              regex = r'bytes from %s icmp_seq' %(Peer_IP)
              if re.search(regex, resp):
                return True
              else:
                return False

    else:

      return False

def checking_operabilty_bgp(Device, command):
    device_data = getdata.get_data()
    hostname = device_data['Device_Details'][Device]['Hostname']
    port = device_data['Device_Details'][Device]['port']
    Dev = Devices.Devices()
    child = Dev.connect(Device)

    if port != "zebra":
        if child:

          clear_buffer.flushBuffer(10, child)
          child.sendcontrol('m')
          child.sendcontrol('m')
          child.sendcontrol('m')
          flag = child.expect([hostname+'>', hostname+'#', 'Router\>', \
                 'Router\#', pexpect.EOF, pexpect.TIMEOUT], timeout=90)
          if flag in (0, 2):
              Dev.Login(Device, child)
              configs = """
              %s
              """ % (command)
              commands = configs.split('\n')
              execute.execute(child, commands)
              resp = child.before.decode('utf-8')
              child.sendcontrol('m')
              child.sendcontrol('m')
              regex = r'never'
              if re.search(regex, resp):
                  return False
              else:
                  return True


          if flag in (1, 3):
              configs = """
              %s
              """ % (command)
              commands = configs.split('\n')
              execute.execute(child, commands)
              resp = child.before.decode('utf-8')
              child.sendcontrol('m')
              child.sendcontrol('m')
              regex = r'never'
              if re.search(regex, resp):
                  return False
              else:
                  return True

    elif port == 'zebra':
        port = "bgpd"
        device_data = getdata.get_data()
        IP_add = device_data['Device_Details'][Device]['ip_add']
        child = pexpect.spawn('telnet ' + IP_add + ' ' + port)
        hostname = device_data['Device_Details'][Device]['Hostname']
        clear_buffer.flushBuffer(10, child)

        child.sendcontrol('m')
        flag = (child.expect(['bgpd*', 'Password*', pexpect.EOF, pexpect.TIMEOUT], timeout=100))
        if flag == 1:
            child.send('zebra')
            child.sendcontrol('m')
            flag = child.expect(['bgpd*>', pexpect.EOF, pexpect.TIMEOUT], timeout=50)
            if flag == 0:
                child.send('enable')
                child.sendcontrol('m')

                if child:
                   flag = child.expect(['bgpd#*', pexpect.EOF, pexpect.TIMEOUT], timeout=90)
                   if flag == 0:
                       Dev.Login(Device, child)
                       configs = """
                       %s
                       """ % (command)
                       commands = configs.split('\n')
                       execute.execute(child, commands)
                       resp = child.before.decode('utf-8')
                       child.sendcontrol('m')
                       child.sendcontrol('m')
                       regex = r'never'
                       if re.search(regex, resp):
                           return False
                       else:
                           return True

    else:
          return False

def ping_vrf(Device, vrf_name, host_ip):
    device_data = getdata.get_data()
    IP_add = device_data['Device_Details'][Device]['ip_add']
    Port_no = device_data['Device_Details'][Device]['port']
    child = pexpect.spawn('telnet ' + IP_add + ' ' + Port_no)
    clear_buffer.flushBuffer(1, child)
    if child:
      child.sendcontrol('m')
      child.sendcontrol('m')
      flag = child.expect(['R*#', pexpect.EOF, pexpect.TIMEOUT], timeout=50)

      if flag == 0:
              configs = "ping vrf %s %s" % (vrf_name, host_ip)
              commands = configs.split('\n')
              execute.execute(child, commands)
              resp = child.before.decode('utf-8')
              child.sendcontrol('m')
              child.sendcontrol('m')
              regex = r'Success rate is \d+ percent \(\d\/\d\)*'
              if re.search(regex, resp):
                return True
              else:
                return False

    else:
      return False

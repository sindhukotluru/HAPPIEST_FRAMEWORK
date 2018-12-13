import time
import pexpect
import execute
import Devices
import clear_buffer
import getdata

class VRF:
    def Configure_VRFs(self, Device, vrf_name, rd, rt, Links, ip_addr, mask, Action):
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
            if flag in (1, 3):
                Dev.Login(Device, child)
                if Action == 'enable':
                    if isinstance(Links, list):
                        for Lnk in Links:
                                interface = device_data['Link_Details'][Lnk][Device]

                                configs = """
                                          configure terminal
                                          ip vrf %s
                                          rd %s
                                          route-target export %s
                                          route-target import %s
                                          exit
                                          interface  %s
                                          ip vrf forwarding  %s
                                          ip address %s %s
                                          exit
                                          exit
                                """ % (vrf_name, rd, rt, rt, interface, vrf_name, ip_addr, mask)
                                commands = configs.split('\n')
                                execute.execute(child, commands)
                                time.sleep(6)
                                child.sendcontrol('m')
                        child.sendline('exit')
                        child.sendcontrol('m')
                else:
                    unconfig = """
                        configure terminal
                        no ip vrf %s
                        exit
                        exit
                        """ % (vrf_name)
                    commands = unconfig.split('\n')
                    execute.execute(child, commands)
                    child.sendcontrol('m')

                return True

        else:
            return False

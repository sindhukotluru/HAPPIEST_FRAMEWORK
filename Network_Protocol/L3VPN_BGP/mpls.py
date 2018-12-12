import time
import pexpect
import execute
import Devices
import clear_buffer
import getdata

class MPLS:

    def Configure_mpls(self, Interface, mpls_label):

        device_data = getdata.get_data()
        hostname = device_data['Device_Details'][Device]['Hostname']
        Dev = Devices.Devices()
        child = Dev.connect(Device)

        if child:

            clear_buffer.flushBuffer(10, child)
            child.sendcontrol('m')
            child.sendcontrol('m')
            child.sendcontrol('m')
            flag = child.expect([hostname+'>', hostname+'#', 'Router\>', 'Router\#', \
                     pexpect.EOF, pexpect.TIMEOUT], timeout=90)
            if flag in (0, 2):
                Dev.Login(Device, child)
                if Action == 'enable':
                    if isinstance(Interface, list):
                        for interface in Interface:
                                configs = """
                                          configure terminal
                                          ip cef
                                          mpls label protocol %s
                                          mpls ldp router-id Loopback0 force
                                          interface %s
                                          mpls ip
                                          mpls label protocol %s
                                          exit
                                          exit
                                """ % (mpls_label, interface, mpls_label)
                                commands = configs.split('\n')
                                execute.execute(child, commands)
                                time.sleep(6)
                                child.sendcontrol('m')
                        child.sendline('exit')
                        child.sendcontrol('m')

                else:
                    unconfig = """
                        configure terminal
                        interface %s
                        no mpls ip
                        no mpls label protocol %s
                        exit
                        exit
                        """ % (mpls_label, interface, mpls_label)
                    commands = unconfig.split('\n')
                    execute.execute(child, commands)
                    child.sendcontrol('m')

                return True

        else:
            return False

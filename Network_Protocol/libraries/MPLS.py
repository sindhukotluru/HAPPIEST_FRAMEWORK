import time
import pexpect
import execute
import Devices
import clear_buffer
import getdata

class MPLS:

    def Configure_mpls(self, Device, Links, mpls_label_proto, Action):
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
                                          ip cef
                                          mpls label protocol %s
                                          mpls ldp router-id Loopback0 force
                                          interface %s
                                          mpls ip
                                          mpls label protocol %s
                                          exit
                                          exit
                                """ % (mpls_label_proto, interface, mpls_label_proto)
                                commands = configs.split('\n')
                                execute.execute(child, commands)
                                time.sleep(6)
                                child.sendcontrol('m')
                        child.sendline('exit')
                        child.sendcontrol('m')

                else:
                    if isinstance(Links, list):
                       for Lnk in Links:
                           interface = device_data['Link_Details'][Lnk][Device]
                           unconfig = """
                           configure terminal
                           no mpls label protocol %s
                           no mpls ldp router-id Loopback0 force
                           interface %s
                           no mpls ip
                           no mpls label protocol %s
                           exit
                           exit
                           """ % (mpls_label_proto, interface, mpls_label_proto)
                           commands = unconfig.split('\n')
                           execute.execute(child, commands)
                           time.sleep(6)
                           child.sendcontrol('m')

                return True

        else:
            return False

    def Configure_mpbgp(self, Device, AS_id, Interface, Action):
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
                    configs = """
                        configure terminal
                        router bgp %d
                        address-family vpnv4
                        neighbor %s activate
                        neighbor %s next-hop-self
                        exit-address-family
                        end
                        """ % (AS_id, Interface, Interface)
                    commands = configs.split('\n')
                    execute.execute(child, commands)
                    time.sleep(6)
                    child.sendcontrol('m')
                    child.sendline('exit')
                    child.sendcontrol('m')

                else:
                    unconfig = """
                    configure terminal
                    no router bgp %s
                    end
                    """ % (AS_id)
                    commands = unconfig.split('\n')
                    execute.execute(child, commands)
                    child.sendcontrol('m')

                return True

        else:
            return False

    def Configure_ebgpvrf(self, Device, AS_id, VRF_Name, Interface, neighbor_AS_id, Action):
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
                    configs = """
                        configure terminal
                        router bgp %d
                        address-family ipv4 vrf %s
                        neighbor %s remote-as %s
                        neighbor %s activate     
                        exit-address-family
                        end
                        """ % (AS_id, VRF_Name, Interface, neighbor_AS_id, Interface)
                    commands = configs.split('\n')
                    execute.execute(child, commands)
                    time.sleep(6)
                    child.sendcontrol('m')
                    child.sendline('exit')
                    child.sendcontrol('m')

                else:
                    unconfig = """
                    configure terminal
                    no router bgp %s
                    end
                    """ % (AS_id)
                    commands = unconfig.split('\n')
                    execute.execute(child, commands)
                    child.sendcontrol('m')

                return True

        else:
            return False

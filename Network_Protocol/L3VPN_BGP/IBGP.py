import time
import pexpect
import execute
import Devices
import clear_buffer
import getdata

class IBGP:

<<<<<<< HEAD
    def Configure_VRFs(self, vrf_name, rd, rt , Interface, ip_addr, mask, Action):
=======
    def Configure_VRFs(self, vrf_name, rd, rt):
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9

        device_data = getdata.get_data()
        hostname = device_data['Device_Details'][Device]['Hostname']
        Dev = Devices.Devices()
        child = Dev.connect(Device)

        if child:

<<<<<<< HEAD
            clear_buffer.flushBuffer(1, child)
=======
            clear_buffer.flushBuffer(10, child)
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
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

    def Configure_IBGP(self, Device, AS_id, Interface, Action):

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
                                router bgp %d
                                neighbor %s remote-as %d
                                neighbor %s update-source loopback 0
<<<<<<< HEAD
                                address family vpnv4
                                neighbor %s activate
                                exit-address-family
                                exit
                                exit
                                """ % (AS_id, interface, AS_id, interface, interface)
=======
                                exit
                                exit
                                """ % (AS_id, interface, AS_id, interface)
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                                commands = configs.split('\n')
                                execute.execute(child, commands)
                                time.sleep(6)
                                child.sendcontrol('m')
                        child.sendline('exit')
                        child.sendcontrol('m')

                    else:
                        interface = Interface
                        configs = """
                        configure terminal
                        router bgp %d
                        neighbor %s remote-as %d
                        neighbor %s update-source loopback 0
<<<<<<< HEAD
                        address family vpnv4
                        neighbor %s activate
                        exit-address-family
                        exit
                        exit
                        """ % (AS_id, interface, AS_id, interface, interface)
=======
                        exit
                        exit
                        """ % (AS_id, interface, AS_id, interface)
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                        commands = configs.split('\n')
                        execute.execute(child, commands)
                        child.sendcontrol('m')

                else:
                    unconfig = """
                    configure terminal
                    no router bgp %d
                    exit
                    exit
                    """ % (AS_id)
                    commands = configs.split('\n')
                    execute.execute(child, commands)
                    child.sendcontrol('m')



            if flag in (1, 3):
                if Action == 'enable':
                    if isinstance(Interface, list):
                        for interface in Interface:
                                print(interface)
                                configs = """
                                configure terminal
                                router bgp %d
                                neighbor %s remote-as %d
                                neighbor %s update-source loopback 0
<<<<<<< HEAD
                                address family vpnv4
                                neighbor %s activate
                                exit-address-family
                                exit
                                exit
                                """ % (AS_id, interface, AS_id, interface, interface)
=======
                                exit
                                exit
                                """ % (AS_id, interface, AS_id, interface)
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                                commands = configs.split('\n')
                                execute.execute(child, commands)
                                time.sleep(6)
                                child.sendcontrol('m')
                        child.sendline('exit')
                        child.sendcontrol('m')

                    else:
                        interface = Interface
                        configs = """
                        configure terminal
                        router bgp %d
                        neighbor %s remote-as %d
                        neighbor %s update-source loopback 0
<<<<<<< HEAD
                        address family vpnv4
                        neighbor %s activate
                        exit-address-family
                        exit
                        exit
                        """ % (AS_id, interface, AS_id, interface, interface)
=======
                        exit
                        exit
                        exit
                        """ % (AS_id, interface, AS_id, interface)
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                        commands = configs.split('\n')
                        execute.execute(child, commands)
                        child.sendcontrol('m')

                else:
                    unconfig = """
                    configure terminal
                    no router bgp %d
                    exit
                    exit
                    """ % (AS_id)
                    commands = configs.split('\n')
                    execute.execute(child, commands)
                    child.sendcontrol('m')

                return True

        else:
            return False


    def enable_syn(self, Device, AS_id):


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
                configs = """
                configure terminal
                router bgp %d
                synchronization
                end
                """ % (AS_id)
                commands = configs.split('\n')
                execute.execute(child, commands)
                child.sendcontrol('m')


            if flag in (1, 3):
                configs = """
                configure terminal
                router bgp %d
                synchronization
                end
                """ % (AS_id)
                commands = configs.split('\n')
                execute.execute(child, commands)
                child.sendcontrol('m')

            return True

        else:
            return False



    def Configure_EBGP(self, Device, AS_id, Interface, neighbor_AS_id, Action, NW_id, Mask):

        device_data = getdata.get_data()
        hostname = device_data['Device_Details'][Device]['Hostname']
        Dev = Devices.Devices()
        child = Dev.connect(Device)
        port = device_data['Device_Details'][Device]['port']

        if port != "zebra":
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
                                    router bgp %d
                                    neighbor %s remote-as %d
<<<<<<< HEAD
=======
                                    network %s mask %s
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                                    exit
                                    exit
                                    """ % (AS_id, interface, neighbor_AS_id, NW_id, Mask)
                                    commands = configs.split('\n')
                                    execute.execute(child, commands)
                                    time.sleep(6)
                                    child.sendcontrol('m')
                            child.sendline('exit')
                            child.sendcontrol('m')

                        else:
                            interface = Interface
                            configs = """
                            configure terminal
                            router bgp %d
                            neighbor %s remote-as %d
<<<<<<< HEAD
=======
                            network %s mask %s
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                            exit
                            exit
                            """ % (AS_id, interface, neighbor_AS_id, NW_id, Mask)
                            commands = configs.split('\n')
                            execute.execute(child, commands)
                            child.sendcontrol('m')

                    else:
                        unconfig = """
                        configure terminal
                        no router bgp %d
                        exit
                        exit
                        """ % (AS_id)
                        commands = unconfig.split('\n')
                        execute.execute(child, commands)
                        child.sendcontrol('m')

                if flag in (1, 3):
                    if Action == 'enable':
                        if isinstance(Interface, list):
                            for interface in Interface:

                                    configs = """
                                    configure terminal
                                    router bgp %d
                                    neighbor %s remote-as %d
<<<<<<< HEAD
=======
                                    network %s mask %s
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                                    exit
                                    exit
                                    """ % (AS_id, interface, neighbor_AS_id, NW_id, Mask)
                                    commands = configs.split('\n')
                                    execute.execute(child, commands)
                                    child.sendcontrol('m')
                            child.sendline('exit')
                            child.sendcontrol('m')

                        else:
                            interface = Interface
                            configs = """
                            configure terminal
                            router bgp %d
                            neighbor %s remote-as %d
<<<<<<< HEAD
=======
                            network %s mask %s
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                            exit
                            exit
                            """ % (AS_id, interface, neighbor_AS_id, NW_id, Mask)
                            commands = configs.split('\n')
                            execute.execute(child, commands)
                            child.sendcontrol('m')

                    else:
                        unconfig = """
                        configure terminal
                        no router bgp %d
                        exit
                        exit
                        """ % (AS_id)
                        commands = unconfig.split('\n')
                        execute.execute(child, commands)
                        child.sendcontrol('m')

                    return True
        elif port == 'zebra':
                    port = "bgpd"
                    device_data = getdata.get_data()
                    IP_add = device_data['Device_Details'][Device]['ip_add']
                    child = pexpect.spawn('telnet ' + IP_add + ' ' + port)
                    hostname = device_data['Device_Details'][Device]['Hostname']
                    clear_buffer.flushBuffer(10, child)

                    child.sendcontrol('m')
                    flag = (child.expect(['bgpd*', 'Password*', \
                            pexpect.EOF, pexpect.TIMEOUT], timeout=100))
                    if flag == 1:
                        child.send('zebra')
                        child.sendcontrol('m')
                        flag = child.expect(['bgpd*>', pexpect.EOF, \
                               pexpect.TIMEOUT], timeout=50)
                        if flag == 0:
                            child.send('enable')
                            child.sendcontrol('m')

                            if child:
                               flag = child.expect(['bgpd#*', pexpect.EOF, \
                                                pexpect.TIMEOUT], timeout=90)
                               if flag == 0:
                                   Dev.Login(Device, child)
                                   if Action == 'enable':
                                       if isinstance(Interface, list):
                                           for interface in Interface:
                                               configs = """
                                               configure terminal
                                               router bgp %d
                                               neighbor %s remote-as %d
<<<<<<< HEAD
=======
                                               network %s
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                                               exit
                                               exit
                                               """ % (AS_id, interface, neighbor_AS_id, NW_id)
                                               commands = configs.split('\n')
                                               execute.execute(child, commands)
                                               time.sleep(6)
                                               child.sendcontrol('m')
                                               child.sendline('exit')
                                               child.sendcontrol('m')

                                       else:
                                           interface = Interface
                                           configs = """
                                           configure terminal
                                           router bgp %d
                                           neighbor %s remote-as %d
<<<<<<< HEAD
=======
                                           network %s
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9
                                           exit
                                           exit
                                           """ % (AS_id, interface, neighbor_AS_id, NW_id)
                                           commands = configs.split('\n')
                                           execute.execute(child, commands)
                                           child.sendcontrol('m')

                                   else:
                                           unconfig = """
                                           configure terminal
                                           no router bgp %d
                                           exit
                                           exit
                                           """ % (AS_id)
                                           commands = unconfig.split('\n')
                                           execute.execute(child, commands)
                                           child.sendcontrol('m')


                                   return True

        else:
            return False


    def advertising_loopback(self, Device, AS_id, Interface, mask):
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
                configs = """
                configure terminal
                router bgp %d
                network %s mask %s
                end
                """ % (AS_id, Interface, mask)
                commands = configs.split('\n')
                execute.execute(child, commands)
                child.sendcontrol('m')


            if flag in (1, 3):
                configs = """
                configure terminal
                router bgp %d
                network %s mask %s
                end
                """ % (AS_id, Interface, mask)
                commands = configs.split('\n')
                execute.execute(child, commands)
                child.sendcontrol('m')

            return True

        else:
            return False



    def redistribution(self, Device, AS_id, Process_id=None):

        device_data = getdata.get_data()
        hostname = device_data['Device_Details'][Device]['Hostname']
        Dev = Devices.Devices()
        child = Dev.connect(Device)
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
                configure terminal
                router bgp %d
                redistribute ospf %d
                exit
                router ospf %d
                redistribute bgp %d subnets
                end
                """ % (AS_id, Process_id, Process_id, AS_id)
                commands = configs.split('\n')
                execute.execute(child, commands)
                child.sendcontrol('m')

            if flag in (1, 3):
                configs = """
                configure terminal
                router bgp %d
                redistribute ospf %d
                exit
                router ospf %d
                redistribute bgp %d subnets
                end
                """ % (AS_id, Process_id, Process_id, AS_id)
                commands = configs.split('\n')
                execute.execute(child, commands)
                child.sendcontrol('m')

            return True

        else:
            return False


    def route(self, Device, AS_id, Interface):

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
                configs = """
                configure terminal
                router bgp %d
                neighbor %s next-hop-self
                end
                """ % (AS_id, Interface)
                commands = configs.split('\n')
                execute.execute(child, commands)
                child.sendcontrol('m')


            if flag in (1, 3):
                configs = """
                configure terminal
                router bgp %d
                neighbor %s next-hop-self
                end
                """ % (AS_id, Interface)
                commands = configs.split('\n')
                execute.execute(child, commands)
                child.sendcontrol('m')

            return True

        else:
            return False


    def redistribution_connected(self, Device, AS_id):

                device_data = getdata.get_data()
                hostname = device_data['Device_Details'][Device]['Hostname']
                Dev = Devices.Devices()
                child = Dev.connect(Device)
                port = device_data['Device_Details'][Device]['port']

                if port != "zebra":
                    if child:

                        clear_buffer.flushBuffer(10, child)
                        child.sendcontrol('m')
                        child.sendcontrol('m')
                        child.sendcontrol('m')
                        flag = child.expect([hostname+'>', hostname+'#', 'Router\>', 'Router\#', \
                               pexpect.EOF, pexpect.TIMEOUT], timeout=90)
                        if flag in (0, 2):
                                  Dev.Login(Device, child)
                                  configs = """
                                  configure terminal
                                  router bgp %d
                                  redistribute connected
                                  end
                                  """ % (AS_id)
                                  commands = configs.split('\n')
                                  execute.execute(child, commands)
                                  child.sendcontrol('m')

                        if flag in (1, 3):
                                  configs = """
                                  configure terminal
                                  router bgp %d
                                  redistribute connected
                                  end
                                  """ % (AS_id)
                                  commands = configs.split('\n')
                                  execute.execute(child, commands)
                                  child.sendcontrol('m')

                        return True

                elif port == 'zebra':
                    port = "bgpd"
                    device_data = getdata.get_data()
                    IP_add = device_data['Device_Details'][Device]['ip_add']
                    child = pexpect.spawn('telnet ' + IP_add + ' ' + port)
                    hostname = device_data['Device_Details'][Device]['Hostname']
                    clear_buffer.flushBuffer(10, child)

                    child.sendcontrol('m')
                    flag = (child.expect(['bgpd*', 'Password*', pexpect.EOF,\
                            pexpect.TIMEOUT], timeout=100))
                    if flag == 1:
                        child.send('zebra')
                        child.sendcontrol('m')
                        flag = child.expect(['bgpd*>', pexpect.EOF,\
                               pexpect.TIMEOUT], timeout=50)
                        if flag == 0:
                            child.send('enable')
                            child.sendcontrol('m')

                        if child:

                            clear_buffer.flushBuffer(10, child)
                            child.sendcontrol('m')
                            child.sendcontrol('m')
                            child.sendcontrol('m')
                            flag = child.expect(['bgpd#*', pexpect.EOF, \
                                   pexpect.TIMEOUT], timeout=90)
                            if flag in (0, 2):
                             Dev.Login(Device, child)
                             configs = """
                             configure terminal
                             router bgp %d
                             redistribute connected
                             end
                             """ % (AS_id)
                             commands = configs.split('\n')
                             execute.execute(child, commands)
                             child.sendcontrol('m')

                            if flag in (1, 3):
                             configs = """
                             configure terminal
                             router bgp %d
                             redistribute connected
                             end
                             """ % (AS_id)
                             commands = configs.split('\n')
                             execute.execute(child, commands)
                             child.sendcontrol('m')

                            return True
                else:
                  return False
<<<<<<< HEAD

    def Configure_EBGP(self, Device, AS_id, Interface, neighbor_AS_id, Action, NW_id, Mask):

        device_data = getdata.get_data()
        hostname = device_data['Device_Details'][Device]['Hostname']
        Dev = Devices.Devices()
        child = Dev.connect(Device)
        port = device_data['Device_Details'][Device]['port']

        if port != "zebra":
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
                                    router bgp %d
                                    neighbor %s remote-as %d
                                    exit
                                    exit
                                    """ % (AS_id, interface, neighbor_AS_id, NW_id, Mask)
                                    commands = configs.split('\n')
                                    execute.execute(child, commands)
                                    time.sleep(6)
                                    child.sendcontrol('m')
                            child.sendline('exit')
                            child.sendcontrol('m')

                        else:
                            interface = Interface
                            configs = """
                            configure terminal
                            router bgp %d
                            neighbor %s remote-as %d
                            exit
                            exit
                            """ % (AS_id, interface, neighbor_AS_id, NW_id, Mask)
                            commands = configs.split('\n')
                            execute.execute(child, commands)
                            child.sendcontrol('m')

                    else:
                        unconfig = """
                        configure terminal
                        no router bgp %d
                        exit
                        exit
                        """ % (AS_id)
                        commands = unconfig.split('\n')
                        execute.execute(child, commands)
                        child.sendcontrol('m')

                if flag in (1, 3):
                    if Action == 'enable':
                        if isinstance(Interface, list):
                            for interface in Interface:

                                    configs = """
                                    configure terminal
                                    router bgp %d
                                    neighbor %s remote-as %d
                                    exit
                                    exit
                                    """ % (AS_id, interface, neighbor_AS_id, NW_id, Mask)
                                    commands = configs.split('\n')
                                    execute.execute(child, commands)
                                    child.sendcontrol('m')
                            child.sendline('exit')
                            child.sendcontrol('m')

                        else:
                            interface = Interface
                            configs = """
                            configure terminal
                            router bgp %d
                            neighbor %s remote-as %d
                            exit
                            exit
                            """ % (AS_id, interface, neighbor_AS_id, NW_id, Mask)
                            commands = configs.split('\n')
                            execute.execute(child, commands)
                            child.sendcontrol('m')

                    else:
                        unconfig = """
                        configure terminal
                        no router bgp %d
                        exit
                        exit
                        """ % (AS_id)
                        commands = unconfig.split('\n')
                        execute.execute(child, commands)
                        child.sendcontrol('m')

                    return True
        elif port == 'zebra':
                    port = "bgpd"
                    device_data = getdata.get_data()
                    IP_add = device_data['Device_Details'][Device]['ip_add']
                    child = pexpect.spawn('telnet ' + IP_add + ' ' + port)
                    hostname = device_data['Device_Details'][Device]['Hostname']
                    clear_buffer.flushBuffer(10, child)

                    child.sendcontrol('m')
                    flag = (child.expect(['bgpd*', 'Password*', \
                            pexpect.EOF, pexpect.TIMEOUT], timeout=100))
                    if flag == 1:
                        child.send('zebra')
                        child.sendcontrol('m')
                        flag = child.expect(['bgpd*>', pexpect.EOF, \
                               pexpect.TIMEOUT], timeout=50)
                        if flag == 0:
                            child.send('enable')
                            child.sendcontrol('m')

                            if child:
                               flag = child.expect(['bgpd#*', pexpect.EOF, \
                                                pexpect.TIMEOUT], timeout=90)
                               if flag == 0:
                                   Dev.Login(Device, child)
                                   if Action == 'enable':
                                       if isinstance(Interface, list):
                                           for interface in Interface:
                                               configs = """
                                               configure terminal
                                               router bgp %d
                                               neighbor %s remote-as %d
                                               exit
                                               exit
                                               """ % (AS_id, interface, neighbor_AS_id, NW_id)
                                               commands = configs.split('\n')
                                               execute.execute(child, commands)
                                               time.sleep(6)
                                               child.sendcontrol('m')
                                               child.sendline('exit')
                                               child.sendcontrol('m')

                                       else:
                                           interface = Interface
                                           configs = """
                                           configure terminal
                                           router bgp %d
                                           neighbor %s remote-as %d
                                           exit
                                           exit
                                           """ % (AS_id, interface, neighbor_AS_id, NW_id)
                                           commands = configs.split('\n')
                                           execute.execute(child, commands)
                                           child.sendcontrol('m')

                                   else:
                                           unconfig = """
                                           configure terminal
                                           no router bgp %d
                                           exit
                                           exit
                                           """ % (AS_id)
                                           commands = unconfig.split('\n')
                                           execute.execute(child, commands)
                                           child.sendcontrol('m')


                                   return True

        else:
            return False

    def Configure_EBGP_PE(self, Device, AS_id, vrf_name, Interface, neighbor_AS_id, Action):

        device_data = getdata.get_data()
        hostname = device_data['Device_Details'][Device]['Hostname']
        Dev = Devices.Devices()
        child = Dev.connect(Device)
        port = device_data['Device_Details'][Device]['port']

        if port != "zebra":
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
                                    router bgp %d
                                    address-family ipv4 vrf %s
                                    neighbor %s remote-as %s
                                    neighbor %s activate
                                    exit-address-family
                                    exit
                                    exit
                                    """ % (AS_id, vrf_name, interface, neighbor_AS_id)
                                    commands = configs.split('\n')
                                    execute.execute(child, commands)
                                    time.sleep(6)
                                    child.sendcontrol('m')
                            child.sendline('exit')
                            child.sendcontrol('m')

                        else:
                            interface = Interface
                            configs = """
                            configure terminal
                            router bgp %d
                            address-family ipv4 vrf %s
                            neighbor %s remote-as %s
                            neighbor %s activate
                            exit-address-family
                            exit
                            """ % (AS_id, vrf_name, interface, neighbor_AS_id)
                            commands = configs.split('\n')
                            execute.execute(child, commands)
                            child.sendcontrol('m')

                    else:
                        unconfig = """
                        configure terminal
                        no router bgp %d
                        exit
                        exit
                        """ % (AS_id)
                        commands = unconfig.split('\n')
                        execute.execute(child, commands)
                        child.sendcontrol('m')

                if flag in (1, 3):
                    if Action == 'enable':
                        if isinstance(Interface, list):
                            for interface in Interface:

                                    configs = """
                                    configure terminal
                                    router bgp %d
                                    address-family ipv4 vrf %s
                                    neighbor %s remote-as %s
                                    neighbor %s activate
                                    exit-address-family
                                    exit
                                    exit
                                    """ % (AS_id, vrf_name, interface, neighbor_AS_id)
                                    commands = configs.split('\n')
                                    execute.execute(child, commands)
                                    child.sendcontrol('m')
                            child.sendline('exit')
                            child.sendcontrol('m')

                        else:
                            interface = Interface
                            configs = """
                            configure terminal
                            router bgp %d
                            address-family ipv4 vrf %s
                            neighbor %s remote-as %s
                            neighbor %s activate
                            exit-address-family
                            exit
                            exit
                            """ % (AS_id, vrf_name, interface, neighbor_AS_id)
                            commands = configs.split('\n')
                            execute.execute(child, commands)
                            child.sendcontrol('m')

                    else:
                        unconfig = """
                        configure terminal
                        no router bgp %d
                        exit
                        exit
                        """ % (AS_id)
                        commands = unconfig.split('\n')
                        execute.execute(child, commands)
                        child.sendcontrol('m')

                    return True
        elif port == 'zebra':
                    port = "bgpd"
                    device_data = getdata.get_data()
                    IP_add = device_data['Device_Details'][Device]['ip_add']
                    child = pexpect.spawn('telnet ' + IP_add + ' ' + port)
                    hostname = device_data['Device_Details'][Device]['Hostname']
                    clear_buffer.flushBuffer(10, child)

                    child.sendcontrol('m')
                    flag = (child.expect(['bgpd*', 'Password*', \
                            pexpect.EOF, pexpect.TIMEOUT], timeout=100))
                    if flag == 1:
                        child.send('zebra')
                        child.sendcontrol('m')
                        flag = child.expect(['bgpd*>', pexpect.EOF, \
                               pexpect.TIMEOUT], timeout=50)
                        if flag == 0:
                            child.send('enable')
                            child.sendcontrol('m')

                            if child:
                               flag = child.expect(['bgpd#*', pexpect.EOF, \
                                                pexpect.TIMEOUT], timeout=90)
                               if flag == 0:
                                   Dev.Login(Device, child)
                                   if Action == 'enable':
                                       if isinstance(Interface, list):
                                           for interface in Interface:
                                               configs = """
                                               configure terminal
                                               router bgp %d
                                               neighbor %s remote-as %d
                                               exit
                                               exit
                                               """ % (AS_id, interface, neighbor_AS_id, NW_id)
                                               commands = configs.split('\n')
                                               execute.execute(child, commands)
                                               time.sleep(6)
                                               child.sendcontrol('m')
                                               child.sendline('exit')
                                               child.sendcontrol('m')

                                       else:
                                           interface = Interface
                                           configs = """
                                           configure terminal
                                           router bgp %d
                                           neighbor %s remote-as %d
                                           exit
                                           exit
                                           """ % (AS_id, interface, neighbor_AS_id, NW_id)
                                           commands = configs.split('\n')
                                           execute.execute(child, commands)
                                           child.sendcontrol('m')

                                   else:
                                           unconfig = """
                                           configure terminal
                                           no router bgp %d
                                           exit
                                           exit
                                           """ % (AS_id)
                                           commands = unconfig.split('\n')
                                           execute.execute(child, commands)
                                           child.sendcontrol('m')


                                   return True

        else:
            return False
=======
>>>>>>> 942ffe0c3e437b1d5f576ad194937b80eaf152e9

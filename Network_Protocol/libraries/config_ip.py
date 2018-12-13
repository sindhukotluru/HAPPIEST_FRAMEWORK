import sys
from time import sleep
import re
from threading import Thread
import Devices
import OSPF
import IBGP
import operational_ph

class config_ip(object):

    @staticmethod
    def config_ip_addr(*args):
        """args[0] is Router name ex., R1
           args[1] is Router link ex., Link_R1_R2
           args[2] has options 'configure'/ """

        dev = Devices.Devices()
        sys.stdout.write("Configuring IP address for %s" % args[0])
        status = dev.set_IP(args[0], args[1], args[2])
        if status is False:
            sys.stdout.write("Configuration of IP Address for %s Failed" % args[0])
        else:
            sys.stdout.write("Configured  IP Address for %s" % args[0])

    @staticmethod
    def config_host_addr(*args):
        dev = Devices.Devices()
        dev.set_IP_Host(args[0], args[1], args[2])

    @staticmethod
    def config_docker_addr(*args):
        dev = Devices.Devices()
        dev.set_IP_DockerHost(args[0], args[1], args[2])

    @staticmethod
    def config_lo_addr(*args):
        dev = Devices.Devices()
        dev.set_loopback(args[0], args[1])

    @staticmethod
    def config_ospf(*args):
        ospf = OSPF.OSPF()
        ospf.Configure_ospf(args[0], args[1], args[2], args[3], args[4])

    @staticmethod
    def config_ibgp(*args):
        ibgp = IBGP.IBGP()
        ibgp.Configure_IBGP(args[0], args[1], args[2], args[3])

    @staticmethod
    def ibgp_sync(*args):
        ibgp = IBGP.IBGP()
        ibgp.enable_syn(args[0], args[1])

    @staticmethod
    def enable_ebgp(*args):
        ibgp = IBGP.IBGP()
        ibgp.Configure_EBGP(args[0], args[1], args[2], args[3], args[4], args[5], args[6])

    @staticmethod
    def loopback_advertise(*args):
        ibgp = IBGP.IBGP()
        ibgp.advertising_loopback(args[0], args[1], args[2], args[3])

    @staticmethod
    def route_establish(*args):
        ibgp = IBGP.IBGP()
        ibgp.route(args[0], args[1], args[2])

    @staticmethod
    def ospf_redistribute(*args):
        ibgp = IBGP.IBGP()
        ibgp.redistribution(args[0], args[1], args[2])

    @staticmethod
    def connected_redistribute(*args):
        ibgp = IBGP.IBGP()
        ibgp.redistribution_connected(args[0], args[1])

    @staticmethod
    def show_ip(*args):
        operational_ph.checking_operabilty(args[0], args[1])

    @staticmethod
    def show_ip_ospf(*args):
        operational_ph.checking_operabilty_ospf(args[0], args[1])

    @staticmethod
    def show_bgp(*args):
        operational_ph.checking_operabilty_bgp(args[0], args[1])

    def start_configure(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                                Thread(target=config_ip.config_ip_addr, \
                                args=[device[0], device[1], device[2]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                                               "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
            elif re.search('PC.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                                Thread(target=config_ip.config_host_addr,\
                                args=[device[0], device[1], device[2]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                                               "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
            elif re.search('Ubuntu*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                                Thread(target=config_ip.config_docker_addr,\
                                args=[device[0], device[1], device[2]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                                               "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def start_configure_loopback(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                               Thread(target=config_ip.config_lo_addr,\
                               args=[device[0], device[1]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                                               "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def start_configure_ospf(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                               Thread(target=config_ip.config_ospf,\
                               args=[device[0], device[1], device[2], device[3], device[4]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                                      "ConfigureRouter_" + str(device[0])
                sleep(2)
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def start_ibgp(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                    Thread(target=config_ip.config_ibgp,\
                    args=[device[0], device[1], device[2], device[3]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                               "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def enable_sync(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                Thread(target=config_ip.ibgp_sync, args=[device[0], device[1]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def ebgp_configure(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                Thread(target=config_ip.enable_ebgp, args=[device[0], device[1], \
                device[2], device[3], device[4], device[5], device[6]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def advertise_loopback(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                            Thread(target=config_ip.loopback_advertise, \
                            args=[device[0], device[1], device[2], device[3]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                               "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False


    def establish_route(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                               Thread(target=config_ip.route_establish,\
                               args=[device[0], device[1], device[2]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def redistribute_ospf(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = Thread(target=config_ip.ospf_redistribute, args=[device[0], device[1], device[2]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def redistribute_connected(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = Thread(target=config_ip.connected_redistribute, args=[device[0], device[1]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def show_ip_interface(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = Thread(target=config_ip.show_ip, args=[device[0], device[1]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def show_ospf_neighbor(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                      Thread(target=config_ip.show_ip_ospf, args=[device[0], device[1]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                                       "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

    def show_bgp_summary(self, devices):
        threads_device = {}
        list_threads = []
        for device in devices:
            if re.search('R.*', device[0]):
                threads_device["new_thread{0}".format(device[0])] = \
                 Thread(target=config_ip.show_bgp, args=[device[0], device[1]])
                threads_device["new_thread{0}".format(device[0])].start()
                threads_device["new_thread{0}".format(device[0])].name = \
                               "ConfigureRouter_" + str(device[0])
                list_threads.append(threads_device["new_thread{0}".format(device[0])])
        for _thread in list_threads:
            print("Waiting thread #%s" % str(_thread.name))
            _thread.join()

        #make list empty if thread not running
        _list_threads = [t for t in list_threads if t.isAlive()]
        #check list empty
        if not _list_threads:
            return True
        else:
            return False

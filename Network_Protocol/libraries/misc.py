import argparse
import re
import subprocess


def get_opened_ports_on_ip(ip, port_type):
    """
    get opened ports
    :param port_type:
    :return:
    """
    COMMAND_PORTSCAN_PROG = "nmap "
    TCP_PORTS_LIST = '5000'
    COMMAND_PORTSCAN_ARGS_TCP = "-Pn -p " + TCP_PORTS_LIST + " "
    REGEX_PORT_INFO_LINE = "[0-9]*[ ]*(open|open\|filtered)[ ]*[a-zA-Z0-9]*.*"
    ports_protocols = []
    print("Scanning opened " + port_type + " ports on IP: " + ip)
    if (port_type == "TCP"):
        portscan_params = eval('COMMAND_PORTSCAN_ARGS_' + port_type)
        nmap_process = subprocess.Popen(COMMAND_PORTSCAN_PROG + portscan_params +
                                        ip,
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT)
        for line in nmap_process.stdout.readlines():
            if re.search(REGEX_PORT_INFO_LINE, str(line)):
                line = line.decode("utf-8")
                port = line.split('/', 1)[0].strip()
                protocol = line.rsplit(' ', 1)[1].strip()
                protocol = protocol.replace("-", "")
                protocol = protocol.lower()
                print("Found opened port: " + port + " Protocol: " + protocol)
                ports_protocols.append([port, protocol])
        return 0
    else:
        print("Unknown Port type")
        return 1
DESCRIPTION_STRING = ""
DESCRIPTION_USAGE = ""
def main():
    parser = argparse.ArgumentParser(
        description=DESCRIPTION_STRING,
        epilog=DESCRIPTION_USAGE)

    parser.add_argument('-ip', '--ip', help="DUT IP", required=True)
    parser.add_argument('--porttype', help="TCP/UDP", required=True)

    # Parsing command line arguments...
    args = parser.parse_args()

    ip = args.ip
    porttype = args.porttype
    get_opened_ports_on_ip(ip, porttype)

main()

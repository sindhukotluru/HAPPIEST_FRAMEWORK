import re

from SDN.core.interface.cli_interface import SSHConnection
from SDN import config

def capture_server_output():
    pass

def monitor_server_traffic(server_ip, server_username, server_password, client_ip,
                           client_username, client_password, port):

    print("Connecting to Server: {0}".format(server_ip))
    server_conn = SSHConnection(IP=server_ip, username=server_username, password=server_password)
    server_conn.connect()

    # Run iperf server to listed on TCP port. Don't wait for command to complete execution
    iperf_svr_cmd = "iperf -s -p {0}".format(port)
    server_conn.execute_command(iperf_svr_cmd, wait=False)
    #server_conn.execute_command(iperf_svr_cmd)

    # Run iperf client command and pump traffic to server on TCP port
    transmitted_traffic = iperf_client(client_ip=client_ip, username=client_username, password=client_password,
                 server_ip=server_ip, port=port)

    # Open a New server session to kill the iperf server running
    server_conn_2 = SSHConnection(IP=server_ip, username=server_username, password=server_password)
    server_conn_2.connect()
    server_conn_2.execute_command("lsof -i | grep 5001")
    expr = r'iperf \s*(\d*).'
    command_pid = re.search(expr, server_conn_2.resp).groups()[0].strip()
    print("Killing iperf server with PID :" + command_pid)
    server_conn_2.execute_command("kill -9 {0}".format(command_pid))

    received_traffic = server_conn.rc.capture_output(wait=False)
    print("Server Output: \n{0}".format(received_traffic))
    server_conn_2.disconnect()
    server_conn.disconnect()

    return transmitted_traffic, received_traffic


def iperf_client(client_ip, username, password, server_ip, port):
    print("Connecting to Client: {0}".format(client_ip))

    client_conn = SSHConnection(IP=client_ip, username=username, password=password)
    client_conn.connect()

    iperf_client_cmd = "iperf -c {0} -p {1}".format(server_ip, port)
    client_conn.execute_command(iperf_client_cmd)
    print("Traffic Sent from Client:{0} to Server:{1}".format(client_ip, server_ip))
    client_conn.disconnect()
    return client_conn.resp




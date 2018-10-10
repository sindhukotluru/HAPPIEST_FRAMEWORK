# Import Built-In Libraries
import os
import socket
import requests
import re
import subprocess
from colorama import Fore

#Import External Libraries

#Import project specific libraries
import paramiko
import time

def controller_feature_list():
    '''check the active feature list in ODL controller by ssh into karaf console'''
    hostname = '10.22.20.153'
    port = 8101
    username = 'karaf'
    password = 'karaf'
    # pkey_file = None
    controller = '10.22.20.153'
    feature_list = ['odl-config-api', 'odl-openflowjava-protocol', 'odl-config-manager', 'odl-config-netty',
                    'odl-dluxapps-topology', 'odl-openflowplugin-app-topology']

    if __name__ == "__main__":
        # key = paramiko.RSAKey.from_private_key_file(pkey_file)
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=hostname, username=username, password=password, port=8101)
        # s.connect(hostname, port, pkey=key)
        command = "feature:list -i"
        stdin, stdout, stderr = s.exec_command(command)
        output_string = stdout.read()
        match_list = re.findall(r"(?=(" + '|'.join(feature_list) + r"))", output_string)
        for i in feature_list:
            if i in match_list:
                print i + " activated"
                return 1
            else:
                print i + " not activated"
        s.close()

def check_odl_connectivity_byport(odl_ip,odl_port):
    '''check odl controller karaf is up and running by
    checking the ports 6633 listening in the base OS
    where odl is running
    odl_port is the openflowplugin port 6633 is <int> type
    returns: True or False'''
    s = socket.socket()
    print "Attempting to connect to %s on port %s" % (odl_ip, odl_port)
    try:
        output=s.connect_ex((odl_ip, odl_port))
        print output,"Connected to %s on port %s" % (odl_ip, odl_port)
        return True
    except socket.error, e:
        print "Connection to %s on port %s failed: %s" % (odl_ip, odl_port, e)
        return False

def check_http_response(response):
    '''check various REST API response messages'''

    if response==200:
        print response, "The request has succeeded"
    elif response==201:
        print response,"The request has been fulfilled and resulted in a new resource being created"
    elif response==202:
        print response,"The request has been accepted for processing, but the processing has not been completed"
    elif response==203:
        print response,"Non-Authoritative Information"
    elif response==204:
        print response,"The server has fulfilled the request but does not need to return an entity-body"
    elif response==205:
        print response,"The server has fulfilled the request and the user agent SHOULD reset the document view which caused the request to be sent"
    elif response==206:
        print response,"The server has fulfilled the partial GET request for the resource"
    elif response==300:
        print response,"Multiple Choices"
    elif response==301:
        print response,"The requested resource has been assigned a new permanent URI"
    elif response==302:
        print response,"The requested resource resides temporarily under a different URI"
    elif response==303:
        print resposne,"The response to the request can be found under a different URI and SHOULD be retrieved using a GET method on that resource"
    elif response==304:
        print resposne,"response indicates an entity not currently cached"
    elif response==305:
        print response,"The requested resource MUST be accessed through the proxy given by the Location field,use proxy"
    elif response==307:
        print response,"The requested resource resides temporarily under a different URI"
    elif response==400:
        print response,"Bad Request"
    elif response==401:
        print response,"The request requires user authentication"
    elif response==403:
        print response,"Forbidden,The server understood the request, but is refusing to fulfill it."
    elif response==404:
        print response,"The server has not found anything matching the Request-URI"
    elif response==405:
        print response,"The method specified in the Request-Line is not allowed for the resource identified by the Request-URI"
    elif response==406:
        print response,"Not Acceptable"
    elif response==407:
        print response,"Proxy Authentication Required"
    elif response==408:
        print response,"request time out"
    elif response==409:
        print response,"The request could not be completed due to a conflict with the current state of the resource"
    elif response==410:
        print response,"The requested resource is no longer available at the server and no forwarding address is known"
    elif response==411:
        print response,"Length Required"
    elif response==412:
        print response,"pre-condition failed"
    elif response==413:
        print response,"request entity too large"
    elif response==414:
        print response,"request uri too long"
    elif response==415:
        print response,"unsupported media type"
    elif response==416:
        print response,"Requested Range Not Satisfiable"
    elif response==417:
        print response,"Expectation Failed"
    elif response==500:
        print response,"internal server error"
    elif response==501:
        print response,"not implemented,The server does not support the functionality required to fulfill the request."
    elif response==502:
        print response,"bad gateway"
    elif response==503:
        print response,"service unavailable"
    elif response==504:
        print response,"gateway timeout"
    elif response==505:
        print response,"http version not supported"
    else:
        return response

def check_odl_connectivity_rest(odl_ip,odl_port,odl_user,odl_pass):
    '''check odl controller REST apidocs is running by
    checking the restconf url
    returns: True or False'''
    url = "http://"+odl_ip+':'+odl_port+"/restconf"
    try:
        response = requests.get(url,auth=(odl_user,odl_pass))
        status_code = response.status_code
        check_http_response(status_code)

       # if status_code :
       #     print status_code
       #     print "ODL REST interface is up. Connected to %s on url %s" % (odl_ip,url)
       #     return True
    except Exception as e:
        print "ODL REST interface is down. Connection to %s with url %s failed : %s" % (odl_ip,url,e)
        return False


def cbench_get_avg(output):
    '''Get the average value from the cbench result
    returns: responses/sec on success, error on failure'''
    #Regular expression to match the average value from the RESULT captured by
    #cbench_throughput or cbench_latency
    averageRe = re.compile('([0-9.]+)\/[0-9.]+ responses\/s$')
    try:
        mach = averageRe.search(output)
        avgResp = mach.group(1)
        return avgResp
    except Exception as e:
        print "\nRegular expression to get the average value from cbench output RESULT failed." \
              " Error : %s" % (e)


def cbench_throughput(**kwargs):
    '''Cbench throughput test
    returns: throughput on success, None and error on failure'''
    controller_ip = kwargs['controller']
    port = kwargs['port']
    loops = kwargs['loops']
    msPerTest = kwargs['msPerTest']
    macPerSwitch = kwargs['macPerSwitch']
    startupDelay = kwargs['startupDelay']
    warmup = kwargs['warmup']
    switch = kwargs['switch']
    throughput = None
    FNULL = open(os.devnull, 'w')

    try:
        result = subprocess.Popen(['cbench', '-c',
                                   str(controller_ip), '-p',
                                   str(port), '-m',
                                   str(msPerTest), '-l',
                                   str(loops), '-s',
                                   str(switch), '-M',
                                   str(macPerSwitch),
                                   '-t'],stdout=subprocess.PIPE)
        #, stdout=subprocess.PIPE

        output = result.communicate()[0]


        throughput = cbench_get_avg(output)
        #output1 = result.communicate()
        #for i in output1:
        #    print i,
        return throughput
    except Exception as e:
        print "Throughput Testcase Failed for ODL controller IP %s. Error while executing" \
              "cbench command: %s " % (controller_ip,e)
        return throughput

def cbench_latency(**kwargs):
    '''Cbench throughput test
    returns: throughput on success, None and error on failure'''
    controller_ip = kwargs['controller']
    port = kwargs['port']
    loops = kwargs['loops']
    msPerTest = kwargs['msPerTest']
    macPerSwitch = kwargs['macPerSwitch']
    startupDelay = kwargs['startupDelay']
    warmup = kwargs['warmup']
    switch = kwargs['switch']
    latency = None
    FNULL = open(os.devnull, 'w')

    try:
        result = subprocess.Popen(['cbench', '-c',
                                   str(controller_ip), '-p',
                                   str(port), '-m',
                                   str(msPerTest), '-l',
                                   str(loops), '-s',
                                   str(switch), '-M',
                                   str(macPerSwitch)],stdout=subprocess.PIPE)
        #, stdout=subprocess.PIPE

        output = result.communicate()[0]
        latency_respsec = cbench_get_avg(output)
        #output1 = result.communicate()
        #print output1
        #for i in output1:
        #    print i,
        #    continue
        #Latency = Test Iteration Duration (milliseconds)/Number of OpenFlow Responses Received from Controller
        if latency_respsec != None:
            latency = float(latency_respsec)/msPerTest
        return latency
    except Exception as e:
        print "Latency Testcase Failed for ODL controller IP %s. Error while executing" \
              "cbench command: %s " % (controller_ip,e)
        return latency

def incremental(**kwargs):
        max_switch=kwargs['switch']
        avgThroughputlist=[]
        #odl
        for i in range(1,max_switch):
            avgThroughput = cbench_throughput(**kwargs)
            avgThroughputlist.append(avgThroughput)
        # get average mean
        avgMean= sum(avgThroughputlist) / float(len(avgThroughputlist))
        return avgMean






#testSdn = SdnBenchmarking ()

#l=testSdn.cbench_throughput(controller = '10.22.20.183',
#                  port = '6633',
#                  loops = 5,
#                  msPerTest = 1000,
#                  macPerSwitch = 100,
#                  startupDelay = 100,
#                  warmup = 1,
#                  switch = 5)
#print l

#testSdn.check_odl_connectivity_rest('10.22.20.153','8181','admin','admin')
#testSdn.check_odl_connectivity_byport('10.22.20.153',6633)
#testSdn.check_odl_connectivity_byport('10.22.20.183',6633)
#testSdn.controller_feature_list()

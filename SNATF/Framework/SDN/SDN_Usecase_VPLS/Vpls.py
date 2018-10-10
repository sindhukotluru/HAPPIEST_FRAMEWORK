import paramiko
import time
import re

def controller_feature_list(apps_list):
    '''check the active feature list in ODL controller by ssh into karaf console'''

    feature_list = ['org.onosproject.drivers','org.onosproject.vpls', 'org.onosproject.openflow', 'org.onosproject.proxyarp', 'org.onosproject.mobility']
    #output_string = execute_command("apps -s -a")
    match_list=[]
    #match_list = re.findall(r"(?=(" + '|'.join(feature_list) + r"))", output_string)

    for i in feature_list:
        pattern = re.compile(i)
        match_output = pattern.findall(apps_list)
        match_list.extend(match_output)
    print match_list.group()


    #if "org.onosproject.fwd" in match_list:
    #    execute_command('app deactivate org.onosproject.fwd')
    #elif "org.onosproject.vpls" not in match_list:
     #   execute_command("app activate org.onosproject.vpls")
     #   print "org.onosproject.vpls activated"
    #else:
     #   print "required apps found"



mininet_topology="sudo mn --custom mininet/custom/simpletopo.py --topo=mytopo --controller=remote,ip=10.22.20.178"

hosts_list1=[]

def configure_interface(hosts):

        hosts_list = re.findall(r'[\[a-z]+\:\d+\/\d+\]', hosts)
        new_list=[]
        for i in range(len(hosts_list)):
            cmd = "interface-add -v {0}00 of:000000000000000{0}/{1} h{0}".format(hosts_list[i][19], hosts_list[i][21])
            new_list.append(cmd)
        return new_list



vpls_name="VPLS"

def create_vpls():
    vpls_name="VPLS"

    new_hostlist=[]
    for i in range(1,5):
        vpls_add_host = "vpls add-if {0} h{1}".format(vpls_name, i)
        new_hostlist.append(vpls_add_host)

    return new_hostlist


def add_encap():
    encap_cmd='vpls set-encap {0} {1}'.format(vpls_name,'MPLS')
    execute_command(encap_cmd)
    intents_list=execute_command("intents")
    verify_encap=re.search(r"{encapType=MPLS}",intents_list)
    if verify_encap:
        print "MPLS encapsulation success"
    else: print "packet not encapsulated"





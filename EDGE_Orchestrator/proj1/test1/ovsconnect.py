'''
Created on Apr 27, 2018

@author: Debiprasanna.M
'''
#-------------------------------------------------------
#importing modules
import paramiko
import time
import re


#pdb.set_trace()

# setting parameters like host IP, username, passwd and number of iteration
# to gather cmds
HOST = "10.16.82.125"
USER = "edge"
PASS = "edge123"
PORT = 22
#A function that logins and execute commands
def fn():
    client1=paramiko.SSHClient()
    #add missing client key
    client1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #connect to switch
    client1.connect(HOST,username=USER,password=PASS,port=PORT)
    print "SSH connection to %s established" %HOST
    remote_conn = client1.invoke_shell()
    remote_conn.send("sudo -i\n")
    time.sleep(1)
    remote_conn.send("edge123\n")
    time.sleep(2)
    remote_conn.send("ovs-ofctl dump-flows S1 \n")
    time.sleep(2)
    output = remote_conn.recv(10000)
    time.sleep(2)
    print output
    time.sleep(2)
#     output1=remote_conn.send(cmdq)
#     time.sleep(2)
#     output1 = remote_conn.recv(10000)
#     time.sleep(2)
#     #print output1
#     b =  re.findall("[rt]x pkts=([0-9]+)",output1)
#     print b
#     client1.close()  
    return output


#-------------------------------------------------------
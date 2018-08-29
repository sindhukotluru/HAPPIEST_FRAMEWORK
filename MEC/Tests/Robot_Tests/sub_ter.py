#!/usr/bin/python
import subprocess
cmd = 'ping 192.168.203.21'
proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ''
while True:
    delta = proc.stdout.readline()
    print ">>>>>>> %s"%delta
    output = output + delta
    result = proc.poll()
    if result is not None:
    #    print 'terminated'
        break
#    if 'Unreachable' in output:
    if 'icmp_seq=1' in output:
        proc.terminate()
        break

    else:
#        output = output + delta
        continue
print output

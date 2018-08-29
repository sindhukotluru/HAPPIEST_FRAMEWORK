#!/usr/bin/python
import subprocess
cmd = 'ping 192.168.203.29'
proc = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
output = ''
while True:
    result = proc.poll()
    print ">>>>>>>>>>>%s"%result
    delta = proc.stdout.read(1)
    delta1 = proc.stdout.readline()
    print ">>>>>>>>>>>%s"%delta1
    if result is not None:
        print 'terminated'
        break

    if delta != ' ':
        output = output + delta
    else:
        if '%' in output:
            print 'percentage is:'
            print output

        elif '/s' in output:
            print 'speed is:'
            print output

        print 'output is:'
        print output
        output = ''


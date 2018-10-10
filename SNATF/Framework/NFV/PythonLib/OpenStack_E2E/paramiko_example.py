import paramiko
import re
k = paramiko.RSAKey.from_private_key_file("/userkey.pem")
H1 = paramiko.SSHClient()
H1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "connecting to H1"
H1.connect( hostname = "10.22.20.225", username = "ubuntu", pkey = k )
print "connected to H1"
print "Executing ping to H2 from H1"
a="10.10.2.3"
stdin , stdout, stderr = H1.exec_command("ping -c 5 {}".format(a))
ping=stdout.read()
print"{}".format(ping)
m=re.search(r'100% packet loss',ping)
if m:
    print "Ping fails to H2 from H1"
else:
    print "Ping success to H2 from H1"

H2 = paramiko.SSHClient()
H2.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print "connecting to H2"
H2.connect( hostname = "10.22.20.226", username = "ubuntu", pkey = k )
print "connected to H2"
print "Executing ping to H1 from H2"
stdin , stdout, stderr = H2.exec_command("ping -c 5 10.10.0.3")
ping1=stdout.read()
print"{}".format(ping1)
m1=re.search(r'100% packet loss',ping)
if m1:
    print "Ping fails to H1 from H2"
else:
    print "Ping success to H1 from H2"
H1.close()
H2.close()

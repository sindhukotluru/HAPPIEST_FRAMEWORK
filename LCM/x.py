print "hello"
import subprocess
#subprocess.call(["ls", "-l", "/etc/resolv.conf"])
subprocess.call(["cat", "/home/test/.ssh/known_hosts"])
#subprocess.call(["cat", "/dev/null", ">", "/home/test/.ssh/known_hosts"])
subprocess.call(["cp", "/dev/null", "/home/test/.ssh/known_hosts"])
subprocess.call(["cat", "/home/test/.ssh/known_hosts"])

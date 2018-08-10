from pexpect import pxssh
import getpass

s = pxssh.pxssh()
s.force_password = True
hostname = raw_input('hostname: ')
username = raw_input('username: ')
password = getpass.getpass('password: ')
s.login(hostname, username, password)

# try:
#     s = pxssh.pxssh()
#     # hostname = raw_input('hostname: ')
#     # username = raw_input('username: ')
#     # password = getpass.getpass('password: ')
#     # s.interact()
#     s.login('10.16.84.236', 'vyos', 'vyos')
#     s.interact()
#     #s.prompt('$')
#     s.sendline('show login')   # run a command
#     s.prompt()             # match the prompt
#     print(s.before)        # print everything before the prompt.
#     # s.sendline('show system login')
#     # s.prompt('#')
#     # print(s.before)
#     # s.sendline('df')
#     # s.prompt()
#     # print(s.before)
#     s.logout()
# except pxssh.ExceptionPxssh as e:
#     print("pxssh failed on login.")
#     print(e)




#import vymgmt

#vyos = vymgmt.Router('10.16.84.236', 'vyos', password='vyos', port=22)

#vyos.login()
#vyos.configure()

#vyos.set("protocols static route 203.0.113.0/25 next-hop 192.0.2.20")
#vyos.delete("system options reboot-on-panic")
#vyos.set("show system")

#vyos.commit()
#vyos.save()
#vyos.exit()
#vyos.logout()












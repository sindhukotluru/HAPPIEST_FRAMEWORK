import pexpect

def execute(child, commands):
  cmds = commands
  flushedStuff = ''
  while not child.expect([r'.+', pexpect.EOF, pexpect.TIMEOUT], timeout=5):
    try:
        flushedStuff += child.match.group(0)
    except TypeError as e:
        pass
#  child.expect(['configure terminal',pexpect.EOF,pexpect.TIMEOUT],timeout=60)
  for cmd in cmds:
      child.send(cmd)
      child.sendcontrol('m')
      child.sendcontrol('m')
  child.expect(['exit', pexpect.EOF, pexpect.TIMEOUT], timeout=5)
  child.sendcontrol('m')
  child.sendcontrol('m')
  print(child.before.decode("utf-8"))
  return

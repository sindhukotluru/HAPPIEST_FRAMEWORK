import logging
import os
import re
import sys
import datetime
import inspect
import config


class Logger(object):
    cwd = os.getcwd()
    log_path = config.LOG_PATH
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    stack = inspect.stack()
    stack.reverse()
    reg = None
    i = 0
    for i in stack:
        if cwd in str(i) and str(__file__) not in str(i):
           reg = re.search(r'%s/(.*py)'%cwd,str(i))
           break
    if reg is not None:
        pyname = reg.group(1)
    else:
        pyname = sys.argv[len(sys.argv)-1]
    file_format = "%s.log" % (pyname.split('/')[len(pyname.split('/')) - 1].split(".")[0])
    _log_file = "%s/%s" % (log_path, file_format)
     
    def __init__(self,logger):
        self.logger = logger
        self.logger.setLevel(logging.DEBUG)
        date_fmt = '%d-%m-%Y %H:%M:%S'
        self.CMD_FROM = {'cmd_from': 'HM-SDN-NFV'}
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',date_fmt)
        if config.GEN_LOG == True:
            handler = logging.FileHandler('%s'%self._log_file)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def writeTolog(self,msg,level=20):
        if config.GEN_LOG == True:
            self.logger.log(level,'  %s\n'%msg)

    def writeDebuglog(self,msg):
        return self.writeTolog(msg, level=10)

    def writeInfolog(self,msg):
        return self.writeTolog(msg,level=20)

    def writeWarnlog(self,msg):
        return self.writeTolog(msg, level=30)

    def writeErrorlog(self,msg):
        return self.writeTolog(msg, level=40)

    def writeCriticallog(self,msg):
        return self.writeTolog(msg, level=60)

loggers = {}
def fill_getLogger(name):
    """
    To update the logger name which is to track called module
    """
    global loggers
    if loggers.get(name):
        return loggers.get(name)
    else:
        logger = logging.getLogger(name)
        log_handler = Logger(logger)
        loggers[name]=log_handler
        return log_handler

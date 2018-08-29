from Supporting_Libs.cli_interface import SSHConnection
from Supporting_Libs.log_generate import fill_getLogger
from Config import config
import re

class Karaf(SSHConnection):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self, *args, **kwargs):
        super(Karaf, self).__init__(*args, **kwargs)
        self.IP = kwargs['IP']
        self.usr = kwargs['username']
        self.pwd = kwargs['password']
        self.connect()
        self.logger_name = __name__.split('.')[-1]
        self.log_handler = fill_getLogger(self.logger_name)
        self.log_handler.writeInfolog('************* SSH to CONTROLLER %s *************' % kwargs["IP"])

    def start_karaf(self, clean=None):
        """
        To start Karaf from provided path
        """
        cmd = config.ODL_PATH+"/karaf"
        if clean is not None:  cmd = config.ODL_PATH+"/karaf clean"
        result = False
        if self.stop_kraf():
            if self.execute_command(cmd=cmd,prompt='>'):
                self.log_handler.writeTolog(msg="****** ODL KARAF started Successfully ******")
                result = True
            else:
                self.log_handler.writeTolog(msg="****** ODL KARAF FAILED to start !!! ******")
        return result

    def stop_kraf(self):
        """
        To Stop the existing KARAF process
        """
        cmd = config.ODL_PATH + "/stop"
        if self.execute_command(cmd=cmd, prompt='#'):
            command_output = self.rc.resp
            if re.search('The container is not running',command_output):
                self.log_handler.writeTolog(msg="****** ODL KARAF stopped Successfully ******")
            return True
        else:
            self.log_handler.writeTolog(msg="****** ODL KARAF FAILED to STOP !!! ******")
            return False

    def configure_plugins(self,config_flag):
        """
        To install Plugins
        """
        cmd = ''
        if config_flag == 'install':
            cmd = "feature:install "
        elif config_flag == 'uninstall':
            cmd = "feature:uninstall "
        else:
            self.log_handler.writeTolog(msg="****** INVALID config_flag, please provide either 'install' or 'uninstall' ******")
            return False
        for plugin in config.ODL_PLUGINS:
            cmd = cmd + plugin + ' '
        if self.execute_command(cmd=cmd,exp_out='Error'):
            self.log_handler.writeTolog(msg="****** FAILED to INSTALL Plugins in ODL KARAF !!!******")
            return False
        else:
            self.log_handler.writeTolog(msg="****** INSTALLED Plugins in ODL KARAF Successfully******")
            return True
 
    def veerify_installed_plugins(self):
        """
        To verify the installed plugins in karaf
        """
        cmd = "feature:list"
        error_flag = 0
        for plugin in config.ODL_PLUGINS:
            pattern = "{0}\s+\|.*\|\s*x\s+\|".format(plugin)
            if self.execute_command(cmd=cmd,exp_out=pattern):
                continue
            else:
                self.log_handler.writeTolog(msg="****** PLUGIN is NOT INSTALLED Properly, Verification FAILED ******")
                error_flag += 1    
        return False if error_flag > 0 else True

    def exit_from_karaf(self):
        """
        To come out of KARAF prompt
        """
        if self.execute_command(cmd='logout', prompt = '#'):
            self.log_handler.writeTolog(msg="****** EXITED From KARAF Prompt Successfully ******")
            return True
        else:
            self.log_handler.writeTolog(msg="****** FAILED To EXIT From KARAF Prompt !!! ******")
            return False

    def karaf_excute_command(self,cmd,exp_out=None,prompt='#'):
        result = self.execute_command(cmd=cmd,exp_out=exp_out,prompt=prompt)
        self.resp = self.resp
        return result

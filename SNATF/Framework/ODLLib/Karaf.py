import sys
sys.path.insert(0,'/home/test/SNATF/Framework/CliLib')
sys.path.append('/home/test/SNATF/TestRepository/Config')
from cli_interface import SSHConnection
from log_generate import fill_getLogger
import ControllerConfig
import re,time

class Karaf(SSHConnection):

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    _prompt = 'opendaylight-user'
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
        cmd = ControllerConfig.ODL_PATH+"/karaf"
        if clean is not None:  cmd = ControllerConfig.ODL_PATH+"/karaf clean"
        result = False
        if self.stop_kraf():
            time.sleep(5)
            if self.execute_command(cmd=cmd,prompt=self._prompt):
                self.log_handler.writeInfolog(msg="****** ODL KARAF started Successfully ******")
                result = True
            else:
                self.log_handler.writeErrorlog(msg="****** ODL KARAF FAILED to start !!! ******")
        return result

    def stop_kraf(self):
        """
        To Stop the existing KARAF process
        """
        cmd = ControllerConfig.ODL_PATH + "/stop"
        if self.execute_command(cmd=cmd, prompt='#'):
            self.log_handler.writeInfolog(msg="****** ODL KARAF stopped Successfully ******")
            cmd = ControllerConfig.ODL_PATH + "/status"
            self.execute_command(cmd=cmd, prompt='#')
            self.log_handler.writeInfolog(self.resp)
            self.log_handler.writeInfolog(msg="****** ODL KARAF stopped Successfully ******")
            return True
        else:
            self.log_handler.writeErrorlog(msg="****** ODL KARAF FAILED to STOP !!! ******")
            return False

    def configure_plugins(self,config_flag,plugins):
        """
        To install Plugins
        """
        cmd = ''
        if config_flag == 'install':
            cmd = "feature:install "
        elif config_flag == 'uninstall':
            cmd = "feature:uninstall "
        else:
            self.log_handler.writeErrorlog(msg="****** INVALID config_flag, please provide either 'install' or 'uninstall' ******")
            return False
        for plugin in plugins:
            cmd = cmd + plugin + ' '
        if self.execute_command(cmd=cmd,prompt=self._prompt):
            self.log_handler.writeInfolog(msg="****** INSTALLED Plugins in ODL KARAF Successfully******")
            return True
        else:
            self.log_handler.writeErrorlog(msg="****** FAILED to INSTALL Plugins in ODL KARAF !!!******")
            return False
 
    def verify_installed_plugins(self,plugins):
        """
        To verify the installed plugins in karaf
        """
        cmd = "feature:list -r"
        error_flag = 0
        if self.execute_command(cmd=cmd,prompt=self._prompt):
            for plugin in plugins:
                if re.search(plugin,self.resp):
                    continue
                else:
                    self.log_handler.writeErrorlog(msg="****** PLUGIN:{0} is NOT INSTALLED Properly, Verification FAILED ******".format(plugin))
                    error_flag += 1    
        if error_flag > 0:return True
        else:
            self.log_handler.writeInfolog(msg="****** Installed Plugins are verified properly ******")
            return True

    def exit_from_karaf(self):
        """
        To come out of KARAF prompt
        """
        if self.execute_command(cmd='logout', prompt = '#'):
            self.log_handler.writeInfolog(msg="****** EXITED From KARAF Prompt Successfully ******")
            return True
        else:
            self.log_handler.writeErrorlog(msg="****** FAILED To EXIT From KARAF Prompt !!! ******")
            return False

    def karaf_excute_command(self,cmd,exp_out=None,prompt='#'):
        result = self.execute_command(cmd=cmd,exp_out=exp_out,prompt=prompt)
        self.resp = self.resp
        return result

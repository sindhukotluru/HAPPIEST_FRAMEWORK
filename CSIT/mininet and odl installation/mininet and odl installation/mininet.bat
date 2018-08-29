@ECHO OFF
set drive = "E:"
set mininet_download_folder = "Downloads"
set mininet_download_URL = "http://downloads.mininet.org"
set mininet_download_file_name = "mininet-2.2.1-150420-ubuntu-14.04-server-amd64.zip"
%drive%
cd %drive%\
cd mininet_download_folder
wget %mininet_download_URL%/%mininet_download_file_name% --no-check-certificate
7z x %mininet_download_file_name%
cd mn-master-trusty64server-150420-00-11-02
@ECHO OFF
VBoxManage import mininet-2.2.1-150420-ubuntu-14.04-server-amd64.ovf
@ECHO OFF
VBoxManage startvm Mininet-VM
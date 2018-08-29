*** Settings ***
Documentation     Test Case To Verify FTP Traffic
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library           ../../../util_findhost.py
Library           ../../../test_vnf.py
Resource          ../../library/vnf_service.robot
Variables         ../../variables/vnf_config.py

*** Variables ***


*** Test Cases ***
DEVSTACK - Validate FTP Traffic
    [Documentation]    Make a connection to Devstack VM and validate Load Balance
    ${status1}    Test Traffic Ftp Success   ${vm_ip[0]}    ${vm_ip[4]}

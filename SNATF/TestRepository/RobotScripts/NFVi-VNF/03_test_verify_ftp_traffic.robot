*** Settings ***
Documentation     Test Case To Verify FTP Traffic
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library           ../../../Framework/NFV/PythonLib/NFVi-VNF/NFVi-VNF_util_findhost.py
Library           ../../../Framework/NFV/PythonLib/NFVi-VNF/test_NFVi-VNF.py
Resource          ../../../Framework/NFV/NFVi-VNF/NFVi-VNF_service.robot
Variables         ../../Variables/NFVi-VNF_variables.py

*** Variables ***


*** Test Cases ***
DEVSTACK - Validate FTP Traffic
    [Documentation]    Make a connection to Devstack VM and validate Load Balance
    ${status1}    Test Traffic Ftp Success   ${vm_ip[0]}    ${vm_ip[4]}

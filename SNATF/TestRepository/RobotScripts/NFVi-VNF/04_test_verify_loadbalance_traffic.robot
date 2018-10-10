*** Settings ***
Documentation     Test Case To Verify Load Balancing
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
DEVSTACK - Validate Load Balance Traffic
    [Documentation]    Make a connection to Devstack VM and validate Load Balance
    ${status1}    Test Load Balance   ${vm_ip[0]}    ${vm_ip[2]}    ${vm_ip[4]}    ${vm_ip[5]}

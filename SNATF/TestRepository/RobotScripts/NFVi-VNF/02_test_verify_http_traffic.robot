*** Settings ***
Documentation     Test Case To Verify HTTP Traffic On DEVSTACK
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library           ../../../Framework/NFV/PythonLib/NFVi-VNF/NFVi-VNF_util_findhost.py
Library           ../../../Framework/NFV/PythonLib/NFVi-VNF/test_NFVi-VNF.py
Resource          ../../../Framework/NFV/NFVi-VNF/NFVi-VNF_service.robot
Variables         ../../Variables/NFVi-VNF_variables.py


*** Variables ***
${vm1_name}       CLIENT1
${vm2_name}       FIREWALL
${vm3_name}       HA_PROXY
${vm4_name}       CLIENT2
${vm5_name}       SERVER1
${vm6_name}       SERVER2


*** Test Cases ***
DEVSTACK - Validate HTTP Traffic
    [Documentation]    Make a connection to Devstack VM and validate HTTP Traffic
    ${status1}   Test Traffic Http Success   ${vm_ip[0]}   ${vm_ip[4]}
    Sleep  60
    ${status2}   Test Traffic Http Failure   ${vm_ip[0]}   ${vm_ip[4]}

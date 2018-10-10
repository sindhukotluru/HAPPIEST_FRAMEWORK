*** Settings ***
Documentation     Test Vnf SNORT Scenarios:-Multiple Hosts Covering Single firewall Interface
#Library           OperatingSystem
#Library           RequestsLibrary
#Library           Collections
#Library           SSHLibrary
#Library		  random
Library            ../../../Framework/NFV/PythonLib/VNF_Certification/util_findhost.py
Library            ../../../Framework/NFV/PythonLib/VNF_Certification/vnf_library.py
#Resource          ../../../library/vnf_service.robot
#Variables         ../../../variables/vnf_config.py

*** Variables ***
${stack_name}     Stack557
#${stack2_name}     multiStack1
#${snapshot_name}  snap1
#${snapshot_name}  catenate    snap     ${suffix}

*** Test Cases ***
OPENSTACK - Validate Snort vnf Scenarios: HTTP Allow Server1 Block Server2 Test
    [Documentation]    Test HTTP
    Vnf Allow1 Http Test Multi    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: HTTP Block Server1 Allow Server2 Test
    [Documentation]    Test HTTP
    Vnf Block1 Http Test Multi    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: HTTP Allow Test
    [Documentation]    Test HTTP
    Vnf Allallow Http Test Multi    ${stack_name}
OPENSTACK - Validate Snort vnf Scenarios: HTTP Block Test
    [Documentation]    Test HTTP
    Vnf Allblock Http Test Multi    ${stack_name}




#OPENSTACK - Validate Vnf Lcm Scenarios: Delete VM
#    [Documentation]    Test VM deletion
#    Vnf Delete Server    ${stack_name}
#OPENSTACK - Validate Vnf Lcm Scenarios: Delete Stack
#    [Documentation]    Test stack deletion
#    Vnf Delete Stack    ${stack_name}

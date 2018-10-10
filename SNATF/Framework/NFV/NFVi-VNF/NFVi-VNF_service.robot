*** Settings ***
Documentation     VNF library. This library is useful to deal with VNF-Devstack.
Library           OperatingSystem
Library           RequestsLibrary
Library           Collections
Library           SSHLibrary
Library           ../../util_findhost.py
Library           ../../test_vnf.py
Variables         ../variables/vnf_config.py



*** Keywords ***
Create Devstack VM
    [Arguments]
    [Documentation]    Will Install Devstack inside the given host
    Install Devstack    ${DEVSTACK2_IP}   ${DEVSTACK2_USER}   ${DEVSTACK2_PSWD}


Connection To Devstack
    [Arguments]   ${host}  ${cmds}
    [Documentation]    Will execute the given ${cmds} by ssh'ing to the Devstack VM console running on ${host}
    ...    Note that this keyword will open&close new SSH connection, without switching back to previously current session.
    Open Connection    ${host}    port=${SSH_PORT}    prompt=${PROMPT}    timeout=${TIMEOUT}
    Login    ${DEVSTACK_USER}    ${DEVSTACK_PSWD}
    Write    ${cmds}
    ${output}    Read Until    ${PROMPT}
    Close Connection
    Log    ${output}
    [Return]    ${output}



DEVSTACK Infrastructure Setup
    [Arguments]   ${vm1}  ${vm2}  ${vm3}  ${vm4}  ${vm5}  ${vm6}
    [Documentation]    Make a connection to Devstack VM and configure the required Infrastructure
    @{vm_ip}    Vnf Infrastructure Setup     ${vm1}   ${vm2}   ${vm3}  ${vm4}  ${vm5}  ${vm6}
    [Return]   @{vm_ip}


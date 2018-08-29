*** Settings ***
Documentation     Mininet library. This library is useful for tests using mininet tool to simulate devices.
Library           SSHLibrary
Resource          Utils.robot
Resource          OVSDB.robot
Variables         ../variables/Variables.py

*** Keywords ***
Start Mininet Single Controller
    [Arguments]    ${mininet}=${TOOLS_SYSTEM_IP}    ${controller}=${ODL_SYSTEM_IP}    ${options}=--topo tree,1 --switch ovsk,protocols=OpenFlow13    ${custom}=${EMPTY}    ${ofport}=6633
    [Documentation]    Start Mininet with custom topology and connect to controller.
    Log    Clear any existing mininet
    Utils.Clean Mininet System    ${mininet}
    ${mininet_conn_id}=    SSHLibrary.Open Connection    ${mininet}    prompt=${TOOLS_SYSTEM_PROMPT}    timeout=${DEFAULT_TIMEOUT}
    Set Suite Variable    ${mininet_conn_id}
    Utils.Flexible Mininet Login
    Run Keyword If    '${custom}' != '${EMPTY}'    Put File    ${custom}
    Log    Start mininet ${options} to ${controller}
    SSHLibrary.Write    sudo mn --controller 'remote,ip=${controller},port=${ofport}' ${options}
    SSHLibrary.Read Until    mininet>
    ${output}=    Utils.Run Command On Mininet    ${mininet}    sudo ovs-vsctl show
    Log    ${output}
    [Return]    ${mininet_conn_id}

Start Mininet Multiple Controllers
    [Arguments]    ${mininet}    ${controller_index_list}    ${options}=--topo tree,1 --switch ovsk,protocols=OpenFlow13    ${custom}=${EMPTY}    ${ofport}=6633
    [Documentation]    Start Mininet with custom topology and connect to all controllers in the ${controller_index_list}.
    Log    Clear any existing mininet
    Utils.Clean Mininet System    ${mininet}
    ${mininet_conn_id}=    SSHLibrary.Open Connection    ${mininet}    prompt=${TOOLS_SYSTEM_PROMPT}    timeout=${DEFAULT_TIMEOUT}
    Set Suite Variable    ${mininet_conn_id}
    Utils.Flexible Mininet Login
    Run Keyword If    '${custom}' != '${EMPTY}'    Put File    ${custom}
    Log    Start mininet ${options}
    SSHLibrary.Write    sudo mn ${options}
    SSHLibrary.Read Until    mininet>
    Log    Create controller configuration
    ${controller_opt}=    Set Variable
    : FOR    ${index}    IN    @{controller_index_list}
    \    ${controller_opt}=    Catenate    ${controller_opt}    ${SPACE}tcp:${ODL_SYSTEM_${index}_IP}:${ofport}
    \    Log    ${controller_opt}
    Log    Find Number of OVS bridges
    ${num_bridges}    Utils.Run Command On Mininet    ${mininet}    sudo ovs-vsctl show | grep Bridge | wc -l
    ${num_bridges}=    Convert To Integer    ${num_bridges}
    Log    Configure OVS controllers ${controller_opt} in all bridges
    : FOR    ${i}    IN RANGE    1    ${num_bridges+1}
    \    ${bridge}=    Utils.Run Command On Mininet    ${mininet}    sudo ovs-vsctl show | grep Bridge | cut -c 12- | sort | head -${i} | tail -1
    \    OVSDB.Set Controller In OVS Bridge    ${mininet}    ${bridge}    ${controller_opt}
    Log    Check OVS configuratiom
    ${output}=    Utils.Run Command On Mininet    ${mininet}    sudo ovs-vsctl show
    Log    ${output}
    [Return]    ${mininet_conn_id}

Send Mininet Command
    [Arguments]    ${mininet_conn_id}    ${cmd}=help
    [Documentation]    Sends Command ${cmd} to Mininet session ${mininet_conn_id} and returns read buffer response.
    SSHLibrary.Switch Connection    ${mininet_conn_id}
    SSHLibrary.Write    ${cmd}
    ${output}=    SSHLibrary.Read Until    mininet>
    [Return]    ${output}

Send Mininet Command Multiple Sessions
    [Arguments]    ${mininet_conn_list}    ${cmd}=help
    [Documentation]    Sends Command ${cmd} to Mininet sessions in ${mininet_conn_list} and returns list of read buffer responses.
    ${output_list}=    Create List
    : FOR    ${mininet_conn_id}    IN    @{mininet_conn_list}
    \    ${output}=    Utils.Send Mininet Command    ${mininet_conn_id}    ${cmd}
    \    Append To List    ${output_list}    ${output}
    [Return]    ${output_list}

Stop Mininet And Exit
    [Arguments]    ${mininet_conn_id}
    [Documentation]    Stops Mininet and exits session ${mininet_conn_id}
    SSHLibrary.Switch Connection    ${mininet_conn_id}
    SSHLibrary.Write    exit
    SSHLibrary.Read Until    ${TOOLS_SYSTEM_PROMPT}
    Close Connection

Stop Mininet And Exit Multiple Sessions
    [Arguments]    ${mininet_conn_list}
    [Documentation]    Stops Mininet and exits sessions in ${mininet_conn_list}.
    : FOR    ${mininet_conn_id}    IN    @{mininet_conn_list}
    \    MininetKeywords.Stop Mininet And Exit    ${mininet_conn_id}

Verify Aggregate Flow From Mininet Session
    [Arguments]    ${mininet_conn_id}    ${switch_count}    ${flow_count}    ${time_out}
    [Documentation]    Verify flow count per switch
    Wait Until Keyword Succeeds    ${time_out}    2s    MininetKeywords.Mininet Sync Status    ${mininet_conn_id}    ${switch_count}    ${flow_count}

Mininet Sync Status
    [Arguments]    ${mininet_id}    ${switch_count}    ${flow_count}
    [Documentation]    Sync with mininet to match exact number of flows
    Set Test Variable    &{dictionary}    flow_count\=${flow_count}=${switch_count}
    ${cmd} =    Set Variable    dpctl dump-aggregate -O OpenFlow13
    ${output}=    MininetKeywords.Send Mininet Command    ${mininet_id}    ${cmd}
    Utils.Check Item Occurrence    ${output}    ${dictionary}


Open Mininet Connection and Login with SSH
    [Arguments]    ${ip}    ${timeout}
    [Documentation]    Opens a connection to Mininet VM and Login using SSH Public key
    ${conn_id}=    Open Connection    ${ip}    prompt=${TOOLS_SYSTEM_PROMPT}    timeout=${timeout}
    Login With Public Key    ${TOOLS_SYSTEM_USER}    ${USER_HOME}/.ssh/${SSH_KEY}    any
    [Return]    ${conn_id}

Set OVS_Manager and Start Mininet Topology
    [Arguments]    ${topo_file}    ${start_cmd}
    [Documentation]    Sets the OVS Manager, transfers the mininet topology file and starts the mininet topology by configuring the controller
    Execute Command    ${OVS_SET_MANAGER}
    Put File    ${topo_file}
    Write    ${start_cmd}
    Read Until    ${TOOLS_MININET_PROMPT}

OVS Add GRE Interface
    [Arguments]    ${port}    ${interface}    ${interface_type}    ${remote_ip}    ${local_ip}
    [Documentation]    Adds GRE interface
    Execute Command    sudo ovs-vsctl add-port ${port} ${interface} -- set interface ${interface} type=${interface_type} options:remote_ip=${remote_ip} options:local_ip=${local_ip}

Validate OVS Manager Version and OpenFlow Versions
    [Arguments]    ${ovs_mgr}    ${ovs_version}    ${OpenFlow_Versions}
    [Documentation]    Verifies The OVS Manager, OVS Version and OpenFlow Versions supported. 
    ${output}    Execute Command    sudo ovs-vsctl show
    Log    ${output}
    Should Contain    ${output}    ${ovs_mgr}
    Should Contain    ${output}    ${ovs_version}
    ${output}    Execute Command    sudo ovs-ofctl --version
    Log    ${output}
    Should Contain    ${output}    ${OpenFlow_Versions}

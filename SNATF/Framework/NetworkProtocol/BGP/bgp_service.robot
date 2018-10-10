*** Settings ***
Documentation     Bgp library. This library is useful to deal with Router BGP Protocol.
Library           SSHLibrary
Library           OperatingSystem
Variables         ../../../TestRepository/Variables/NetworkProtocol_BGPvariables.py 
Resource          bgp_function.robot

*** Variables ***
${HT_NEW}  50
${KAT_NEW}  150
${cmd_t}  timers
${cmd_st}  neighbor ${HOSTR3_INTF} ${cmd_t} ${HT_NEW} ${KAT_NEW}
${cmd_rt}  no neighbor ${HOSTR3_INTF} ${cmd_t}
@{cmd_sn}  redistribute connected   neighbor ${HOSTR2_INTF} remote-as ${AS2}   neighbor ${HOSTR3_INTF} remote-as ${AS2}
@{cmd_rn}  no redistribute connected   no neighbor ${HOSTR2_INTF} remote-as ${AS2}   no neighbor ${HOSTR3_INTF} remote-as ${AS2}
${cmd_rna}  no network ${NWK_ADV} mask ${NWK_MSK}
${cmd_sna}  network ${NWK_ADV} mask ${NWK_MSK}
${cmd_cra}  neighbor ${HOSTR3_INTF} remote-as
@{cmd_sin}  redistribute kernel   redistribute connected   neighbor ${HOSTR1_INTF_2} remote-as ${AS1}
${cmd_sh}  sudo vtysh -c 'show ip bgp neighbors'
${cmd_sh_2}  sudo vtysh -c 'show ip bgp'
${prompt_sl}   MBytes



*** Keywords ***
Connection To Router
    [Arguments]   ${host}  ${cmd}
    [Documentation]    Will execute the given ${cmd} by ssh'ing to the router console running on ${HOSTR2}
    ...    Note that this keyword will open&close new SSH connection, without switching back to previously current session.
    Open Connection    ${host}    port=${SSH_PORT}    prompt=${ROUTER_PROMPT}    timeout=${TIMEOUT}
    Login    ${USER}    ${PASS}
    Write    ${cmd}
    ${output}    Read Until    ${ROUTER_PROMPT}
    Close Connection
    Log    ${output}
    [Return]    ${output}


Refresh Timers Value On Router
    [Arguments]
    [Documentation]    Will refresh the Timers value in bgp configuration
    ${output1}  Modify Bgp Config  ${HOSTR1}  ${AS1}  ${cmd_rt}
    [Return]    ${output1}

Validate Default Timers Value On Router
    [Arguments]    ${match1}
    [Documentation]    Will succeed if the message - ${match1} found in the output
    ${output2}  Connection To Router   ${HOSTR1}  ${cmd_sh}
    Should Contain    ${output2}    ${match1}
    [Return]    ${output2}

Modify Timers Value On Router
    [Arguments]
    [Documentation]    Will modify the Timers value in bgp configuration
    ${output3}  Modify Bgp Config  ${HOSTR1}  ${AS1}  ${cmd_st}
    [Return]    ${output3}


Validate Modified Timers Value On Router
    [Arguments]    ${match2}
    [Documentation]    Will succeed if the message - ${match2} found in the output
    ${output4}  Connection To Router   ${HOSTR1}  ${cmd_sh}
    Should Contain    ${output4}    ${match2}
    [Return]    ${output4}


Refresh Neighbor Details On Router
    [Arguments]
    [Documentation]    Will refresh the Neighbor details in bgp configuration
    ${output5}  Modify Bgp Config  ${HOSTR1}  ${AS1}  @{cmd_rn}
    [Return]    ${output5}


Confirm No Neighbor On Router
    [Arguments]    ${match3}
    [Documentation]    Will succeed if the message - ${match3} not found in the output
    ${output6}  Connection To Router   ${HOSTR1}  ${cmd_sh}
    Should Not Contain    ${output6}    ${match3}
    [Return]    ${output6}


Add Neighbors On Router
    [Arguments]
    [Documentation]    Will add neighbor router in bgp configuration
    ${output7}  Modify Bgp Config  ${HOSTR1}  ${AS1}  @{cmd_sn}
    [Return]    ${output7}


Validate Neighbor On Router
    [Arguments]    ${host}   ${match4}   ${cmd_check}   @{match_n}
    [Documentation]    Will succeed if the message - ${match4} found in the output
    ${output8}  Connection To Router   ${host}  ${cmd_check}
    Should Contain    ${output8}    ${match4}
    : FOR   ${i}   IN    @{match_n}
    \    Should Contain    ${output8}    ${i}
    [Return]    ${output8}


Refresh Network Advertisement On Router
    [Arguments]
    [Documentation]    Will refresh the Network Advertisement in bgp configuration
    ${output9}  Modify Bgp Config  ${HOSTR2}  ${AS2}  ${cmd_rna}
    [Return]    ${output9}


Confirm No Network Advertisement On Router
    [Arguments]    ${match_nadv}
    [Documentation]    Will succeed if the message - ${match_nadv} not found in the output
    ${output10}  Connection To Router   ${HOSTR1}  ${cmd_sh_2}
    Should Not Contain    ${output10}    ${match_nadv}
    [Return]    ${output10}


Add Network Advertisement On Router
    [Arguments]
    [Documentation]    Will add network advertisement in bgp configuration
    ${output11}  Modify Bgp Config  ${HOSTR2}  ${AS2}  ${cmd_sna}
    [Return]    ${output11}


Validate Network Advertisement On Router
    [Arguments]    ${match_nadv}
    [Documentation]    Will succeed if the message - ${match_nadv} found in the output
    ${output12}  Connection To Router   ${HOSTR1}  ${cmd_sh_2}
    Should Contain    ${output12}    ${match_nadv}
    [Return]    ${output12}


Add Internal Neighbors On Router
    [Arguments]
    [Documentation]    Will add internal neighbor router in bgp configuration
    ${output13}  Reset Bgp Config  ${HOSTR3}  ${AS2}  ${AS1}  @{cmd_sin}
    ${output14}  Modify Bgp Config  ${HOSTR1}   ${AS1}   ${cmd_cra} ${AS1}
    [Return]    ${output13}  ${output14}


Reset Neighbor
    [Arguments]
    [Documentation]    Will reset neighbor bgp configuration
    ${output15}  Reset Bgp Config  ${HOSTR3}  ${AS1}  ${AS2}  @{cmd_sin}
    ${output16}  Modify Bgp Config  ${HOSTR1}  ${AS1}  @{cmd_sn}
    [Return]    ${output15}  ${output16}


Initiate And Validate Traffic
    [Arguments]  ${host1}   ${host2}   ${cmd_trf2}   ${cmd_trf1}  ${match_trfc}
    [Documentation]    Will initiate the Traffic on Router
    Open Connection    ${host2}    port=${SSH_PORT}    prompt=${ROUTER_PROMPT}    timeout=${TIMEOUT}   alias=2
    Login    ${USER}    ${PASS}
    Write    ${cmd_trf2}
    Open Connection    ${host1}    port=${SSH_PORT}    prompt=${ROUTER_PROMPT}    timeout=${TIMEOUT}   alias=1
    Login    ${USER}    ${PASS}
    Write    ${cmd_trf1}
    Sleep  ${SLEEP_TIME}
    ${output17}    Read Until    ${ROUTER_PROMPT}
    Close Connection
    Log    ${output17}
    Switch Connection  2
    Sleep  ${SLEEP_TIME}
    ${output18}    Read Until    ${prompt_sl}
    Close Connection
    Log    ${output18}
    Should Contain    ${output17}    ${match_trfc}
    Should Contain    ${output18}    ${match_trfc}
    [Return]    ${output17}  ${output18}


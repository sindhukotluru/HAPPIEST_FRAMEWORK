*** Settings ***
Documentation     Bgp library. This library is useful to deal with Router BGP Protocol.
Library           SSHLibrary
Library           OperatingSystem
Variables         ../../../TestRepository/Variables/NetworkProtocol_BGPvariables.py 


*** Variables ***
${cmd}  telnet localhost bgpd
${cmd1}  en
${cmd2}  conf t
${cmd3}  router bgp
${cmd4}  write
${cmd5}  exit
${cmd6}  sudo /etc/init.d/quagga restart
${expected1}  Password:
${expected2}  >
${expected3}  \#
${expected4}  Configuration saved to /etc/quagga/bgpd.conf


*** Keywords ***
Modify Bgp Config
    [Arguments]   ${host}  ${as}  @{commands}
    [Documentation]    Will modify the bgp configuration
    Open Connection    ${host}    port=${SSH_PORT}    prompt=${ROUTER_PROMPT}    timeout=${TIMEOUT}
    Login    ${USER}    ${PASS}
    Write   ${cmd}
    ${output}    Read Until    ${expected1}
    Write   ${PASS_EN}
    ${output1}    Read Until    ${expected2}
    Write   ${cmd1}
    ${output2}    Read Until    ${expected3}
    Write   ${cmd2}
    ${output3}    Read Until    ${expected3}
    Write   ${cmd3} ${as}
    ${output4}    Read Until    ${expected3}
    : FOR   ${i}   IN   @{commands}
    \  Write   ${i}
    ${output5}    Read Until    ${expected3}
    Write   ${cmd4}
    ${output6}    Read Until    ${expected4}
    ${output7}    Read Until    ${expected3}
    Write   ${cmd5}
    ${output8}    Read Until    ${expected3}
    Write   ${cmd5}
    ${output9}    Read Until    ${expected3}
    Write   ${cmd5}
    ${output10}    Read Until    ${ROUTER_PROMPT}
    Write   ${cmd6}
    ${output11}    Read Until    ${ROUTER_PROMPT}


Reset Bgp Config
    [Arguments]   ${host}  ${as}  ${as_n}  @{commands}
    [Documentation]    Will reset the bgp configuration
    Open Connection    ${host}    port=${SSH_PORT}    prompt=${ROUTER_PROMPT}    timeout=${TIMEOUT}
    Login    ${USER}    ${PASS}
    Write   ${cmd}
    ${output}    Read Until    ${expected1}
    Write   ${PASS_EN}
    ${output1}    Read Until    ${expected2}
    Write   ${cmd1}
    ${output2}    Read Until    ${expected3}
    Write   ${cmd2}
    ${output3}    Read Until    ${expected3}
    Write   no ${cmd3} ${as}
    ${output4}    Read Until    ${expected3}
    Write   ${cmd3} ${as_n}
    ${output4}    Read Until    ${expected3}
    : FOR   ${i}   IN   @{commands}
    \  Write   ${i}
    ${output5}    Read Until    ${expected3}
    Write   ${cmd4}
    ${output6}    Read Until    ${expected4}
    ${output7}    Read Until    ${expected3}
    Write   ${cmd5}
    ${output8}    Read Until    ${expected3}
    Write   ${cmd5}
    ${output9}    Read Until    ${expected3}
    Write   ${cmd5}
    ${output10}    Read Until    ${ROUTER_PROMPT}
    Write   ${cmd6}
    ${output11}    Read Until    ${ROUTER_PROMPT}

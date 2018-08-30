*** Settings ***
Documentation     SDN benchmarking robot file
Suite Setup       Cbench Suite Setup
Test Teardown     Log Results As Zero If Cbench Timed Out
Variables         GlobalVariables.py
Variables         ${CURDIR}/TestcaseVariables.py
Variables         ${CURDIR}/common/CommonUtilLibrary.py
Resource          ${CURDIR}/common/CommonUtils.robot
Resource          ${CURDIR}/libodl/OdlKarafKeywords.robot
Resource          ${CURDIR}/libonos/OnosKarafKeywords.robot
Library           SdnBenchmarking.py
Library           Collections
Library           String
Library           Process

*** Variables ***
${GREEN}  "\\033[32m"
${RED}    "\\033[31m"
${duration_in_secs}    10
${cbench_system}    ${TOOLS_SYSTEM_IP}
${cbench_executable}    /usr/local/bin/cbench
${throughput_results_file}    throughput.csv
${latency_results_file}    latency.csv
@{sumThroughput}
${INDEX}    1

*** Testcases ***
#1. SDN Benchmarking TC1
    #-----------------------------------------------------------------
    #"TestCaseID: TC2"
    #"Constant Switch condition"
    #"Time (ms) : 1000"
    #"Loop : 10"
    #"Switches : 10"
    #"Hosts : 10"
    # -----------------------------------------------------------------
#    Generate Testcase Constant Switch Description    1    ${switch_count_tc1}  ${duration_in_ms_tc1}  ${loops_tc1}  ${num_of_unique_macs_tc1}
#    Cbench Throughput Latency Constant Load Test    -m ${duration_in_ms_tc1} -M ${num_of_unique_macs_tc1} -s ${switch_count_tc1} -l ${loops_tc1} -D ${start_delay} -p ${of_port}

2. SDN Benchmarking TC2

    #-----------------------------------------------------------------
    #"TestCaseID: TC2"
    #"Incremental Switch condition"
    #"Time (ms) : 1000"
    #"Loop : 10"
    #"Switches : 1 to 10"
    #"Hosts : 100"
    # -----------------------------------------------------------------
    Generate Testcase Incremental Switch Description    2  ${switch_count_tc2}  ${duration_in_ms_tc2}  ${loops_tc2}  ${num_of_unique_macs_tc2}
    Log to console   "\nConnecting to Device"
#    "Switches : 1 to 10"
    Cbench Throughput Latency Incremental Load    ${switch_count_tc2}    ${ODL_SYSTEM_IP}    -m ${duration_in_ms_tc2} -M ${num_of_unique_macs_tc2} -s ${switch_count_tc2} -l ${loops_tc2} -D ${start_delay} -p ${of_port}



3. SDN Benchmarking TC3
    #-----------------------------------------------------------------
    #"TestCaseID: TC3"
    #"Constant Switch condition"
    #"Time (ms) : 1000"
    #"Loop : 10"
    #"Switches : 10"
    #"Hosts : 100"
    # -----------------------------------------------------------------
    Generate Testcase Constant Switch Description    3    ${switch_count_tc3}  ${duration_in_ms_tc3}  ${loops_tc3}  ${num_of_unique_macs_tc3}
    Cbench Throughput Latency Constant Load Test    -m ${duration_in_ms_tc1} -M ${num_of_unique_macs_tc1} -s ${switch_count_tc1} -l ${loops_tc1} -D ${start_delay} -p ${of_port}


*** Keywords ***
Initialize Colors

  ${red}=  Evaluate  ${RED}
  Set Suite Variable  ${red}

Run Cbench And Log Results
    [Arguments]    ${cbench_testtype}    ${controller_name}    ${controller_ip}    ${cbench_args}    ${output_filename}=results.csv
    Set Suite Variable    ${output_filename}
    log to console    ${\n}Start Cbench ${cbench_testtype} of SDN controller ${controller_name} ${controller_ip}
    ${output}=    Run Keyword If    "${cbench_system}" == "localhost"    Run    ${cbench_executable} -c ${controller_ip} ${cbench_args}
    ...    ELSE    Run Command On Remote System    ${cbench_system}    ${cbench_executable} -c ${controller_ip} ${cbench_args}
    log to console    ${output}
    Log    ${output}
    Should Contain    ${output}    RESULT
    ${result_line}=    Get Lines Containing String    ${output}    RESULT
    @{results_list}=    Split String    ${result_line}
    Log    ${results_list[5]}
    Log    ${results_list[7]}
    @{result_name_list}=    Split String    ${results_list[5]}    /
    @{result_value_list}=    Split String    ${results_list[7]}    /
    ${num_stats}=    Get Length    ${result_name_list}
    : FOR    ${i}    IN RANGE    0    ${num_stats}
    \    Log    ${result_name_list[${i}]} :: ${result_value_list[${i}]}
    ${min}=    Set Variable    ${result_value_list[${0}]}
    ${max}=    Set Variable    ${result_value_list[${1}]}
    ${average}=    Set Variable    ${result_value_list[${2}]}
    ${stdev}=    Set Variable    ${result_value_list[${3}]}
    ${date}=    Get Time    d,m,s
    Log    CBench Result: ${date},${cbench_args},${min},${max},${average},${stdev}
    Log Results And Determine Status    ${cbench_testtype}    ${controller_name}    ${controller_ip}    ${average}    ${output_filename}
    [Return]    ${average}

Cbench Throughput Latency Constant Load Test
    [Arguments]    ${TC_ARGS}
    #${green}=  Evaluate  ${GREEN}
    #Set Suite Variable  ${green}
    #Test on ODL controller and get average value from cbench output

    ##############Throughput#######################
    ${odlThroughput}=    Run Cbench And Log Results    Throughput    ODL    ${ODL_SYSTEM_IP}    ${TC_ARGS} -t    ${throughput_results_file}
    Sleep    ${test_delay}
    ${onosThroughput}=    Run Cbench And Log Results    Throughput    ONOS    ${ONOS_SYSTEM_IP}     ${TC_ARGS} -t    ${throughput_results_file}
    #check which controller has higher throughput
    #${odlThroughput}=    Set Variable    1
    #${onosThroughput}=    Set Variable    10000
    Log    ODL average throughput : ${odlThroughput}
    Log    ONOS average throughput : ${onosThroughput}
    Log    Comparing results...

    Run Keyword If  ${odlThroughput} > ${onosThroughput}  log to console  ${\n}CONCLUSION : ODL performs betters than ONOS    Log  CONCLUSION : ODL performs betters than ONOS
    Run Keyword If  ${onosThroughput} > ${odlThroughput}  log to console  ${\n}CONCLUSION : ONOS performs betters than ODL    Log  CONCLUSION : ONOS performs betters than ODL

    ##############Latency#######################
    ${odlLatency}=    Run Cbench And Log Results    Latency    ODL    ${ODL_SYSTEM_IP}     ${TC_ARGS}    ${throughput_results_file}
    Sleep    ${test_delay}
    ${onosLatency}=    Run Cbench And Log Results    Latency    ONOS    ${ONOS_SYSTEM_IP}     ${TC_ARGS}    ${throughput_results_file}

    Log    ODL average Latency : ${odlLatency}
    Log    ONOS average Latency : ${onosLatency}
    Log    Comparing results...
    #check which controller has higher throughput
    #${odlThroughput}=    Set Variable    1
    #${onosThroughput}=    Set Variable    10000
    Run Keyword If  ${odlLatency} < ${onosLatency}  log to console  ${\n}CONCLUSION : ODL performs betters than ONOS    Log  CONCLUSION : ODL performs betters than ONOS
    Run Keyword If  ${onosLatency} < ${odlLatency}  log to console  ${\n}CONCLUSION : ONOS performs betters than ODL    Log  CONCLUSION : ONOS performs betters than ODL


Cbench Throughput Latency Incremental Load
    [Arguments]    ${load}    ${SDNC_SYSTEM_IP}    ${TC_ARGS}
    @{avgThroughputlist}=  Create List
    ##############Throughput#######################
    : FOR    ${INDEX}    IN RANGE    1    ${load}+1
    \    ${avgThroughput}=    Run Cbench And Log Results    Throughput    ODL    ${SDNC_SYSTEM_IP}    ${TC_ARGS} -t    ${throughput_results_file}
    \    Log to console    ${avgThroughput}
   #  \    Append To List    ${avgThroughputlist}  ${1}    ${2}   ${3}
    \    Append To List    ${avgThroughputlist}  ${${avgThroughput}}
    \    ${avgMean} =    Evaluate    sum(${avgThroughputlist})
    \    Log to console    ${INDEX}
    Log to console    For loop is over
    Log to console    ${avgThroughputlist}
    Log to console    ${avgMean}


Generate Testcase Constant Switch Description
    [Arguments]    ${number}    ${switch_count}    ${duration_in_ms}    ${loops}    ${num_of_unique_macs}
    log to console  ${\n}-----------------------------------------------------------------
    log to console   "TestCaseID: TC${number}"
    log to console   "Constant Switch condition"
    log to console   "Time (ms) : ${duration_in_ms}"
    log to console   "Loop : ${loops}"
    log to console   "Switches : ${switch_count}"
    log to console   "Hosts : ${num_of_unique_macs}"
    log to console  -----------------------------------------------------------------

Generate Testcase Incremental Switch Description
    [Arguments]    ${number}    ${switch_count}    ${duration_in_ms}    ${loops}    ${num_of_unique_macs}
    log to console  ${\n}-----------------------------------------------------------------
    log to console   "TestCaseID: TC${number}"
    log to console   "Incremental Switch condition"
    log to console   "Time (ms) : ${duration_in_ms}"
    log to console   "Loop : ${loops}"
    log to console   "Switches : ${INDEX} to ${switch_count}"
    log to console   "Hosts : ${num_of_unique_macs}"
    log to console  -----------------------------------------------------------------




Cbench Suite Setup
    #ODL
    Wait Until Keyword Succeeds    3x    1s    OdlKarafKeywords.Issue Command On Karaf Console In Odl   log:set ERROR
    #ONOS
    Wait Until Keyword Succeeds    3x    1s    OnosKarafKeywords.Issue Command On Karaf Console In Onos   log:set ERROR
    #Check cbench installed either locally or remotely
    Run Keyword If    "${cbench_system}" == "localhost"    OperatingSystem.File Should Exist    ${cbench_executable}
    ...    ELSE    Verify File Exists On Remote System    ${cbench_system}    ${cbench_executable}
    #odl controller:
    #Install feature
    Install A Feature in Odl   odl-openflowplugin-drop-test
    Install A Feature in Odl   odl-openflowplugin-flow-services

    #Verify Installation
    Verify Feature Is Installed In Odl   odl-openflowplugin-drop-test
    Verify Feature Is Installed In Odl   odl-openflowplugin-flow-services

    Issue Command On Karaf Console In Odl   dropallpacketsrpc on

    #onos controller:
    #Install feature
    Install A Feature in Onos   org.onosproject.fwd
    Install A Feature in Onos   org.onosproject.openflow-base
    #Verify installation
    Verify Feature Is Installed In Onos   org.onosproject.fwd
    Verify Feature Is Installed In Onos   org.onosproject.openflow-base

    Issue Command On Karaf Console In Onos    cfg set org.onosproject.fwd.ReactiveForwarding packetOutOnly true

Log Results And Determine Status
    [Arguments]    ${cbench_testtype}    ${controller_name}    ${controller_ip}    ${average}    ${output_file}
    Append To File    ${output_file}    ${cbench_testtype},${controller_name},${controller_ip},${average}\n


Log Results As Zero If Cbench Timed Out
    Run Keyword If Timeout Occurred    Log Results And Determine Status    0    0    0    0    ${output_filename}
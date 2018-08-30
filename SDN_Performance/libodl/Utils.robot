*** Settings ***
Documentation     General Utils library. This library has broad scope, it can be used by any robot system tests.
Library           SSHLibrary
Library           HttpLibrary.HTTP
Library           String
Library           DateTime
Library           Process
Library           Collections
Library           RequestsLibrary
Library           OperatingSystem
Library           ${CURDIR}/../common/CommonUtilLibrary.py
Resource          ${CURDIR}/SSHKeywords.robot
Resource          ${CURDIR}/../common/CommonTemplatedRequests.robot
Variables         ${CURDIR}/../GlobalVariables.py

*** Variables ***
# TODO: Introduce ${tree_size} and use instead of 1 in the next line.
${start}          sudo mn --controller=remote,ip=${ODL_SYSTEM_IP} --topo tree,1 --switch ovsk,protocols=OpenFlow13
${USER_HOME}        /root

*** Keywords ***

Report_Failure_Due_To_Bug
    [Arguments]    ${number}    ${include_bug_in_tags}=True
    [Documentation]    Report that a test failed due to a known Bugzilla bug whose
    ...    number is provided as an argument.
    ...    Not FAILED (incl. SKIPPED) test are not reported.
    ...    This keyword must be used in the [Teardown] setting of the affected test
    ...    or as the first line of the test if FastFail module is not being
    ...    used. It reports the URL of the bug on console and also puts it
    ...    into the Robot log file.
    ${test_skipped}=    BuiltIn.Evaluate    len(re.findall('SKIPPED', """${TEST_MESSAGE}""")) > 0    modules=re
    BuiltIn.Return From Keyword If    ('${TEST_STATUS}' != 'FAIL') or ${test_skipped}
    ${bug_url}=    BuiltIn.Set_Variable    https://bugs.opendaylight.org/show_bug.cgi?id=${number}
    ${msg}=    BuiltIn.Set_Variable    This test fails due to ${bug_url}
    ${newline}=    BuiltIn.Evaluate    chr(10)
    BuiltIn.Set Test Message    ${msg}${newline}${newline}${TEST_MESSAGE}
    BuiltIn.Log    ${msg}
    BuiltIn.Run_Keyword_If    "${include_bug_in_tags}"=="True"    Set Tags    ${bug_url}

Report_Failure_And_Point_To_Linked_Bugs
    [Documentation]    Report that a test failed and point to linked Bugzilla bug(s).
    ...    Linked bugs must contain the ${reference} inside comments (workaround
    ...    becasue of currently missing suitable field for external references and
    ...    not correctly working the CONTENT MATCHES filter).
    ...    Not FAILED (incl. SKIPPED) test are not reported.
    ...    This keyword must be used in the [Teardown] setting of the affected test
    ...    or as the first line of the test if FastFail module is not being
    ...    used. It reports the URL of the bug on console and also puts it
    ...    into the Robot log file.
    ${test_skipped}=    BuiltIn.Evaluate    len(re.findall('SKIPPED', """${TEST_MESSAGE}""")) > 0    modules=re
    BuiltIn.Return From Keyword If    ('${TEST_STATUS}' != 'FAIL') or ${test_skipped}
    ${newline}=    BuiltIn.Evaluate    chr(10)
    ${reference}=    String.Replace_String_Using_Regexp    ${SUITE_NAME}_${TEST_NAME}    [ /\.-]    _
    ${reference}=    String.Convert_To_Lowercase    ${reference}
    ${msg}=    BuiltIn.Set_Variable    ... click for list of related bugs or create a new one if needed (with the${newline}"${reference}"${newline}reference somewhere inside)
    ${bugs}=    BuiltIn.Set_Variable    "https://bugs.opendaylight.org/buglist.cgi?f1=cf_external_ref&o1=substring&v1=${reference}&order=bug_status"
    BuiltIn.Set Test Message    ${msg}${newline}${bugs}${newline}${newline}${TEST_MESSAGE}
    BuiltIn.Log    ${msg}${newline}${bugs}

Check Nodes Stats
    [Arguments]    ${node}    ${session}=session
    [Documentation]    A GET on the /node/${node} API is made and specific flow stat
    ...    strings are checked for existence.
    ${resp}    RequestsLibrary.Get Request    ${session}    ${OPERATIONAL_NODES_API}/node/${node}
    Should Be Equal As Strings    ${resp.status_code}    200
    Should Contain    ${resp.content}    flow-capable-node-connector-statistics
    Should Contain    ${resp.content}    flow-table-statistics




Check Karaf Log File Does Not Have Messages In Odl
    [Arguments]    ${ip}    ${message}    ${user}=${ODL_SYSTEM_USER}    ${password}=${ODL_SYSTEM_PASSWORD}    ${prompt}=${ODL_SYSTEM_PROMPT}    ${log_file}=${WORKSPACE}/${BUNDLEFOLDER}/data/log/karaf.log
    [Documentation]    Fails if the provided ${message} is found in the karaf.log file. Uses grep to search. The
    ...    karaf.log file can be overridden with ${log_file} to be any file on the given system @ ${ip}
    ${output}=    Run Command On Controller    ${ip}    grep -c '${message}' ${log_file}    user=${user}    password=${password}    prompt=${prompt}
    Should Be Equal As Strings    ${output}    0

Verify Controller Is Not Dead In Odl
    [Arguments]    ${controller_ip}=${ODL_SYSTEM_IP}
    [Documentation]    Will execute any tests to verify the controller is not dead. Some checks are
    ...    Out Of Memory Execptions.
    Check Karaf Log File Does Not Have Messages    ${controller_ip}    java.lang.OutOfMemoryError
    # TODO: Should Verify Controller * keywords also accept user, password, prompt and karaf_log arguments?

Verify Controller Has No Null Pointer Exceptions In Odl
    [Arguments]    ${controller_ip}=${ODL_SYSTEM_IP}
    [Documentation]    Will execute any tests to verify the controller is not having any null pointer eceptions.
    Check Karaf Log File Does Not Have Messages    ${controller_ip}    java.lang.NullPointerException
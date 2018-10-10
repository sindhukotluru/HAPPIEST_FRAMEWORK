*** Settings ***
Documentation     Karaf library. This library is useful to deal with controller Karaf console for ssh sessions in cluster.
...               Running Setup_Karaf_Keywords is necessary. If SetupUtils initialization is called, this gets initialized as well.
...               If this gets initialized, ClusterManagement gets initialized as well.
Library           SSHLibrary
Library           OperatingSystem

Resource          ${CURDIR}/SSHKeywords.robot
Variables         ../../../../TestRepository/Variables/SDN_Performance-GlobalVariables.py

*** Variables ***
${WORKSPACE}      /tmp
${connection_index_dict}    &{EMPTY}

*** Keywords ***

Verify Feature Is Installed In Odl
    [Arguments]    ${feature_name}    ${controller}=${ODL_SYSTEM_IP}    ${karaf_port}=${KARAF_SHELL_PORT}
    [Documentation]    Will Succeed if the given ${feature_name} is found in the output of "feature:list -i"
    ${output} =    Issue Command On Karaf Console In Odl    feature:list -i | grep ${feature_name}    ${controller}    ${karaf_port}
    BuiltIn.Should_Contain    ${output}    ${feature_name}
    [Return]    ${output}

Issue Command On Karaf Console In Odl
    [Arguments]    ${cmd}    ${controller}=${ODL_SYSTEM_IP}    ${karaf_port}=${KARAF_SHELL_PORT}    ${timeout}=10    ${loglevel}=INFO
    [Documentation]    Will execute the given ${cmd} by ssh'ing to the karaf console running on ${controller}
    ...    Note that this keyword will open&close new SSH connection, without switching back to previously current session.
    SSHLibrary.Open_Connection    ${controller}    port=${karaf_port}    prompt=${KARAF_PROMPT}    timeout=${timeout}
    SSHLibrary.Login    ${KARAF_USER}    ${KARAF_PASSWORD}    loglevel=${loglevel}
    SSHLibrary.Write    ${cmd}
    ${output}    SSHLibrary.Read_Until    ${KARAF_PROMPT}
    SSHLibrary.Close_Connection
    BuiltIn.Log    ${output}
    [Return]    ${output}

Safe Issue Command On Karaf Console In Odl
    [Arguments]    ${cmd}    ${controller}=${ODL_SYSTEM_IP}    ${karaf_port}=${KARAF_SHELL_PORT}    ${timeout}=10    ${loglevel}=INFO
    [Documentation]    Run Issue_Command_On_Karaf_Console but restore previous connection afterwards.
    BuiltIn.Run_Keyword_And_Return    SSHKeywords.Run_Keyword_Preserve_Connection    Issue_Command_On_Karaf_Console    ${cmd}    ${controller}    ${karaf_port}    ${timeout}
    ...    ${loglevel}

Check For Elements On Karaf Command Output Message In Odl
    [Arguments]    ${cmd}    ${elements}    ${controller}=${ODL_SYSTEM_IP}    ${karaf_port}=${KARAF_SHELL_PORT}    ${timeout}=5
    [Documentation]    Will execute the command using Issue Command On Karaf Console then check for the given elements
    ...    in the command output message
    ${output}    Issue Command On Karaf Console In Odl    ${cmd}    ${controller}    ${karaf_port}    ${timeout}
    : FOR    ${i}    IN    @{elements}
    \    BuiltIn.Should_Contain    ${output}    ${i}

Verify Bundle Is Installed In Odl
    [Arguments]    ${bundle_name}    ${controller}=${ODL_SYSTEM_IP}    ${karaf_port}=${KARAF_SHELL_PORT}
    [Documentation]    Will succeed if the given ${bundle name} is present in the output of "bundle:list -s "
    ${output} =    Issue Command On Karaf Console In Odl    bundle:list -s | grep ${bundle_name}    ${controller}    ${karaf_port}
    BuiltIn.Should_Contain    ${output}    ${bundle_name}
    [Return]    ${output}

Verify Bundle Is Not Installed In Odl
    [Arguments]    ${bundle_name}    ${controller}=${ODL_SYSTEM_IP}    ${karaf_port}=${KARAF_SHELL_PORT}
    [Documentation]    Will succeed if the given ${bundle_name} is NOT found in the output of "bundle:list -s"
    ${output} =    Issue Command On Karaf Console In Odl   bundle:list -i | grep ${bundle_name}    ${controller}    ${karaf_port}
    BuiltIn.Should_Not_Contain    ${output}    ${bundle_name}
    [Return]    ${output}

Check Karaf Log Has Messages In Odl
    [Arguments]    ${filter_string}    @{message_list}
    [Documentation]    Will succeed if the @{messages} are found in \ the output of "log:display"
    ${output} =    Issue Command On Karaf Console In Odl    log:display | grep ${filter_string}
    : FOR    ${message}    IN    @{message_list}
    \    BuiltIn.Should_Contain    ${output}    ${message}
    [Return]    ${output}

Install A Feature In Odl
    [Arguments]    ${feature_name}    ${controller}=${ODL_SYSTEM_IP}    ${karaf_port}=${KARAF_SHELL_PORT}    ${timeout}=180
    [Documentation]    Will Install the given ${feature_name}
    BuiltIn.Log    ${timeout}
    ${output} =    Issue Command On Karaf Console In Odl    feature:install ${feature_name}    ${controller}    ${karaf_port}    ${timeout}
    BuiltIn.Log    ${output}
    [Return]    ${output}

Install A Feature Using Active Connection In Odl
    [Arguments]    ${feature_name}
    [Documentation]    Will Install the given ${feature_name} using active connection
    ${cmd} =    BuiltIn.Set_Variable    feature:install ${feature_name}
    SSHLibrary.Write    ${cmd}
    ${output}    SSHLibrary.Read_Until    ${KARAF_PROMPT}
    BuiltIn.Log    ${output}
    [Return]    ${output}

Uninstall A Feature In Odl
    [Arguments]    ${feature_name}    ${controller}=${ODL_SYSTEM_IP}    ${karaf_port}=${KARAF_SHELL_PORT}    ${timeout}=180
    [Documentation]    Will UnInstall the given ${feature_name}
    ${output} =    Issue Command On Karaf Console In Odl    feature:uninstall ${feature_name}    ${controller}    ${karaf_port}    ${timeout}
    BuiltIn.Log    ${output}
    [Return]    ${output}

Wait_For_Karaf_Log In Odl
    [Arguments]    ${message}    ${timeout}=60    ${member_index}=${1}
    [Documentation]    Read karaf logs until message appear
    # TODO: refactor this keyword to use the new workflow to account for multiple controllers.    Initial work was done
    # in this patch https://git.opendaylight.org/gerrit/#/c/45596/
    # however, the consumers of this keyword were breaking after that change.    Initial theory is that a previous
    # keyword used before this "Wait For Karaf Log" keyword was closing the karaf console connection, so the
    # "Flexible SSH Login" keyword from the patch above (45596) was failing.
    BuiltIn.Log    Waiting for '${message}' in karaf log
    SSHLibrary.Open_Connection    ${ODL_SYSTEM_IP}    port=${KARAF_SHELL_PORT}    prompt=${KARAF_PROMPT}    timeout=${timeout}
    SSHLibrary.Login    ${KARAF_USER}    ${KARAF_PASSWORD}    loglevel=${loglevel}
    SSHLibrary.Write    log:tail
    SSHLibrary.Read_Until    ${message}
    SSHLibrary.Close_Connection

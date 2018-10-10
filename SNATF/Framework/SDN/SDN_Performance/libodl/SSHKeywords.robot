*** Settings ***
Documentation     Resource enhancing SSHLibrary with Keywords used in multiple suites.
...
...               Copyright (c) 2015 Cisco Systems, Inc. and others. All rights reserved.
...
...               This program and the accompanying materials are made available under the
...               terms of the Eclipse Public License v1.0 which accompanies this distribution,
...               and is available at http://www.eclipse.org/legal/epl-v10.html
...
...
...               Some suites evolved utility Keywords re-usable with other suites.
...               When the Keywords assume a SSH session is active,
...               and if the Keywords do not fit into a more specific Resource,
...               you can place them here.
Library           SSHLibrary
Resource          ${CURDIR}/Utils.robot
Resource          ../../../../TestRepository/Variables/SDN_Performance-GlobalVariables.robot

*** Variables ***
${SSHKeywords__current_remote_working_directory}    .
${SSHKeywords__current_venv_path}    /tmp/defaultvenv

*** Keywords ***
Open_Connection_To_ODL_System
    [Arguments]    ${ip_address}=${ODL_SYSTEM_IP}    ${timeout}=10s
    [Documentation]    Open a connection to the ODL system at ${ip_address} and return its identifier.
    ${odl_connection} =    SSHLibrary.Open_Connection    ${ip_address}    prompt=${ODL_SYSTEM_PROMPT}    timeout=${timeout}
    Flexible_Controller_Login
    [Return]    ${odl_connection}

Run_Unsafely_Keyword_Over_Temporary_Odl_Session
    [Arguments]    ${ip_address}    ${keyword_name}    @{args}    &{kwargs}
    [Documentation]    Open connection to given IP address, run keyword, close connection, return result.
    ...    This is unsafe in the sense that previously active session will be switched out off, but safe in the sense only the temporary connection is closed.
    Open_Connection_To_ODL_System    ${ip_address}
    # Not using Teardown, to avoid a call to close if the previous line fails.
    ${status}    ${result} =    BuiltIn.Run_Keyword_And_Ignore_Error    ${keyword_name}    @{args}    &{kwargs}
    SSHLibrary.Close_Connection
    BuiltIn.Return_From_Keyword_If    "${status}" == "PASS"    ${result}
    BuiltIn.Fail    ${result}

Copy_File_To_Remote_System
    [Arguments]    ${system}    ${source}    ${destination}=./    ${user}=${DEFAULT_USER}    ${password}=${DEFAULT_PASSWORD}    ${prompt}=${DEFAULT_LINUX_PROMPT}
    ...    ${prompt_timeout}=5s
    [Documentation]    Copy the ${source} file to the ${destination} file on the remote ${system}. Any pre-existing active
    ...    ssh connection will be retained.
    SSHKeywords.Run_Keyword_Preserve_Connection    SSHKeywords.Unsafe_Copy_File_To_Remote_System    ${system}    ${source}    ${destination}    ${user}    ${password}
    ...    ${prompt}    ${prompt_timeout}

Copy_File_To_Odl_System
    [Arguments]    ${system}    ${source}    ${destination}=./
    [Documentation]    Wrapper keyword to make it easier to copy a file to an ODL specific system
    SSHKeywords.Copy_File_To_Remote_System    ${system}    ${source}    ${destination}    ${ODL_SYSTEM_USER}    ${ODL_SYSTEM_PASSWORD}    ${ODL_SYSTEM_PROMPT}

Copy_File_To_Tools_System
    [Arguments]    ${system}    ${source}    ${destination}=./
    [Documentation]    Wrapper keyword to make it easier to copy a file to an Tools specific system
    SSHKeywords.Copy_File_To_Remote_System    ${system}    ${source}    ${destination}    ${TOOLS_SYSTEM_USER}    ${TOOLS_SYSTEM_PASSWORD}    ${TOOLS_SYSTEM_PROMPT}

Flexible_SSH_Login
    [Arguments]    ${user}    ${password}=${EMPTY}    ${delay}=0.5s
    [Documentation]    On active SSH session: if given non-empty password, do Login, else do Login With Public Key.
    ${pwd_length} =    BuiltIn.Get Length    ${password}
    # ${pwd_length} is guaranteed to be an integer, so we are safe to evaluate it as Python expression.
    BuiltIn.Run Keyword And Return If    ${pwd_length} > 0    SSHLibrary.Login    ${user}    ${password}    delay=${delay}
    BuiltIn.Run Keyword And Return    SSHLibrary.Login With Public Key    ${user}    ${USER_HOME}/.ssh/${SSH_KEY}    ${KEYFILE_PASS}    delay=${delay}

Flexible_Mininet_Login
    [Arguments]    ${user}=${TOOLS_SYSTEM_USER}    ${password}=${TOOLS_SYSTEM_PASSWORD}    ${delay}=0.5s
    [Documentation]    Call Flexible SSH Login, but with default values suitable for Mininet machine.
    BuiltIn.Run Keyword And Return    Flexible SSH Login    user=${user}    password=${password}    delay=${delay}

Flexible_Controller_Login
    [Arguments]    ${user}=${ODL_SYSTEM_USER}    ${password}=${ODL_SYSTEM_PASSWORD}    ${delay}=0.5s
    [Documentation]    Call Flexible SSH Login, but with default values suitable for Controller machine.
    BuiltIn.Run Keyword And Return    Flexible SSH Login    user=${user}    password=${password}    delay=${delay}

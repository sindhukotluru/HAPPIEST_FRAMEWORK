Private Function get_unique_range_values(sheet As String, range As String)
    Dim unique_values As Dictionary
    Set unique_values = New Dictionary
    
    With Worksheets(sheet)
        'last_row = .Cells(.Rows.Count, "C").End(xlUp).Row
        range_values = .range(range).Value
        For Each c In range_values
            If unique_values.Exists(c) = False Then unique_values(c) = 1
        Next c
        get_unique_range_values = Join(unique_values.Keys, ",")
        'MsgBox (get_unique_range_values)
    End With
End Function

Private Function create_data_validation_list(sheet As String, rownum As Integer, colnum As Integer, source_list As String)
    With Worksheets(sheet).range(Cells(rownum, colnum), Cells(rownum, colnum)).Validation
        .Delete
        .Add Type:=xlValidateList, Operator:=xlBetween, Formula1:=source_list
        '.Add Type:=xlValidateList, Operator:=xlBetween, Formula1:="=vpn_instance_request_payload"
        .IgnoreBlank = False
        .InCellDropdown = True
        .InputTitle = ""
        .ErrorTitle = ""
        .InputMessage = ""
        .ErrorMessage = ""
        .ShowInput = True
        .ShowError = True
    End With

End Function


Private Function create_addtest_button(rownum As Integer, colnum As Integer)
    Dim addrow_btn As Button
    Dim cellrange As range
    Set cellrange = ActiveSheet.range(Cells(rownum, colnum), Cells(rownum, colnum))
    Set addrow_btn = ActiveSheet.Buttons.Add(cellrange.Left, cellrange.Top, cellrange.Width, cellrange.Height)
    With addrow_btn
        .Caption = "Add Test"
        .Name = "Add Test" & rownum
    End With
    addrow_btn.OnAction = "APITEST.AddARow"
    ActiveWorkbook.Save
    
End Function

Private Function get_header_start_rownumber(sheet_name As String)
    get_header_start_rownumber = Worksheets(sheet_name).range("B1")
End Function


Private Function get_header_colum_index(sheet_name As String, header_name As String)
    Dim header_field As String
    
    If sheet_name = "APITEST" Then get_header_colum_index = get_apitest_header_column_index(header_name)
    If sheet_name = "model schema" Then get_header_column_index = get_model_schema_header_column_index(header_name)
 
End Function

Private Function get_model_schema_header_column_index(header_name As String)
    
    Dim header_index As Dictionary
    Set header_index = New Dictionary
    
    header_index.Add "resource", 3
    header_index.Add "schema file path", 4
    
End Function

Private Function get_apitest_header_column_index(header_name As String)
    
    Dim header_index As Dictionary
    Set header_index = New Dictionary
    
    header_index.Add "test id", 3
    header_index.Add "resource", 4
    header_index.Add "url", 5
    header_index.Add "method", 6
    header_index.Add "request parameters", 7
    header_index.Add "expected response", 8
    header_index.Add "expected response code", 9
    header_index.Add "actual response", 10
    header_index.Add "actual response code", 11
    header_index.Add "execute", 12
    header_index.Add "bulk execute", 13
    header_index.Add "status", 14
    
    get_apitest_header_column_index = header_index.Item(header_name)
    
End Function

Private Function generate_test_id(rownum As Integer, colnum As Integer)
    Dim previous_test_id As String
    Dim next_test_id As String
    previous_test_id = Cells(rownum - 1, colnum)
    Dim testid_arr() As String
    testid_arr = Split(previous_test_id, "_")
    next_test_id = testid_arr(0) & "_" & CStr(CInt(testid_arr(1)) + 1)
    Cells(rownum, colnum).Value = next_test_id
    
End Function

Private Function get_resources(rownum As Integer, colnum As Integer)

    Dim source_sheet_name As String
    Dim header_index As Integer
    Dim header_start_row As Integer
    Dim resource_list As String
    
    source_sheet_name = "model schemas"
    header_index = get_header_colum_index(source_sheet_name, "resource")
    header_start_row = get_header_start_rownumber(source_sheet_name)
    
    Dim range As String
    range = "C5:C16"
    resource_list = get_unique_range_values(source_sheet_name, range)
    
    Call create_data_validation_list("APITEST", rownum, colnum, resource_list)
    
End Function

Private Function get_url(rownum As Integer, colnum As Integer)

    Dim source_sheet_name As String
    Dim header_index As Integer
    Dim header_start_row As Integer
    Dim url_list As String
    
    source_sheet_name = "endpoint urls"
    header_index = get_header_colum_index(source_sheet_name, "url")
    header_start_row = get_header_start_rownumber(source_sheet_name)
    
    Dim range As String
    range = "D4:D15"
    url_list = get_unique_range_values(source_sheet_name, range)
    
    Call create_data_validation_list("APITEST", rownum, colnum, url_list)
    
End Function

Private Function get_http_method(rownum As Integer, colnum As Integer)
    
    Call create_data_validation_list("APITEST", rownum, colnum, "=HTTP_METHOD")

End Function

Private Function get_request_prameter_references(rownum As Integer, colnum As Integer)
    Dim request_params_sheets As Collection
    Set request_params_sheets = New Collection
    Dim header_row As Integer
    Dim request_params_references As Collection
    Set request_params_references = New Collection
    
    ' Get all sheet names with .request in their name
    For Each wks In Worksheets
        If InStrRev(wks.Name, ".request") <> 0 Then request_params_sheets.Add wks.Name
    Next
    Dim i As Long
    Dim sheet As String
    
    For i = 1 To request_params_sheets.Count
        sheet = request_params_sheets(i)
        'MsgBox (sheet)
        With Worksheets(sheet)
            For Each col In .range("C4:Z4")
                If InStrRev(col.Value, "payload") <> 0 Then request_params_references.Add (sheet & "." & col.Value)
            Next
        End With
    Next i
    'Convert request parameter payload reference to string
    Dim request_params_validation_string As String
    For i = 1 To request_params_references.Count
        request_params_validation_string = request_params_validation_string & request_params_references(i) & ","
    Next i
    request_params_validation_string = Left(request_params_validation_string, Len(request_params_validation_string) - 1)
    'MsgBox (request_params_validation_string)
    Call create_data_validation_list("APITEST", rownum, colnum, request_params_validation_string)
    
End Function

Private Function get_http_response_codes(rownum As Integer, colnum As Integer)
    
    Call create_data_validation_list("APITEST", rownum, colnum, "=RESPONSE_CODES")

End Function

Private Function create_execute_button(rownum As Integer, colnum As Integer)
    Dim exec_test_btn As Button
    Dim cellrange As range
    Set cellrange = ActiveSheet.range(Cells(rownum, colnum), Cells(rownum, colnum))
    Set exec_test_btn = ActiveSheet.Buttons.Add(cellrange.Left, cellrange.Top, cellrange.Width, cellrange.Height)
    With exec_test_btn
        .Caption = "Execute"
        .Name = "Execute" & rownum
    End With
    exec_test_btn.OnAction = "APITEST.ExecuteTest"
End Function

Private Function set_actual_response_parameter_references(rownum As Integer, colnum As Integer)
    
    Dim resource_header_index As Integer
    Dim test_id_header_index As Integer
    Dim resource_name, test_id, actual_response_reference As String
    
    resource_header_index = get_header_colum_index("APITEST", "resource")
    test_id_header_index = get_header_colum_index("APITEST", "test id")
    
    resource_name = Cells(rownum, resource_header_index).Value
    test_id = Cells(rownum, test_id_header_index).Value
    
    actual_response_reference = LCase(resource_name) & ".response." & LCase(test_id)
    Cells(rownum, colnum).Value = actual_response_reference
    
End Function

Private Function set_actual_response_code(rownum As Integer, colnum As Integer, response_code As Variant)
     
     Cells(rownum, colnum).Value = response_code
    
End Function

Private Function update_execution_status(rownum As Integer, colnum As Integer)

    'Compare the Actual vs Expected Response Codes
    Dim actual_response_code, expected_response_code As Integer
    Dim actual_response_code_header_index  As Integer
    Dim expected_response_code_header_index As Integer
    
    actual_response_code_header_index = get_header_colum_index("APITEST", "actual response code")
    expected_response_code_header_index = get_header_colum_index("APITEST", "expected response code")
    
    actual_response_code = Int(Cells(rownum, actual_response_code_header_index).Value)
    expected_response_code = Int(Cells(rownum, expected_response_code_header_index).Value)
    
    If actual_response_code = expected_response_code Then
        Cells(rownum, colnum).Value = "PASSED"
        Cells(rownum, colnum).Interior.ColorIndex = 10
        
    Else
        Cells(rownum, colnum).Value = "FAILED"
        Cells(rownum, colnum).Interior.ColorIndex = 3
    End If
    
    
End Function
Sub AddARow()
    Dim addbtn As Object
    Dim rownum As Integer
    Dim colnum As Integer
    Set addbtn = ActiveSheet.Buttons(Application.Caller)
    With addbtn.TopLeftCell
        rownum = .Row
        colnum = .column
    End With
    'Create Add test Button
    Dim newrownum As Integer
    newrownum = rownum + 1
    
    Call create_addtest_button(newrownum, colnum)
    Dim header_index As Integer
    
    'Auto generate Test Case ID on the basis of previous id in the sheet. Default to "APITEST_1"
    header_index = get_header_colum_index("APITEST", "test id")
    Call generate_test_id(newrownum, header_index)
    
    'Populate the resource column with unique values
    header_index = get_header_colum_index("APITEST", "resource")
    Call get_resources(newrownum, header_index)
    
    'TDB: Assign a macro "url" column to fetch all the End point URLS on the basis of the "resource" value selected
    'Currently just get all unique URLS
    header_index = get_header_colum_index("APITEST", "url")
    Call get_url(newrownum, header_index)
    
    'Populate HTTP methods
    header_index = get_header_colum_index("APITEST", "method")
    Call get_http_method(newrownum, header_index)
    
    'Populate the request parameter sheet reference to the "request parameters" column
    'header_index = get_header_colum_index("APITEST", "request parameters")
    'Call get_request_prameter_references(newrownum, header_index)
    
    'Populate the expected response parameters to the " expected response" column
    'header_index = get_header_colum_index("APITEST", "expected response")
    'Call get_request_prameter_references(newrownum, header_index)
    
    'Populate the HTTP response codes
    header_index = get_header_colum_index("APITEST", "expected response code")
    Call get_http_response_codes(newrownum, header_index)
    
    'Create a Execute test button
    header_index = get_header_colum_index("APITEST", "execute")
    Call create_execute_button(newrownum, header_index)
    
End Sub


Sub ExecuteTest()
    
    Dim rownum As Integer
    Dim colnum As Integer
    Dim response_codes_count As String
    Dim lst_status() As String
    
    Set execbtn = ActiveSheet.Buttons(Application.Caller)
    With execbtn.TopLeftCell
        rownum = .Row
        colnum = .column
    End With
    
    'Call the Python function which to execute the API and return response
    Dim test_id As String
    Dim resource_name As String
    Dim url As String
    Dim http_method As String
    Dim request_params_reference As String
    Dim exp_response_reference As String
    Dim exp_response_code As String
    Dim header_index As Integer
    Dim response_code As Variant
    Dim status As String
    Dim data_source_file As String
    
    header_index = get_header_colum_index("APITEST", "test id")
    test_id = Cells(rownum, header_index)
    
    header_index = get_header_colum_index("APITEST", "resource")
    resource_name = Cells(rownum, header_index)
    
    header_index = get_header_colum_index("APITEST", "url")
    url = Cells(rownum, header_index)
    
    header_index = get_header_colum_index("APITEST", "method")
    http_method = Cells(rownum, header_index)
    
    header_index = get_header_colum_index("APITEST", "request parameters")
    request_params_reference = Cells(rownum, header_index)
    
    header_index = get_header_colum_index("APITEST", "expected response")
    exp_response_reference = Cells(rownum, header_index)
    
    header_index = get_header_colum_index("APITEST", "expected response code")
    exp_response_code = Cells(rownum, header_index)
    
    data_source_file = Application.WorksheetFunction.VLookup(resource_name, Worksheets("datasource references").range("$A:$B"), 2, False)
    
    'Populate the Actual Response Parameter reference to the "actual response" column
    response_code = run_api_test(test_id, resource_name, url, http_method, request_params_reference, exp_response_reference, exp_response_code, data_source_file)
    
    header_index = get_header_colum_index("APITEST", "actual response")
    Call set_actual_response_parameter_references(rownum, header_index)
    
    'Populate the Actual Response Code
    header_index = get_header_colum_index("APITEST", "actual response code")
    Call set_actual_response_code(rownum, header_index, response_code)
    'Call set_actual_response_code(rownum, header_index, lst_status(0))
    
    'Populate the Test Execution status
    header_index = get_header_colum_index("APITEST", "status")
    Call update_execution_status(rownum, header_index)
    'Call update_execution_status(rownum, header_index, lst_status(1))
    
End Sub




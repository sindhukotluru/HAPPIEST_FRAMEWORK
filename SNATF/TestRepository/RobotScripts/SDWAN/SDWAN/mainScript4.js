function handleKeyPress(e) {
	if (e.keyCode == 13) {
		document.getElementById("login").click();
	}
}
var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function validate() {
	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;
	if (username == "admin" && password == "admin") {
		window.location = "mainPage4.html";
		return false;
	} else {
		attempt--;
		// Disabling fields after 3 attempts.
		if (attempt == 0) {
			document.getElementById("username").disabled = true;
			document.getElementById("password").disabled = true;
			document.getElementById("submit").disabled = true;
			return false;
		}
	}
}

var onload_Count = 0;
window.onload = function() {
	default_Flows();
	var linkoption_arr = [];
	var service_arr = [ "ssh", "ftp", "pop3/imap", "icmp", "arp", "youtube",
			"netflix", "skype" ];
	var button_arr = [ "ssh_button", "ftp_button", "pop3/imap_button",
			"icmp_button", "arp_button", "youtube_button", "netflix_button",
			"skype_button" ];
	for (var i = 0; i <= 7; i++) {
		linkoption_arr.push(sessionStorage.getItem("SelItem" + i));
		if (linkoption_arr[i] != null) {
			document.getElementById(service_arr[i]).value = linkoption_arr[i];
			switch (linkoption_arr[i]) {
			case "MPLS":
				document.getElementById(button_arr[i]).style.background = '#E2DFA2';
				break;
			case "DIA":
				document.getElementById(button_arr[i]).style.background = '#C1E1DC';
				break;
			case "DROP":
				document.getElementById(button_arr[i]).style.background = '#CDCDC0';
				break;
			}
		}
	}

	// Retain Bandwidth and Cost calculation
	var mpls_bwd_retain = sessionStorage.getItem("SelItem8");
	var dia_bwd_retain = sessionStorage.getItem("SelItem9");

	if (mpls_bwd_retain != null) {
		document.getElementById("mpls").value = mpls_bwd_retain + "%";
		document.getElementById("cost").value = (mpls_bwd_retain / 100 * 100)
				+ "$";
	}

	if (mpls_bwd_retain != null) {
		document.getElementById("dia").value = dia_bwd_retain + "%";
		document.getElementById("savings").value = (dia_bwd_retain / 100 * 100)
				+ "$";
	}

	setInterval(function() {
		default_Flows();
		document.getElementById("reload_Button").click();
	}, 15000);
};

var mpls_bw = [ 0, 0, 0, 0, 0, 0, 0, 0 ], dia_bw = [ 0, 0, 0, 0, 0, 0, 0, 0 ];
function bw(linkOption, position, bw_value) {
	if (linkOption.includes("MPLS")) {
		mpls_bw.splice(position, 1, bw_value);
	} else {
		mpls_bw.splice(position, 1, 0);
	}
	if (linkOption.includes("DIA")) {
		dia_bw.splice(position, 1, bw_value);
	} else {
		dia_bw.splice(position, 1, 0);
	}
}

function generate(min, max) {
	var minNumber = min;
	var maxNumber = max;
	var randomnumber = Math.floor(Math.random() * (maxNumber + 1) + minNumber);
	return randomnumber;
}

function fetch_output_Port(linkOption) {
	var output_Port;
	switch (linkOption) {
	case "MPLS":
		output_Port = 2;
		break;
	case "DIA":
		output_Port = 3;
		break;
	case "DROP":
		output_Port = 0;
		break;
	}
	return output_Port;
}

function default_Flows() {
	install_Default_Flows(0, null, "2048", null, "ipv4-source",
			"10.22.12.100/24", null, null, "NORMAL", "flow_0", generate(500, 600),
			generate(200, 500), generate(0, 65535));
	install_Default_Flows(1, null, "2048", null, "ipv4-destination",
			"10.22.12.100/24", null, null, "NORMAL", "flow_1", generate(500, 600),
			generate(200, 500), generate(0, 65535));
	install_Default_Flows(2, null, "2054", null, null, null, null, null,
			"NORMAL", "flow_2", generate(500, 600), generate(200, 500), generate(0, 65535));
	install_Default_Flows(3, 1, "0x0800", 6, "ipv4-destination",
			"192.168.122.153/24", "tcp-destination-port", 22, 2, "flow_3", generate(500, 600),
			generate(200, 500), generate(0, 65535));
	install_Default_Flows(4, 2, "0x0800", 6, "ipv4-source", 
	        "192.168.122.153/24",
			"tcp-source-port", 22, 1, "flow_4", generate(500, 600), generate(200, 500), generate(0,
					65535));
	install_Default_Flows(5, 1, "0x0800", 6, "ipv4-destination",
			"192.168.122.107/24", "tcp-destination-port", 22, 3, "flow_5", generate(500, 600),
			generate(200, 500), generate(0, 65535));
	install_Default_Flows(6, 3, "0x0800", 6, "ipv4-source", 
	        "192.168.122.107/24",
			"tcp-source-port", 22, 1, "flow_6", generate(500, 600), generate(200, 500), generate(0,
					65535));
}

function delete_Flow(flowId) {
	var xhr = new XMLHttpRequest();
	xhr
			.open(
					"DELETE",
					"http://192.168.203.44:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:125441924469315/flow-node-inventory:table/0/flow/"
							+ flowId, true);
	xhr.setRequestHeader("Authorization", "Basic " + btoa("admin:admin"));
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send();
}

var count1 = 0, count2 = 0, count3 = 0, count4 = 0, count5 = 0, count6 = 0, count7 = 0, count8 = 0;
function install_Flow(type_Of_Service) {
	var output_Port, linkOption;

	switch (type_Of_Service) {
	case 'SSH':
		linkOption = document.getElementById("ssh").value;
		sessionStorage.setItem("SelItem0", linkOption);
		bw(linkOption, 0, 25);
		if (count1 != 0) {
			if (linkOption.includes("DROP")) {
				delete_Flow(11);
				delete_Flow(12);
			} else {
				delete_Flow(13);
			}
		}
		output_Port = fetch_output_Port(linkOption);
		if (output_Port != 0) {
			send_Request("ssh_button", 'SSH', 11, 1, "0x0800", 6,
					"tcp-destination-port", 22, output_Port, "flow_11",
					generate(1, 100), generate(200, 500), generate(0, 65535));
			send_Request("ssh_button", 'SSH', 12, output_Port, "0x0800", 6,
					"tcp-source-port", 22, 1, "flow_12", generate(1, 100),
					generate(200, 500), generate(0, 65535));
		} else {
			send_Request("ssh_button", 'SSH', 13, 1, "0x0800", 6,
					"tcp-destination-port", 22, output_Port, "flow_13",
					generate(1, 100), generate(200, 500), generate(0, 65535));
		}
		count1++;
		break;
	case 'FTP':
		linkOption = document.getElementById("ftp").value;
		sessionStorage.setItem("SelItem1", linkOption);
		bw(linkOption, 1, 5);
		if (count2 != 0) {
			if (linkOption.includes("DROP")) {
				delete_Flow(14);
				delete_Flow(15);
			} else {
				delete_Flow(16);
			}
		}
		output_Port = fetch_output_Port(linkOption);
		if (output_Port != 0) {
			send_Request("ftp_button", 'FTP', 14, 1, "0x0800", 6,
					"tcp-destination-port", 21, output_Port, "flow_14",
					generate(1, 100), generate(200, 500), generate(0, 65535));
			send_Request("ftp_button", 'FTP', 15, output_Port, "0x0800", 6,
					"tcp-source-port", 21, 1, "flow_15", generate(1, 100),
					generate(200, 500), generate(0, 65535));
		} else {
			send_Request("ftp_button", 'FTP', 16, 1, "0x0800", 6,
					"tcp-destination-port", 21, output_Port, "flow_16",
					generate(1, 100), generate(200, 500), generate(0, 65535));
		}
		count2++;
		break;
	case 'POP3/IMAP':
		linkOption = document.getElementById("pop3/imap").value;
		sessionStorage.setItem("SelItem2", linkOption);
		bw(linkOption, 2, 35);
		if (count3 != 0) {
			if (linkOption.includes("DROP")) {
				delete_Flow(17);
				delete_Flow(18);
			} else {
				delete_Flow(19);
			}
		}
		output_Port = fetch_output_Port(linkOption);
		if (output_Port != 0) {
			send_Request("pop3/imap_button", 'POP3/IMAP', 17, 1, "0x0800", 6,
					"tcp-destination-port", 110, output_Port, "flow_17",
					generate(1, 100), generate(200, 500), generate(0, 65535));
			send_Request("pop3/imap_button", 'POP3/IMAP', 18, output_Port,
					"0x0800", 6, "tcp-source-port", 110, 1, "flow_18",
					generate(1, 100), generate(200, 500), generate(0, 65535));
		} else {
			send_Request("pop3/imap_button", 'POP3/IMAP', 19, 1, "0x0800", 6,
					"tcp-destination-port", 110, output_Port, "flow_19",
					generate(1, 100), generate(200, 500), generate(0, 65535));
		}
		count3++;
		break;
	case 'ICMP':
		linkOption = document.getElementById("icmp").value;
		sessionStorage.setItem("SelItem3", linkOption);
		bw(linkOption, 3, 5);
		if (count4 != 0) {
			if (linkOption.includes("DROP")) {
				delete_Flow(20);
				delete_Flow(21);
			} else {
				delete_Flow(22);
			}
		}
		output_Port = fetch_output_Port(linkOption);
		if (output_Port != 0) {
			send_Request("icmp_button", 'ICMP', 20, 1, "0x0800", 1, null, null,
					output_Port, "flow_20", generate(1, 100),
					generate(200, 500), generate(0, 65535));
			send_Request("icmp_button", 'ICMP', 21, output_Port, "0x0800", 1,
					null, null, 1, "flow_21", generate(1, 100), generate(200,
							500), generate(0, 65535));
		} else {
			send_Request("icmp_button", 'ICMP', 22, 1, "0x0800", 1, null, null,
					output_Port, "flow_22", generate(1, 100),
					generate(200, 500), generate(0, 65535));
		}
		count4++;
		break;
	case 'ARP':
		linkOption = document.getElementById("arp").value;
		sessionStorage.setItem("SelItem4", linkOption);
		bw(linkOption, 4, 5);
		if (count5 != 0) {
			if (linkOption.includes("DROP")) {
				delete_Flow(23);
				delete_Flow(24);
			} else {
				delete_Flow(25);
			}
		}
		output_Port = fetch_output_Port(linkOption);
		if (output_Port != 0) {
			send_Request("arp_button", 'ARP', 23, 1, "0x0806", null, null,
					null, output_Port, "flow_23", generate(1, 100), generate(
							200, 500), generate(0, 65535));
			send_Request("arp_button", 'ARP', 24, output_Port, "0x0806", null,
					null, null, 1, "flow_24", generate(1, 1000), generate(200,
							500), generate(0, 65535));
		} else {
			send_Request("arp_button", 'ARP', 25, 1, "0x0806", null, null,
					null, output_Port, "flow_25", generate(1, 100), generate(
							200, 500), generate(0, 65535));
		}
		count5++;
		break;
	case 'Youtube':
		linkOption = document.getElementById("youtube").value;
		sessionStorage.setItem("SelItem5", linkOption);
		bw(linkOption, 5, 10);
		if (count6 != 0) {
			if (linkOption.includes("DROP")) {
				delete_Flow(26);
				delete_Flow(27);
			} else {
				delete_Flow(28);
			}
		}
		output_Port = fetch_output_Port(linkOption);
		if (output_Port != 0) {
			send_Request("youtube_button", 'Youtube', 26, 1, "0x0800", 6,
					"tcp-destination-port", 35, output_Port, "flow_26",
					generate(1, 100), generate(200, 500), generate(0, 65535));
			send_Request("youtube_button", 'Youtube', 27, output_Port,
					"0x0800", 6, "tcp-source-port", 35, 1, "flow_27", generate(
							1, 100), generate(200, 500), generate(0, 65535));
		} else {
			send_Request("youtube_button", 'Youtube', 28, 1, "0x0800", 6,
					"tcp-destination-port", 35, output_Port, "flow_28",
					generate(1, 100), generate(200, 500), generate(0, 65535));
		}
		count6++;
		break;
	case 'Netflix':
		linkOption = document.getElementById("netflix").value;
		sessionStorage.setItem("SelItem6", linkOption);
		bw(linkOption, 6, 5);
		if (count7 != 0) {
			if (linkOption.includes("DROP")) {
				delete_Flow(29);
				delete_Flow(30);
			} else {
				delete_Flow(31);
			}
		}
		output_Port = fetch_output_Port(linkOption);
		if (output_Port != 0) {
			send_Request("netflix_button", 'Netflix', 29, 1, "0x0800", 6,
					"tcp-destination-port", 67, output_Port, "flow_29",
					generate(1, 100), generate(200, 500), generate(0, 65535));
			send_Request("netflix_button", 'Netflix', 30, output_Port,
					"0x0800", 6, "tcp-source-port", 67, 1, "flow_30", generate(
							1, 100), generate(200, 500), generate(0, 65535));
		} else {
			send_Request("netflix_button", 'Netflix', 31, 1, "0x0800", 6,
					"tcp-destination-port", 67, output_Port, "flow_31",
					generate(1, 100), generate(200, 500), generate(0, 65535));
		}
		count7++;
		break;
	case 'Skype':
		linkOption = document.getElementById("skype").value;
		sessionStorage.setItem("SelItem7", linkOption);
		bw(linkOption, 7, 10);
		if (count8 != 0) {
			if (linkOption.includes("DROP")) {
				delete_Flow(32);
				delete_Flow(33);
			} else {
				delete_Flow(34);
			}
		}
		output_Port = fetch_output_Port(linkOption);
		if (output_Port != 0) {
			send_Request("skype_button", 'Skype', 32, 1, "0x0800", 6,
					"tcp-destination-port", 98, output_Port, "flow_32",
					generate(1, 100), generate(200, 500), generate(0, 65535));
			send_Request("skype_button", 'Skype', 33, output_Port, "0x0800", 6,
					"tcp-source-port", 98, 1, "flow_33", generate(1, 100),
					generate(200, 500), generate(0, 65535));
		} else {
			send_Request("skype_button", 'Skype', 34, 1, "0x0800", 6,
					"tcp-destination-port", 98, output_Port, "flow_34",
					generate(1, 100), generate(200, 500), generate(0, 65535));
		}
		count8++;
		break;
	}

	// Bandwidth and cost calculation
	var mpls_bwd = 0, dia_bwd = 0;
	for (var i = 0; i < mpls_bw.length; i++) {
		mpls_bwd = mpls_bwd + mpls_bw[i];
	}
	document.getElementById("mpls").value = mpls_bwd + "%";
	sessionStorage.setItem("SelItem8", mpls_bwd);

	for (var i = 0; i < dia_bw.length; i++) {
		dia_bwd = dia_bwd + dia_bw[i];
	}
	document.getElementById("dia").value = dia_bwd + "%";
	sessionStorage.setItem("SelItem9", dia_bwd);

	document.getElementById("cost").value = (mpls_bwd / 100 * 100) + "$";
	document.getElementById("savings").value = (dia_bwd / 100 * 100) + "$";

}

function install_Default_Flows(flowId, input_port, ethernet_typeId,
		protocol_No, ipv4_End, ipv4_Addrs, portName, portNo, output_Port,
		flow_Name, priority, cookie, max_Length) {
	var xhr = new XMLHttpRequest();
	xhr
			.open(
					"PUT",
					"http://192.168.203.44:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:125441924469315/flow-node-inventory:table/0/flow/"
							+ flowId, true);
	xhr.setRequestHeader("Authorization", "Basic " + btoa("admin:admin"));
	xhr.setRequestHeader('Content-Type', 'application/json');
	var json = {
		"flow" : [ {
			"id" : flowId,
			"match" : {
				"in-port" : input_port,
				"ethernet-match" : {
					"ethernet-type" : {
						"type" : ethernet_typeId
					}
				},
				"ip-match" : {
					"ip-protocol" : protocol_No,
					"ip-proto" : "ipv4"
				},
			},
			"instructions" : {
				"instruction" : [ {
					"order" : "0",
					"apply-actions" : {
						"action" : [ {
							"output-action" : {
								"output-node-connector" : output_Port,
								"max-length" : max_Length
							},
							"order" : "0"
						} ]
					}
				} ]
			},
			"cookie_mask" : "255",
			"flow-name" : flow_Name,
			"installHw" : "false",
			"priority" : priority,
			"idle-timeout" : "0",
			"hard-timeout" : "0",
			"cookie" : cookie,
			"table_id" : "0"
		} ]
	};
	if (ethernet_typeId.includes('0x0800')) {
		json["flow"][0]["match"][ipv4_End] = ipv4_Addrs;
		json["flow"][0]["match"][portName] = portNo;
	} else if (ethernet_typeId.includes('2048')) {
		delete json["flow"][0]["match"]["in-port"];
		delete json["flow"][0]["match"]["ip-match"];
		json["flow"][0]["match"][ipv4_End] = ipv4_Addrs;
	} else if (ethernet_typeId.includes('2054')) {
		delete json["flow"][0]["match"]["in-port"];
		delete json["flow"][0]["match"]["ip-match"];
	}

	xhr.send(JSON.stringify(json));
}

function send_Request(button, type_Of_Service, flowId, input_port,
		ethernet_typeId, protocol_No, portName, portNo, output_Port, flow_Name,
		priority, cookie, max_Length) {
	var xhr = new XMLHttpRequest();
	xhr
			.open(
					"PUT",
					"http://192.168.203.44:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:125441924469315/flow-node-inventory:table/0/flow/"
							+ flowId, true);
	xhr.setRequestHeader("Authorization", "Basic " + btoa("admin:admin"));
	xhr.setRequestHeader('Content-Type', 'application/json');
	var json = {
		"flow" : [ {
			"id" : flowId,
			"match" : {
				"in-port" : input_port,
				"ethernet-match" : {
					"ethernet-type" : {
						"type" : ethernet_typeId
					}
				},
				"ip-match" : {
					"ip-protocol" : protocol_No,
					"ip-proto" : "ipv4"
				}
			},
			"instructions" : {
				"instruction" : [ {
					"order" : "0",
					"apply-actions" : {
						"action" : [ {
							"output-action" : {
								"output-node-connector" : output_Port,
								"max-length" : max_Length
							},
							"order" : "0"
						} ]
					}
				} ]
			},
			"cookie_mask" : "255",
			"flow-name" : flow_Name,
			"installHw" : "false",
			"priority" : priority,
			"idle-timeout" : "0",
			"hard-timeout" : "0",
			"cookie" : cookie,
			"table_id" : "0"
		} ]
	};
	if (type_Of_Service.includes('SSH') || type_Of_Service.includes('FTP')
			|| type_Of_Service.includes('POP3/IMAP')
			|| type_Of_Service.includes('Youtube')
			|| type_Of_Service.includes('Netflix')
			|| type_Of_Service.includes('Skype')) {
		json["flow"][0]["match"][portName] = portNo;
	} else if (type_Of_Service.includes('ARP')) {
		delete json["flow"][0]["match"]["ip-match"];
	}
	if (output_Port == 0) {
		delete json["flow"][0]["instructions"]["instruction"][0]["apply-actions"]["action"][0]["output-action"];
		json["flow"][0]["instructions"]["instruction"][0]["apply-actions"]["action"][0]["drop-action"] = {};
	}
	xhr.send(JSON.stringify(json));
	xhr.onreadystatechange = processRequest;
	function processRequest(e) {
		if (xhr.readyState == 4 || xhr.readyState == 0) {
			if (IsRequestSuccessful(xhr)) {
				if ((input_port == 1 || input_port == 2)
						&& (output_Port == 2 || output_Port == 1)) {
					document.getElementById(button).style.background = '#E2DFA2';// orange
				} else if ((input_port == 1 || input_port == 3)
						&& (output_Port == 3 || output_Port == 1)) {
					document.getElementById(button).style.background = '#C1E1DC';// purple
				} else if ((input_port == 1 || input_port == 0)
						&& (output_Port == 0 || output_Port == 1)) {
					document.getElementById(button).style.background = '#CDCDC0';// blue
				}
			}
		}
	}
}

function get_nodes() {
	var xhr = new XMLHttpRequest();
	xhr
			.open(
					"GET",
					"http://10.22.12.100:8181/restconf/operational/opendaylight-inventory:nodes",
					true);
	xhr.setRequestHeader("Authorization", "Basic " + btoa("admin:admin"));
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send();
	xhr.onreadystatechange = processRequest;
	function processRequest(e) {
		if (xhr.readyState == 4 || xhr.readyState == 0) {
			if (IsRequestSuccessful(xhr)) {
				var response = JSON.parse(xhr.responseText);
				load_Nodeconnectorstatistics(response);
				get_Flows(response);
			} else {
				// alert("No nodes found");
			}
		}
	}
}

function clear_Table_Data(tableId) {
	var table = document.getElementById(tableId);
	var rowCount = table.rows.length;
	while (table.rows.length > 0) {
		table.deleteRow(0);
	}
}

var nodeconnectorstat_arr = [];
var no_of_nodeconnectors = null;
function load_Nodeconnectorstatistics(response) {
	document.getElementById("nodeconnectorstatistics_Checkbox").checked = false;
	debug("nodeconnectorstatistics_Checkbox");
	clear_Table_Data("nodeconnectorstatistics_tbody");
	nodeconnectorstat_arr.length = 0;

	var node_Id = response["nodes"]["node"][0]["id"];
	no_of_nodeconnectors = response["nodes"]["node"][0]["node-connector"].length;

	document.getElementById("nodeconnectorstatistics_node_Id").innerHTML = node_Id;

	for (var x = 0; x < no_of_nodeconnectors; x++) {
		nodeconnectorstat_arr
				.push([
						response["nodes"]["node"][0]["node-connector"][x]["id"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["packets"]["received"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["packets"]["transmitted"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["bytes"]["received"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["bytes"]["transmitted"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["receive-drops"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["transmit-drops"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["receive-errors"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["transmit-errors"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["receive-frame-error"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["receive-over-run-error"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["receive-crc-error"],
						response["nodes"]["node"][0]["node-connector"][x]["opendaylight-port-statistics:flow-capable-node-connector-statistics"]["collision-count"] ]);
	}

	for (var i = 0; i < no_of_nodeconnectors; i++) {
		var table = document.getElementById("nodeconnectorstatistics_tbody");
		var rowCount = table.rows.length;
		var row = table.insertRow(rowCount);

		for (var j = 0; j <= 4; j++) {

			var cell = row.insertCell(j);
			cell.innerHTML = "<td>" + nodeconnectorstat_arr[i][j] + "</td>";
		}
	}
}

function get_Flows(response) {
	var node_Id = response["nodes"]["node"][0]["id"];
	document.getElementById("flowtablestatistics_node_Id").innerHTML = node_Id;

	var xhr = new XMLHttpRequest();
	xhr
			.open(
					"GET",
					"http://192.168.203.44:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:125441924469315/flow-node-inventory:table/0",
					true);
	xhr.setRequestHeader("Authorization", "Basic " + btoa("admin:admin"));
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send();
	xhr.onreadystatechange = processRequest;
	function processRequest(e) {
		if (xhr.readyState == 4 || xhr.readyState == 0) {
			if (IsRequestSuccessful(xhr)) {
				var innerResponse = JSON.parse(xhr.responseText);
				load_Flowtable(innerResponse);
			} else {
				document.getElementById("no_of_flows").innerHTML = 0;
			}
		}
	}
}

function fetch_linkoption(port) {
	var linkoption;
	switch (parseInt(port)) {
	case 2:
		linkoption = "MPLS";
		break;
	case 3:
		linkoption = "DIA";
		break;
	case 0:
		linkoption = "DROP";
		break;
	case 1:
		linkoption = "EDGE";
		break;
	}
	return linkoption;
}

function fetch_service(flowId) {
	var service;
	if (flowId == 11 || flowId == 12 || flowId == 13) {
		service = "SSH";
	} else if (flowId == 14 || flowId == 15 || flowId == 16) {
		service = "FTP";
	} else if (flowId == 17 || flowId == 18 || flowId == 19) {
		service = "POP3/IMAP";
	} else if (flowId == 20 || flowId == 21 || flowId == 22) {
		service = "ICMP";
	} else if (flowId == 23 || flowId == 24 || flowId == 25) {
		service = "ARP";
	} else if (flowId == 26 || flowId == 27 || flowId == 28) {
		service = "Youtube";
	} else if (flowId == 29 || flowId == 30 || flowId == 31) {
		service = "Netflix";
	} else if (flowId == 32 || flowId == 33 || flowId == 34) {
		service = "Skype";
	}
	return service;
}

var flowtablestat_arr = [];
var no_of_flows = null;
function load_Flowtable(response) {
	document.getElementById("flowtablestatistics_Checkbox").checked = false;
	debug("flowtablestatistics_Checkbox");
	clear_Table_Data("flows_tbody");
	flowtablestat_arr.length = 0;
	no_of_flows = response["flow-node-inventory:table"][0]["flow"].length;
	document.getElementById("no_of_flows").innerHTML = no_of_flows - 7;

	for (var x = 0; x < no_of_flows; x++) {
		if (/{}/
				.exec(JSON
						.stringify(response["flow-node-inventory:table"][0]["flow"][x]["instructions"]["instruction"][0]["apply-actions"]["action"][0]["drop-action"])) == "{}") {
			flowtablestat_arr
					.push([
							fetch_service(response["flow-node-inventory:table"][0]["flow"][x]["id"]),
							response["flow-node-inventory:table"][0]["flow"][x]["table_id"],
							response["flow-node-inventory:table"][0]["flow"][x]["id"],
							response["flow-node-inventory:table"][0]["flow"][x]["priority"],
							fetch_linkoption(response["flow-node-inventory:table"][0]["flow"][x]["match"]["in-port"]),
							fetch_linkoption("0"),
							response["flow-node-inventory:table"][0]["flow"][x]["cookie_mask"],
							response["flow-node-inventory:table"][0]["flow"][x]["idle-timeout"],
							response["flow-node-inventory:table"][0]["flow"][x]["cookie"],
							response["flow-node-inventory:table"][0]["flow"][x]["hard-timeout"],
							0 ]);
		} else {
			if (response["flow-node-inventory:table"][0]["flow"][x]["id"] > 10) {
				flowtablestat_arr
						.push([
								fetch_service(response["flow-node-inventory:table"][0]["flow"][x]["id"]),
								response["flow-node-inventory:table"][0]["flow"][x]["table_id"],
								response["flow-node-inventory:table"][0]["flow"][x]["id"],
								response["flow-node-inventory:table"][0]["flow"][x]["priority"],
								fetch_linkoption(response["flow-node-inventory:table"][0]["flow"][x]["match"]["in-port"]),
								fetch_linkoption(response["flow-node-inventory:table"][0]["flow"][x]["instructions"]["instruction"][0]["apply-actions"]["action"][0]["output-action"]["output-node-connector"]),
								response["flow-node-inventory:table"][0]["flow"][x]["cookie_mask"],
								response["flow-node-inventory:table"][0]["flow"][x]["idle-timeout"],
								response["flow-node-inventory:table"][0]["flow"][x]["cookie"],
								response["flow-node-inventory:table"][0]["flow"][x]["hard-timeout"],
								response["flow-node-inventory:table"][0]["flow"][x]["instructions"]["instruction"][0]["apply-actions"]["action"][0]["output-action"]["max-length"] ]);
			}
		}
	}

	for (var i = 0; i < flowtablestat_arr.length; i++) {
		var table = document.getElementById("flows_tbody");
		var rowCount = table.rows.length;
		var row = table.insertRow(rowCount);

		for (var j = 0; j <= 5; j++) {

			var cell = row.insertCell(j);
			cell.innerHTML = "<td>" + flowtablestat_arr[i][j] + "</td>";
		}
	}
}

var count = 0;
function debug(checkbox_Id) {
	var nodeconnector_arr = [ "Rx Drops", "Tx Drops", "Rx Errs", "Tx Errs",
			"Rx Frame Errs", "Rx OverRun Errs", "Rx CRC Errs", "Collisions" ];
	var flowtable_arr = [ "Cookie_Mask", "Idle-Timeout", "Cookie",
			"Hard-Timeout", "Max-Length" ];
	if (document.getElementById(checkbox_Id).checked) {
		if (count != 0) {
			var elements = document.getElementsByClassName("show_hide");
			while (elements[0]) {
				elements[0].parentNode.removeChild(elements[0]);
			}
		}

		if (checkbox_Id.includes("nodeconnectorstatistics_Checkbox")) {
			for (var i = 5; i <= 12; i++) {
				var table = document
						.getElementById("nodeconnectortable_header");
				var rowCount = table.rows.length;
				var cell = table.rows[0].insertCell(i);
				cell.className = "show_hide";
				cell.style.fontWeight = "bold";
				cell.innerHTML = "<th>" + nodeconnector_arr[i - 5] + "</th>";

			}

			for (var i = 0; i < no_of_nodeconnectors; i++) {
				var table = document
						.getElementById("nodeconnectorstatistics_tbody");
				var rowCount = table.rows.length;
				for (var j = 5; j <= 12; j++) {

					var cell = table.rows[i].insertCell(j);
					cell.className = "show_hide";
					cell.innerHTML = "<td>" + nodeconnectorstat_arr[i][j]
							+ "</td>";
				}
			}
		} else {
			for (var i = 6; i <= 10; i++) {
				var table = document.getElementById("flowtable_header");
				var rowCount = table.rows.length;
				var cell = table.rows[0].insertCell(i);
				cell.className = "show_hide";
				cell.style.fontWeight = "bold";
				cell.innerHTML = "<th>" + flowtable_arr[i - 6] + "</th>";

			}

			for (var i = 0; i < flowtablestat_arr.length; i++) {
				var table = document.getElementById("flows_tbody");
				var rowCount = table.rows.length;
				for (var j = 6; j <= 10; j++) {

					var cell = table.rows[i].insertCell(j);
					cell.className = "show_hide";

					cell.innerHTML = "<td>" + flowtablestat_arr[i][j] + "</td>";
				}
			}

		}

		var elems = document.getElementsByClassName("show_hide");
		for (var i = 0; i < elems.length; i++) {
			elems[i].style.display = "";
		}
		count++;
	} else {
		var elems = document.getElementsByClassName("show_hide");
		for (var i = 0; i < elems.length; i++) {
			elems[i].style.display = "none";
		}
	}
}

function IsRequestSuccessful(httpRequest) {
	// IE: sometimes 1223 instead of 204
	var success = (httpRequest.status == 0
			|| (httpRequest.status >= 200 && httpRequest.status < 300)
			|| httpRequest.status == 304 || httpRequest.status == 1223);

	return success;
}

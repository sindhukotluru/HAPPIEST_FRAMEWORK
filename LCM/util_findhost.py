import re

debug = True


def dlog(log):
    if debug:
        print log


def search_host(text):
    print "text :: ", text
    pattern = r'(\d+\.\d+\.\d+\.\d+)'
    match = re.search(pattern, text)
    print "MATCH:", match.groups()[0]
    return match.groups()[0]


def __parse_tabular_data(text):
    found_header = False
    header_row = []
    data = text.split("\n")
    data_list = []
    for line in data:
        line = line.strip()
        if line.startswith("|"):
            if not found_header:
                if "ID" in line:
                    found_header = True
                    header_row = [header.strip() for header in line.split("|") if header.strip() != ""]
            else:
                row_values = [value.strip() for value in line.split("|") if value.strip() != ""]
                data_list.append({header: value for header, value in zip(header_row, row_values)})
    print "data_list ::: ", data_list
    return data_list


def get_active_ip(text):
    net_ip = []
    pair_ip = []
    data_list = __parse_tabular_data(text)
    for value_set in data_list:
        if value_set['Status'] == "ACTIVE":
            net_ip.append(value_set['Networks'])
    for set in net_ip:
        set = set[12:].strip().split(", ")
        for i in set:
            if i.startswith("10."):
                pair_ip.append(i)
    return pair_ip


def get_ip_set(text):
    ip_set = []
    d1 = text.split('"addresses":')
    d2 = d1[1].lstrip(' "').rstrip('",')
    d3 = d2.split('; ')
    print "d3 :", d3
    for i in d3:
        if i.startswith("priv-"):
            i1 = i.split('=')
            ip_set.append(i1[1])
        else:
            i1 = i.split(', ')
            ip_set.append(i1[2])
    print "ip_set: ", ip_set
    ip_set.sort()
    return ip_set


def get_intf(text):
    intf_set = []
    t1 = text.strip().split("\n")
    for i in t1:
        v = i.split(" ", 1)
        intf_set.append(v[0])
    return intf_set[1:]

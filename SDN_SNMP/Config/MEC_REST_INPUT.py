import config


MEC_URL = 'http://'+config.SWITCH['IP']+':8081/'

Login_input = {"login":{"username":"abc","password":"xyz"}}
Reset_input = {"reset":{"action":"reset"}}
Service_Selection_input = {"services":{"type1":"firewall","type2":"dns","type3":"telemetry"}}
Service_Config_input = {"config":{"vlan":[{"id":10,"firewall":[{"src_ip": "10.0.0.2","dest_ip":"10.0.0.4","protocol":"tcp"}],"dns":[{"url":"www.trello.com"}],"telemetry":[{"selected":"true"}]}],"action":"add"}}



def make_input(input_data,services):
    default_services = ['firewall','dns','telemetry']
    for service in default_services:
        if service not in services:
            if input_data.has_key('services'):
                for key,value in input_data['services'].items():
                    if value == service: 
                        input_data['services'].pop(key)
            elif input_data.has_key('config'):
                input_data["config"]['vlan'][0].pop(service)    
    return input_data

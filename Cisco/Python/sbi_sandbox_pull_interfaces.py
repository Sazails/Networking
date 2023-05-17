# Visit https://devnetsandbox.cisco.com/RM/Topology and search for Open NX-OS Programmability lab for login details
# sudo apt install python3-pip
# sudo pip3 install -U netmiko


from netmiko import ConnectHandler
import json

nx_os = {
    'device_type' : 'cisco_ios',
    'ip' : 'sbx-nxos-mgmt.cisco.com',
    'username' : 'admin',
    'password' : 'Admin_1234!',
    'port' : '22'
}

net_connect = ConnectHandler(**nx_os)
output = json.loads(net_connect.send_command('show ip interface brief | json-pretty'))

int_length = len(output['TABLE_intf']['ROW_intf'])
array_interfaces = []

for x in range(int_length):
    str_data = (output['TABLE_intf']['ROW_intf'][x]['intf-name'] +
    ' = '
    + output['TABLE_intf']['ROW_intf'][x]['prefix'] +
    ' is '
    + output['TABLE_intf']['ROW_intf'][x]['proto-state'])

    if "up" in str_data:
        array_interfaces.insert(0, str_data)
    else:
        array_interfaces.append(str_data)
        
for word in array_interfaces:
    print(word)

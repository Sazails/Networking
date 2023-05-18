import requests
import time

# Allow for self signed certs
requests.packages.urllib3.disable_warnings()

USER='admin'
PASS='C1sco12345'

# URL for GET request
url='https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces'

# Set the data formats
headers={'Content-Type' : 'application/yang-data+json', 'Accept' : 'application/yang-data+json'}

# Create interfaces with loop
interface_count = 3

for x in range(interface_count):
	ipaddr='7.7.7.' + str(x)
	print('Loopback created = '+ipaddr)

	interface_payload='\
	{\
		"ietf-interfaces:interface": {\
			"name" : "Loopback777' + str(x) + '",\
			"description" : "RESTCONFed BY 007",\
			"type" : "iana-if-type:softwareLoopback",\
			"enabled" : "true",\
			"ietf-ip:ipv4" : {\
				"address" : [\
					{\
						"ip" : "7.7.7.' + str(x) + '",\
						"netmask" : "255.255.255.255"\
					}\
				]\
			}\
		}\
	}'

	response=requests.request('POST',url,auth=(USER,PASS),headers=headers,data=interface_payload,verify=False)
	print('Status Code = ' + str(response.status_code))
	if(response.text!=""):
		print('Response Text = ' + response.text)



# Get created interfaces from config
response=requests.get(url,auth=(USER,PASS),headers=headers,verify=False)
print(response.text)



## Delete interfaces with loop

int_sleep_time_sec = 5
print('All interfaces created. Will sleep for ' + str(int_sleep_time_sec) + ' seconds before deleting the entries.')
time.sleep(int_sleep_time_sec)

null_payload={}

for y in range(interface_count):
	interface_name="Loopback777" + str(y)
	print('Deleting ' + interface_name)
	loopurl='https://sandbox-iosxe-latest-1.cisco.com:443/restconf/data/ietf-interfaces:interfaces/interface=' + interface_name
	response = requests.request('DELETE',loopurl,auth=(USER,PASS),headers=headers,data=null_payload,verify=False)
	print('Status Code = ' + str(response.status_code))
	if(response.text!=""):
		print('Response Text = ' + response.text)


# Get created interfaces from config
response=requests.get(url,auth=(USER,PASS),headers=headers,verify=False)
print(response.text)


print("=== SCRIPT FINISHED ===")

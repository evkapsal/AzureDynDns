
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.dns import DnsManagementClient
from requests import get
import time
import logging

ip = get('https://api.ipify.org').text
#print( 'My public IP address is:', ip)

# Tenant ID for your Azure subscription
TENANT_ID = 'Your Tenant ID'

# Your service principal App ID
CLIENT = 'Your App ID'

# Your service principal password
KEY = 'Your App ID Key'

#Your Subscription ID
subscription_id= 'Your Subscription ID'

credentials = ServicePrincipalCredentials(
    client_id = CLIENT,
    secret = KEY,
    tenant = TENANT_ID
)

dns_client = DnsManagementClient(
	credentials,
	subscription_id
)

while True :
    try:
        record_set = dns_client.record_sets.create_or_update(
	        'Your Resourse Group',
	        'Your DNS Name',
	        'Your Record Name',
	        'A', #Record Type
	        {
			        "ttl": 300,
			        "arecords": [
				        {
				        "ipv4_address": ip
				        }
			        ]
	        }
        )
    except Exception as c:
        logging.error(c)
    
    time.sleep(3600)

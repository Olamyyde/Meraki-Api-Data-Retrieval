import requests
import json

# Setting the API key and organization ID
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id = "566327653141842188"

# Define endpoint URLs
admins_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/admins"
devices_url = f"https://api.meraki.com/api/v1/organizations/{org_id}/inventoryDevices"

# Set up request headers
headers = {
    "Content-Type": "application/json",
    "X-Cisco-Meraki-API-Key": api_key,
}

# Send the requests and get the responses
admins_resp = requests.get(admins_url, headers=headers)
devices_resp = requests.get(devices_url, headers=headers)

# Parse JSON responses into Python dictionaries
admins_data = json.loads(admins_resp.content)
devices_data = json.loads(devices_resp.content)

# Create lists to store admin names and device information
admins = []
devices = []

# Extract admin names
for admin in admins_data:
    admins.append(admin['name'])

# Extract device information
for device in devices_data:
    device_dict = {
        "serial": device['serial'],
        "mac": device['mac'],
        "networkId": device['networkId'],
        "productType": device['productType'],
    }
    devices.append(device_dict)

# Write data to a text file
with open("PythonRequestsModule.txt", "w") as f:
    f.write("Admins:\n")
    f.write(json.dumps(admins, indent=4))
    f.write("\n\nDevices:\n")
    f.write(json.dumps(devices, indent=4))

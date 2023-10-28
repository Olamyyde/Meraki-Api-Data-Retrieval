import meraki
import json

# Set the API key and organization ID
api_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_id = "566327653141842188"

# Create a Meraki dashboard API session
dashboard = meraki.DashboardAPI(api_key)

# Get all admins in the organization
admins_data = dashboard.organizations.getOrganizationAdmins(org_id)

# Get all devices in the organization
devices_data = dashboard.organizations.getOrganizationInventoryDevices(org_id)

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
        "productType": device['productType']
    }
    devices.append(device_dict)

# Write the data to a text file
with open("MerakiModule.txt", "w") as f:
    f.write("Admins:\n")
    f.write(json.dumps(admins, indent=4))
    f.write("\n\nDevices:\n")
    f.write(json.dumps(devices, indent=4))

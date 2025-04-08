# Firewall simulation script
# We are going to implement a whitelist approach to enhance security.
"""
Scenario:
Our internal Payroll server is receiving requests from random IP addresses. 
The firewall checks if the incoming IP is on the whitelist of accepted IP addresses.
It then allows or blocks the IP address based on the whitelist. 
"""

import random # Import the random module to generate port numbers

# create a list of network traffic with IP addresses and their corresponding departments
network_traffic = [
    {"192.168.1.40": "Human Resources"},
    {"192.168.10.5": "IT Department"},
    {"172.16.2.10": "Marketing"},
    {"203.98.123.45": "Remote Vpn"},
    {"172.16.10.20": "Payroll"},
    {"196.25.14.88": "Mexico"},
    {"172.16.10.30": "Payroll"},
    {"172.16.10.15": "Payroll"},
    {"192.168.20.3": "Sales"},
    {"192.168.2.16": "Kitchen"},
]
# The list contains dictionaries with IP addresses as keys and their corresponding departments as values.

# Blacklisted IP addresses
whitelist = ["172.16.10.20", "172.16.10.30", "172.16.10.15"]

# Function to check firewall rules
def firewall_rules(ip_address):
    if ip_address in whitelist: # Check if the IP address is in the whitelist
        return "ALLOWED"
    else:
        return "BLOCKED"


print ("Network Traffic")
print ("-----------------")
# Go through all network traffic
for traffic in network_traffic: # Iterate through the network traffic data
    # Extract IP address and department from the dictionary
    ip_address, department = list(traffic.items())[0] 
    # Generate a random port number
    port = random.randint(1024, 65535)  # Random port number between 1024 and 65535
    # Check the firewall rules for the IP address
    action = firewall_rules(ip_address)

    # Print the result of the firewall check
    print(f"Ip:", ip_address, "Port:", port, "Department:", department, "Action:", action) 
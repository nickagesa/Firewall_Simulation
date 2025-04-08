# Firewall simulation script
# This script simulates a basic firewall that checks incoming network traffic against a blacklist of IP addresses.
"""
Scenario:
Our web server is receiving requests from random external IP addresses. 
The firewall checks if the incoming IP is on the blacklist of known malicious IPs. 
It then blocks the Ip address if necessary.
"""

import random # Import the random module to generate random port numbers

# create a list of network traffic with IP addresses and their corresponding countries
network_traffic = [
    {"102.89.34.12": "South Africa"},
    {"185.23.56.78": "Germany"},
    {"45.67.89.10": "United States"},
    {"203.98.123.45": "Australia"},
    {"150.129.57.89": "India"},
    {"196.25.14.88": "Mexico"},
    {"77.45.23.101": "France"},
    {"190.80.32.77": "Brazil"},
    {"62.210.111.33": "Netherlands"},
    {"14.139.54.201": "United States"},
]
# The list contains dictionaries with IP addresses as keys and their corresponding countries as values.

# Blacklisted IP addresses
blacklist = ["102.89.34.12", "45.67.89.10", "77.45.23.101", "62.210.111.33", "203.98.123.45"]

# Function to check firewall rules
def firewall_rules(ip_address):
    if ip_address in blacklist: # Check if the IP address is in the blacklist
        return "BLOCKED"
    else:
        return "ALLOWED"

# Go through all network traffic
for traffic in network_traffic: # Iterate through the network traffic data
    # Extract IP address and country from the dictionary
    ip_address, country = list(traffic.items())[0] # Extract IP address and country from the dictionary
    # Generate a random port number
    port = random.randint(1024, 65535)  # Random port number between 1024 and 65535
    # Check the firewall rules for the IP address
    action = firewall_rules(ip_address)

    # Print the result of the firewall check
    print(f"Ip:", ip_address, "Port:", port, "Country:", country, "Action:", action) 

# The weakness of using a blacklist is that it can be bypassed by attackers using IP addresses that are not on the list.
# A more robust solution would be to implement a whitelist approach, where only known safe IP addresses are allowed access.
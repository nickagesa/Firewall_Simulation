# Firewall_Simulation
Basic firewall simulation in Python to help beginners understand how firewalls work.
The two python files have two different senarios to demonstrate how a firewall would be configured at a basic level.

### Scenario 1:
Our web server is receiving requests from random external IP addresses. 
The firewall checks if the incoming IP is on the blacklist of known malicious IPs. 
It then blocks the Ip address based on the blacklist.

### Scenario 2:
Our internal Payroll server is receiving requests from random IP addresses. 
The firewall checks if the incoming IP is on the whitelist of accepted IP addresses.
It then allows or blocks the IP address based on the whitelist.

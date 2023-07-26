import ipaddress

# Load subnets from a file
with open('block.txt') as f:
    subnets = [line.strip() for line in f]

# Create a set to store unique IP addresses
unique_ips = set()

for subnet in subnets:
    # Create an IPv4Network object
    net = ipaddress.IPv4Network(subnet)

    # Get a set of all IP addresses in this subnet
    subnet_ips = set(net)

    # Add the IPs from this subnet to the set of unique IPs
    unique_ips = unique_ips.union(subnet_ips)

# Print the total number of unique IPs
print(len(unique_ips))

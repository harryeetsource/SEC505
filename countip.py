import ipaddress
from tqdm import tqdm

# Load subnets from a file
with open('block.txt') as f:
    subnets = [ipaddress.IPv4Network(line.strip()) for line in f]

# Sort the subnets by their network address
subnets.sort(key=lambda net: net.network_address)

i = 0
while i < len(subnets) - 1:
    # If this subnet overlaps with the next one
    if subnets[i].overlaps(subnets[i + 1]):
        # Merge the two subnets
        merged = ipaddress.collapse_addresses([subnets[i], subnets[i + 1]])
        # Replace the two original subnets with their merge
        subnets[i:i+2] = merged
    else:
        # Move on to the next subnet
        i += 1

# Now that all overlapping subnets have been merged, calculate the total number of unique IPs
total_ips = sum(net.num_addresses for net in tqdm(subnets, desc="Calculating total IPs", unit="subnet"))

print(total_ips)

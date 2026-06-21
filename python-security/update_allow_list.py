# Algorithm for File Updates in Python
# Google Cybersecurity Certificate - Automate Cybersecurity Tasks with Python
# Analyst: Mario Galarza

# Open the file that contains the allow list
import_file = "allow_list.txt"

# Read the file contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert the string into a list
ip_addresses = ip_addresses.split()

# Iterate through the remove list
remove_list = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]

for element in remove_list:
    # Remove IP addresses that are on the remove list
    if element in ip_addresses:
        ip_addresses.remove(element)

# Update the file with the revised list of IP addresses
ip_addresses = "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)

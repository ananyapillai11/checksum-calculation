import struct
import socket

def calculate_checksum(data):
    if len(data) % 2 != 0:
        data += b'\x00'  # Pad the data if its length is odd

    checksum = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i+1]
        checksum += word

    while checksum >> 16:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)

    return ~checksum & 0xFFFF

def calculate_udp_checksum(source_ip, dest_ip, protocol, udp_length, source_port, dest_port, udp_data):
    # Pseudo-header
    pseudo_header = struct.pack('!4s4sBBH', socket.inet_aton(source_ip), socket.inet_aton(dest_ip), 0, protocol, udp_length)

    # UDP header
    udp_header = struct.pack('!HHHH', source_port, dest_port, udp_length, 0)

    # Concatenate pseudo-header, UDP header, and data
    checksum_data = pseudo_header + udp_header + udp_data

    # Calculate checksum
    checksum = calculate_checksum(checksum_data)

    return checksum

# Get user input for sender information
source_ip = input("Enter source IP address: ")
dest_ip = input("Enter destination IP address: ")
protocol = 17  # UDP protocol number
udp_length = int(input("Enter UDP length: "))
source_port = int(input("Enter source port number: "))
dest_port = int(input("Enter destination port number: "))
udp_data_hex = input("Enter UDP payload data (hexadecimal): ")

# Convert UDP payload data from hexadecimal to bytes
udp_data = bytes.fromhex(udp_data_hex)

# Calculate sender checksum
sender_checksum = calculate_udp_checksum(source_ip, dest_ip, protocol, udp_length, source_port, dest_port, udp_data)

# Get user input for receiver checksum
#receiver_checksum_hex = input("Enter receiver checksum (hexadecimal): ")
#receiver_checksum = int(receiver_checksum_hex, 16)

# Check if sender checksum matches receiver checksum
#checksum_match = sender_checksum == receiver_checksum

# Print the results
print("Sender Checksum (Hexadecimal):", hex(sender_checksum))
#print("Receiver Checksum (Hexadecimal):", receiver_checksum_hex)
#print("Checksum Match:", checksum_match)

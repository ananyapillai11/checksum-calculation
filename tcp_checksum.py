def convert_decimal_to_binary(decimal, num_bits):
    # Convert decimal to binary
    binary = bin(decimal)[2:].zfill(num_bits)
    return binary

def calculate_checksum(source_ip, dest_ip, reserved1, protocol, tcp_length,source_port, dest_port, sequence, ack, hlen, reserved2,flags, window, checksum_in, urgent_pointer, tcp_data):
    # Convert IP addresses to binary strings
    source_ip_binary = convert_decimal_to_binary(source_ip, 32)
    dest_ip_binary = convert_decimal_to_binary(dest_ip, 32)
    
    # Convert other inputs to binary strings
    protocol = convert_decimal_to_binary(protocol, 8)
    source_port = convert_decimal_to_binary(source_port, 16)
    dest_port = convert_decimal_to_binary(dest_port, 16)
    tcp_length = convert_decimal_to_binary(tcp_length, 16)
    sequence = convert_decimal_to_binary(sequence, 32)
    ack = convert_decimal_to_binary(ack, 32)
    hlen = convert_decimal_to_binary(hlen, 4)
    window = convert_decimal_to_binary(window, 16)
    reserved1 = convert_decimal_to_binary(reserved1, 8)
    reserved2 = convert_decimal_to_binary(reserved2, 6)
    flags = convert_decimal_to_binary(flags, 6)
    checksum_in = convert_decimal_to_binary(checksum_in, 16)
    urgent_pointer = convert_decimal_to_binary(urgent_pointer, 16)
    
    # Convert TCP data from hexadecimal to binary
    tcp_data_binary = bin(int(tcp_data, 16))[2:].zfill(len(tcp_data) * 4)
    
    # Pad TCP data with zeros to make its length a multiple of 16
    if len(tcp_data_binary) % 16 != 0:
        tcp_data_binary += '0' * (16 - len(tcp_data_binary) % 16)
    
    # Concatenate all binary strings
    message = source_ip_binary + dest_ip_binary + reserved1 + protocol + tcp_length + source_port + dest_port + sequence + ack + hlen + reserved2 + flags + window + checksum_in + urgent_pointer + tcp_data_binary
    
    # Perform one's complement addition
    checksum = 0
    while len(message) >= 16:
        value = int(message[:16], 2)
        checksum += value
        message = message[16:]
        if len(message) < 16:
            break
    
    # Add the remaining 16-bit value if present
    if len(message) > 0:
        value = int(message, 2)
        checksum += value
    
    # Fold 1's complement carry
    while checksum >> 16:
        checksum = (checksum & 0xFFFF) + (checksum >> 16)
    
    # Take one's complement
    checksum = checksum ^ 0xFFFF
    return hex(checksum)[2:].zfill(4).upper()

# Example usage
source_ip_input = input("Enter source IP address (decimal dotted format): ")
dest_ip_input = input("Enter destination IP address (decimal dotted format): ")
reserved1_input = int(input("Enter the reserved bits (in decimal): "))
protocol_input = int(input("Enter protocol number (in decimal): "))
tcp_length_input = int(input("Enter TCP segment length (in decimal): "))
source_port_input = int(input("Enter source port number (in decimal): "))
dest_port_input = int(input("Enter destination port number (in decimal): "))
sequence_input = int(input("Enter the sequence number (in decimal): "))
ack_input = int(input("Enter the acknowledgment number (in decimal): "))
hlen_input = int(input("Enter the header length (in decimal): "))
reserved2_input = int(input("Enter the reserved bits (in decimal): "))
flags_input = int(input("Enter the flag bits (in decimal): "))
window_input = int(input("Enter the window size (in decimal): "))
checksum_in_input = int(input("Enter the existing checksum (in decimal): "))
urgent_pointer_input = int(input("Enter the urgent pointer (in decimal): "))
tcp_data_input = input("Enter TCP data (in hexadecimal): ")

# Convert IP addresses from decimal dotted format to decimal
source_ip = int(''.join(format(int(x), '08b') for x in source_ip_input.split('.')), 2)
dest_ip = int(''.join(format(int(x), '08b') for x in dest_ip_input.split('.')), 2)

checksum = calculate_checksum(source_ip, dest_ip, reserved1_input, protocol_input,tcp_length_input, source_port_input, dest_port_input,sequence_input, ack_input, hlen_input, reserved2_input,flags_input, window_input, checksum_in_input,urgent_pointer_input, tcp_data_input)

print("Calculated checksum:", checksum)

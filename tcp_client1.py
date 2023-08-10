import socket
# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Define the host and port
host = 'localhost'
port = 12345
# Connect to the server
client_socket.connect((host, port))
# Get user input
name = input("Enter your name: ")
reg_number = input("Enter your registration number: ")
# Create a string with name and registration number separated by a comma
data = name + reg_number
# Send the data to the server
client_socket.send(data.encode())
# Close the connection with the server
client_socket.close()

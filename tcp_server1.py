import socket
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Define the host and port
host = 'localhost'
port = 12345
# Bind the socket to the host and port
server_socket.bind((host, port))
# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on {}:{}".format(host, port))
while True:
    # Accept a client connection
    client_socket, address = server_socket.accept()
    print("Connection established with {}:{}".format(address[0], address[1]))
 
    # Receive data from the client
    name = client_socket.recv(1024).decode()
    reg_number = client_socket.recv(1024).decode()
    # Print the received data
    print("DATA:", name +reg_number)
    # Close the connection with the client
    client_socket.close()
    print("Connection closed with {}:{}".format(address[0], address[1]))

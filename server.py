import socket

# Create a socket object
# .AF_INET reefers to the address family IPv4
# .SOCK_STREAM reefers to socket type TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Assign IP-address and port for socket instance
# associating sockets with determined network interface and port
server_socket.bind(('127.0.0.1', 2345))

# Passive socket accepting incoming request with a given method
server_socket.listen(1)

# While-loop running until server is stopped
while True:
    print("Waiting...")  # Print message to console

    # Server listening for possible connections
    # .accept used to establish connection creating a new socket object
    client_socket, address = server_socket.accept()

    print(f"Connection established - {address}")  # Print message to console

    # .send() sends response message from server socket to client sockets
    client_socket.send("Connection has been esablished. Hello and goodbye".encode())

    # Receive input from client
    message = client_socket.recv(1024)

    # Convert bytes to string
    response = message.decode()

    print("Input: " + response)

    # .close() ends connection with client socket
    #client_socket.close()

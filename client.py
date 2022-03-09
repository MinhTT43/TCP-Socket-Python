from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)

async def communicate (cli):
        # Text input from user
        command = input("You: ")

        # Convert input from string to bytes
        response = command.encode()

        # Send response to server
        client_socket.sendall(response)

# Client-object
class Client:
    def __init__(self, ip, port, bot):
        self.ip = ip
        self.port = port
        self.bot = bot

    def connect(self):
        # Instantiate client socket
        client_socket = socket(AF_INET, SOCK_STREAM)

        # Connect to server
        client_socket.connect((self.ip, self.port))

        if not self.bot:
            while True:
                message = client_socket.recv(1024)
                print(message.decode())

                # Text input from user
                command = input("You: ")

                # Convert input from string to bytes
                response = command.encode()

                # Send response to server
                client_socket.sendall(response)

        if self.bot == "Minh":
            while True:
                message = client_socket.recv(1024)
                print(message.decode())

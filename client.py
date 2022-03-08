from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)

from bot import Bot


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

        # Message received, reading at most 1024-bytes
        message = client_socket.recv(1024)

        # Decode received message to ASCII from bytes format
        print(message.decode())

        if not self.bot:
            while True:
                # Text input from user
                command = input("You: ")

                # Convert input from string to bytes
                response = command.encode()

                # Send response to server
                client_socket.sendall(response)

        if self.bot == "Minh":
            message = Bot.minh_bot().encode()
            client_socket.sendall(message)
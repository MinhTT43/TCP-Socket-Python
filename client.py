from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)

import sys

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

        message = None
        command = None


        if not self.bot:
            while command != 'quit':
                message = client_socket.recv(1024)
                print(message.decode())

                # Text input from user
                command = input("Me: ")

                # Convert input from string to bytes
                response = command.encode()

                # Send response to server
                client_socket.sendall(response)
            sys.exit("Connection terminated")

        if self.bot == "Charlie":
            while message != 'quit':
                message_coded = client_socket.recv(1024)
                message = message_coded.decode('utf-8')
                print("Input: " + message)
                if message:
                    response = Bot.charlie(message)
                    client_socket.sendall(response.encode())

        if self.bot == "Chong":
            while message != 'quit':
                message_coded = client_socket.recv(1024)
                message = message_coded.decode('utf-8')
                print("Input: " + message)
                if message:
                    response = Bot.chong(message)
                    client_socket.sendall(response.encode())

        sys.exit("User terminated connection, bot disconnecting")

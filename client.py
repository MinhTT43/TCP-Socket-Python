from pickle import FALSE
import socket
import sys
from bot import Bot
import time

# Client-object
class Client:
    def __init__(self, ip, port, bot):
        self.ip = ip
        self.port = port
        self.bot = bot

    def connect(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create client socket
        client_socket.connect((self.ip, self.port))  # connect client socket to server

        message = None  # response variable
        command = None  # user message variable

        # user
        # if bot-parameter == false then it is the user
        if not self.bot: 
            message = client_socket.recv(1024)
            print(message.decode())

            while command != 'quit':
                # Text input from user
                command = input("Me: ")

                # Convert input from string to bytes
                response = ("Me: " + command).encode()
                client_socket.sendall(response)

                for i in range(3):
                    
                    message = client_socket.recv(1024).decode()
                    print(message)
                print("\n")
            sys.exit("Connection terminated")

        # bot
        # if bot-parameter is a string then it is a bot where name is given
        if str(self.bot):
            while True:
                message_coded = client_socket.recv(1024)
                message = message_coded.decode('utf-8')
                print(message)
                if message == 'Me: quit':
                    sys.exit("User terminated session")

                if "Me: " in message: # checks if user has sent message
                    if self.bot == "Charlie":
                        response = Bot.charlie(message)
                    elif self.bot == "Chuck": 
                        response = Bot.chuck(message)
                    elif self.bot == "Chong":
                        response = Bot.chong(message)
                        
                    client_socket.sendall(response.encode())

        sys.exit("User terminated connection, bot disconnecting")

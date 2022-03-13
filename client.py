from pickle import FALSE
import socket
import sys
from bot import Bot
import time

# Client-object

ip = sys.argv[1]
port = int(sys.argv[2])
bot = sys.argv[3]


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create client socket
client_socket.connect((ip, port))  # connect client socket to server

message = None  # response variable
command = None  # user message variable

# user
# if bot-parameter == false then it is the user
if bot == "none": 
    message = client_socket.recv(1024)
    print(message.decode())

    while True:
        # Text input from user
        command = input("Me: ")
        if command != 'quit':
            # Convert input from string to bytes
            response = ("Me: " + command).e
            ncode()
            client_socket.sendall(response)

            for i in range(3):
                
                message = client_socket.recv(1024).decode()
                print(message)
            print("\n")
        else:
            client_socket.sendall("quit".encode())
            sys.exit("Connection terminated")

# bot
# if bot-parameter is a string then it is a bot where name is given
if bot == 'Charlie' or 'Chong' or 'Chuck':
    while True:
        message_coded = client_socket.recv(1024)
        message = message_coded.decode('utf-8')
        print(message)
        if message == 'Me: quit':
            client_socket.sendall((bot + " has disconnected").encode())
            sys.exit("User terminated session")

        if "Me: " in message: # checks if user has sent message
            if bot == "Charlie":
                response = Bot.charlie(message)
            elif bot == "Chuck": 
                response = Bot.chuck(message)
            elif bot == "Chong":
                response = Bot.chong(message)
                
            client_socket.sendall(response.encode())

sys.exit("User terminated connection, bot disconnecting")

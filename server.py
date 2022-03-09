from socket import (
    socket,
    AF_INET,
    SOCK_STREAM
)

import asyncio

async def client_handler(client):
    loop = asyncio.get_event_loop()  # Define
    request = None  # Data from client
    while request != 'quit': # If user write "quit" exit
        request = await loop.sock_recv(client, 255)
        response = request.decode()
        await loop.sock_sendall(client, response.encode())


status = None
server_socket = socket(AF_INET, SOCK_STREAM)  # Socket object for server
server_socket.bind(('127.0.0.1', 2345))  # Assign IP-address and port
server_socket.listen(4)

while status != 'quit':
    print("Waiting...")
    client, address = server_socket.accept()
    print(f"Connection established - {address}")
    client.send("Test".encode())
    message_coded = client.recv(1024)
    status = message_coded.decode()
    print(status)

client.close()
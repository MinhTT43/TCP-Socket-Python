import asyncio
import socket
import time


async def client_handler(client, cli_list):
    loop = asyncio.get_event_loop()
    request = None
    while request != 'quit':
        request = (await loop.sock_recv(client, 1024)).decode()
        print(request)
        for cli in cli_list:
            if cli != client:
                time.sleep(0.5)
                await loop.sock_sendall(cli, request.encode())


async def run_server():
    cli_list = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 2345))
    server.listen(4)
    server.setblocking(False)

    loop = asyncio.get_event_loop()

    while True:
        print("Waiting for new connection...\n")
        client, address = await loop.sock_accept(server)
        cli_list.append(client)
        print(f"Connection established - {address} \n")  # Print message to cons
        client.send("Connection has been established!".encode())
        loop.create_task(client_handler(client, cli_list))


asyncio.run(run_server())

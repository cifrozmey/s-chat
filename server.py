import socket

SERVER_ADDRESS = ('тут ip локального сервера', 8125)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)
clients = []
members = {}
print("Start")

while True:
    data, address = server_socket.recvfrom(1024)
    print(address[0], address[1])
    if address not in clients:
        clients.append(address)
        text = "Добро пожаловать в чат!"
        server_socket.sendto(text.encode('utf-8'), address)

    for client in clients:

        if client == address:
            text_from_client = data.decode('utf-8')
            print(text_from_client)

            continue

        server_socket.sendto(data, client)
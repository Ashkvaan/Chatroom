import socket , threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',1212))
server.listen()

# Recive message
def ReMe(client:socket.socket):
    while True:
        data = client.recv(2048)
        if data.decode().strip() != '':
            with open("./log.text",'a+') as f:
                f.write(data.decode())

# Accept Clients
while True:
    client,address = server.accept()
    thread = threading.Thread(target=ReMe, args=(client,))
    thread.start()

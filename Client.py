import socket
import time
Client = socket.socket()
Client.connect(('127.0.0.1',1212))

time.sleep(1)
Client.send("Hi".encode())
import socket
import os
from _thread import *

Ss = socket.socket()
LOCALHOST = "192.168.1.17"
PORT = 8080
ThreadCount = 0

try:
    Ss.bind((LOCALHOST, PORT))
except socket.error as e:
    print(str(e))

print('Socket is listening..')
Ss.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)

        response = input("Response: ")
        
        if not data:
            break
        connection.sendall(str.encode("server message: " + response))
    connection.close()

while True:
    Client, address = Ss.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
Ss.close()
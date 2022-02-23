import socket
import os
from _thread import *
import main

Ss = socket.socket()
LOCALHOST = "192.168.83.72"
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
        response = 'Server message: ' + data.decode('utf-8')
        
        if not data:
            break
        connection.sendall(str.encode(response))
    connection.close()

while True:
    Client, address = Ss.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(multi_threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    print(main.shuffle_deck())
Ss.close()
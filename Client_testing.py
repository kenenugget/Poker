import socket

ClientMultiSocket = socket.socket()
SERVER = "192.168.1.17"
PORT = 8080

print('Waiting for connection response')

try:
    ClientMultiSocket.connect((SERVER, PORT))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)

while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(1024)
    print(res.decode('utf-8'))
ClientMultiSocket.close()
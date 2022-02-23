import socket

ClientMultiSocket = socket.socket()
SERVER = "192.168.83.72"
PORT = 8080

print('Waiting for connection response')

try:
    ClientMultiSocket.connect((SERVER, PORT))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(2048)

while True:
    Input = input('Hey there: ')
    ClientMultiSocket.send(str.encode(Input))
    res = ClientMultiSocket.recv(2048)
    print(res.decode('utf-8'))
ClientMultiSocket.close()
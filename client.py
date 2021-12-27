import socket

SERVER = "192.168.1.16"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))
data =  client.recv(1024)

print(data.decode())
client.close()

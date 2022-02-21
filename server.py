import socket

LOCALHOST = "192.168.1.17"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)

print("Server started")
print("Waiting for client request..")



msg = ''

while True:
  clientConnection,clientAddress = server.accept()

  print("Connected clinet :" , clientAddress)

  
  in_data = clientConnection.recv(1024)
  msg = in_data.decode()

  if msg=='bye':
    break

  print("From Client :" , msg)
  out_data = input("Message: ")
  clientConnection.send(bytes(out_data,'UTF-8'))

print("Client disconnected....")
clientConnection.close()
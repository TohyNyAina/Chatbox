import socket

host = "192.168.11.56"
port = 5000
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen(2)
cnx, address = server_socket.accept()
print("connection from : " + str(address))

while True:
    data = cnx.recv(1024).decode()
    if not data:
        break
    print(("from connected user : " + str(data)))
    data = input(' -> ')
    cnx.send(data.encode())
cnx.close()
import socket
server= socket.socket()
host = socket.gethostname()
port = 4447
server.bind((host,port))
server.listen(5)
while True:
    client,address = server.accept()
    while True:
       data=client.recv(1024)
       print(f"Avi:{data} ")
       send= input("You: ")
       client.send(str.encode(send))

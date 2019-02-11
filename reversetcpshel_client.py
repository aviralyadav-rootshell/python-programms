#client
import socket
client =  socket.socket()
host= "127.0.0.1"
port = 5556
client.connect((host,port))
print(f'Success fully connected to {host}')
while True:
    cmd= input("shell>")
    client.send(str.encode(cmd))
    respond=client.recv(1024)
    respond=respond.decode()
    print(respond)

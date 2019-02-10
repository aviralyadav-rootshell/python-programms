import socket
ser = socket.socket()
host = socket.gethostname()
port = 4449
ser.bind((host,port))
ser.listen(2)
while True:
    try:
       client,address= ser.accept()
       print(f'Connection from {address} stablished ')
    except:
      print("\n\n\n\t\t\tSorry : fail to connect")

    try:
        client.send("thanks for connection")
    except:
       print("\n\n\n\t\t\tSorry : fail to respond")
    client.close()

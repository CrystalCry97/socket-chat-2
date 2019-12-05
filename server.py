import sys
from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024
LOCK = False
LOCK_HOLDER = ""

hostName = gethostbyname( '0.0.0.0' )

mySocket = socket( AF_INET, SOCK_DGRAM )
mySocket.bind( (hostName, PORT_NUMBER) )

print ("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
    (data,addr) = mySocket.recvfrom(SIZE)
    print (data.decode())
    if "getlock" in data.decode():
        if LOCK == False:
            LOCK = True
            LOCK_HOLDER = data.decode().split(':')[0]
            print(f"Server: {LOCK_HOLDER} get the lock")
        else:
            print (f"Server: {LOCK_HOLDER} took the lock. Please wait.")
    elif "releaselock" in data.decode():
        if LOCK_HOLDER == data.decode().split(':')[0]:
            LOCK = False
            print (f"Server: {LOCK_HOLDER} released the lock")
            LOCK_HOLDER = ""
        else:
            # print(f"{LOCK_HOLDER} !== {data.decode().split(':')[0]}")
            print (f"Server: {data.decode().split(':')[0]} not hold the lock")

    # msg = input("SERVER: ")
    # mySocket.sendto(msg.encode(),(SERVER_IP,PORT_NUMBER))
sys.exit()
import sys
from socket import socket, AF_INET, SOCK_DGRAM

SERVER_IP   = '127.0.0.1'
PORT_NUMBER = 5000
SIZE = 1024

print ("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket( AF_INET, SOCK_DGRAM )

name = input("Please enter your name: ")

while True:
        msg = input(f"{name}: ")
        mySocket.sendto(f"{name}: {msg}".encode(),(SERVER_IP,PORT_NUMBER))
        # (data,addr) = mySocket.recvfrom(SIZE)
        # print ("SERVER: " + data.decode())
sys.exit()
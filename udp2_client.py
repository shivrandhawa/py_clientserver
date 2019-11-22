#!/usr/bin/env python3
import time
import socket
from classes import testclass


pack = testclass.Packet(1,"0","car","22",0)

print(pack.type)
print(pack.WindowSize)
time.sleep(99)

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ("10.211.55.3",5003)

sock.bind(address)

sock.sendto("FirstMsg from Client".encode(),("10.211.55.4",5002)) #2 args, data being sent and list containing adddress 
print(address)

while True:
	data,addr = sock.recvfrom(1024)
	print ("ACK recieved -> ",data.decode(),"|| FROM: ",addr)
	inp = input("next message to send:  ")
	sock.sendto(inp.encode(),("10.211.55.4",5002)) #2 args, data being sent and list containing adddress 




# while True:
# 	data, addr = sock.recvfrom(1024) #data contains string addr contains address of sender
# 	print(data.decode())
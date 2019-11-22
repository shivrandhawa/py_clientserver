#!/usr/bin/env python3

import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
address = ("127.0.0.1", 5002)	#list of address and port

sock.bind(address)
print(address)

ACKNUM = 0

def SendAck():
	sock.sendto(ACKNUM,("127.0.0.1",5002)) #2 args, data being sent and list containing adddress 
	ACKNUM+=1



data = None
while True: 
	data, addr = sock.recvfrom(1024) #data contains string addr contains address of sender
	
	print(data.decode())  #decode() removes the b b4 data
	print(" sender address:  ")
	print (addr)

	# if data is not None:
	# 		sock.sendto("data recieved".encode(),("127.0.0.1",5002))
	# 		data  None

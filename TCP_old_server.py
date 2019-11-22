#!/usr/bin/python3
import socket
import os.path

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 7005
port2 = 7006

def send_file():
	#rec. file name from client
	filename = conn2.recv(1024) 
	if os.path.isfile(filename):	#checking if file exists
		print(filename, "Exisits, transfering now")
		file = open(filename, 'rb')  # readbytes mode
		file_data = file.read(1024)
		conn2.send(file_data)
		print("Data has been transmitted successfully")
		
	else:
		print("File does not exist")
		s.close()
		socket_data.close()		
		quit()

def rec_file():
	filename = "transferred_file.txt"
	file = open(filename, 'wb')
	file_data = conn2.recv(1024)
	file.write(file_data)
	file.close()
	print("File has been received successfully. ")
	s.close()
	socket_data.close()


s.bind((host, port))
s.listen(10)
print(host)
print("waiting for any incomming connections...")
conn, addr = s.accept()
print(addr, "Has connected to the server")



msg = conn.recv(1024)
msg = msg.decode("utf-8")
if msg == "send":
	socket_data= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_data.bind((host, port2))
	socket_data.listen(10)
	conn2, addr = socket_data.accept()
	print("file being received")
	rec_file()
	s.close()
	socket_data.close()
elif msg =="get":
	socket_data= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_data.bind((host, port2))
	socket_data.listen(10)
	conn2, addr = socket_data.accept()
	print("sending a file")
	send_file()
	s.close()
	socket_data.close()


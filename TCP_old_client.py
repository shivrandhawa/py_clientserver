#!/usr/bin/python3
import socket
import sys
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = sys.argv[1]
port = 7005
port2 = 7006

def get():
	s.send("get".encode())
	time.sleep(1)
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s2.connect((host, port2))
	filename = input(str("please enter a filename to take -> "))
	s2.send(filename.encode())
	file = open(filename, 'wb')
	file_data = s2.recv(1024)
	file.write(file_data)
	file.close()
	print("File has been received successfully. ")
	s.close()
	s2.close()

def send():
	s.send("send".encode())
	print("hi")
	time.sleep(1)
	s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s2.connect((host, port2))
	filename = input(str("please enter filename of file to send -> "))
	# new_name = input(str("enter name to give new file on server"))
	file = open(filename, 'rb')  # readbytes mode
	file_data = file.read(1024)
	s2.send(file_data)
	print("Data ha been transmitted successfully")
	s.close()
	s2.close()


s.connect((host, port))
print("connected...")

command = input("get or send file:  ")


if command == "get":
    get()
if command == "send":
    print("sendhi")
    send()

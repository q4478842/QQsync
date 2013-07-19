#!D:/Python27/Python
# Filename : qqClient.py


import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port = 1234
s.connect(('192.168.60.219',port))
s.sendall("hello,world\n")
s.sendall("hello,world")
s.close()

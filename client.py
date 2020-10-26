# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:32:30 2020

@author: sullivana6
"""
import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 1234))


msg = ''
while msg != 'exit':
    msg = s.recv(1024)
    print("Server: " + msg.decode("utf-8") + "\n")
    msg = input("Client: ")
    s.send(bytes(msg, "utf-8"))

s.close()

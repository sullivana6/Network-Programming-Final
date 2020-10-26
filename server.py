# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:20:12 2020

@author: sullivana6
"""

import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Current machine address is ', socket.gethostname())
s.bind(('', 1234)) #socket.gethostname()
s.listen(5)

clientsocket, address = s.accept()
msg = ' '

while msg != None:
    msg = input('Server: ')
    clientsocket.send(bytes(msg, "utf-8"))
    msg = clientsocket.recv(1024)
    print("Client: " + msg.decode("utf-8") + "\n")

clientsocket.close
    
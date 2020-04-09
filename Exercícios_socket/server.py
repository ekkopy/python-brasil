# -*- coding: utf-8 -*-

from socket import socket, gethostname, close
from os import path, getenv
from dotenv import load_dotenv


print("""
    ####  ###### #####  #    # ###### #####  
   #      #      #    # #    # #      #    # 
    ####  #####  #    # #    # #####  #    # 
        # #      #####  #    # #      #####  
   #    # #      #   #   #  #  #      #   #  
    ####  ###### #    #   ##   ###### #    # 

   [*] Author: ekkopy
   [*] Date: 04/09/2020
   [*] GitHub: https://github.com/ekkopy                                         
""")

# Load share folder
load_dotenv()
folder = getenv('PASTA_COMPARTILHADA')

port = 8000
server_socket = socket()
host = gethostname()
server_socket.bind((host, port))
server_socket.listen(5)
print("[*] Server on...\n")

while True:
    connection, addres = server_socket.accept()
    response = connection.recv(1024).decode()
    absoluto = folder + "/" + response
    print(absoluto)
    assert path.exists(absoluto), "Not found"
    with open(absoluto, 'rb') as fl:
        row = fl.read(1024)
        connection.send(row)
    fl.close()
    connection.send(b"Thanks for connecting...")
    connection.close()
    break
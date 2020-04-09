# -*- coding: utf-8 -*-

from socket import socket, gethostname
from os import path

print("""
  ####    #      # ###### #    # ##### 
  #    #  #      # #      ##   #   #   
  #       #      # #####  # #  #   #   
  #       #      # #      #  # #   #   
  #    #  #      # #      #   ##   #   
  ####    ###### # ###### #    #   #   

  [*] Author: Thiago Martins AKa ekkopy
  [*] Date: 04/09/2020
  [*] GitHub: https://github.com/ekkopy 
""")

nome_arquivo = input("Name of file: ")
client_socket = socket()
host = gethostname()
port = 8000 
client_socket.connect((host, port))
client_socket.send(nome_arquivo.encode())
data = client_socket.recv(1024).decode()
with open(nome_arquivo, 'w') as arquivo_recebido:
  arquivo_recebido.write(data)
  arquivo_recebido.close()
client_socket.close()
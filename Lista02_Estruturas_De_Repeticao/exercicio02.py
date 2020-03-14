# -*- coding: utf-8 -*-

"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

username = input('Digite seu nome de usuario: ')
password = input('Digite sua senha: ')

while username == password:
    print(f"Nome de usuario e senhas são iguais: {username} - {password}\nInforme corretamente!")
    username = input('Digite seu nome de usuario: ')
    password = input('Digite sua senha: ')

print(f"Username: {username} - Password: {password}")    


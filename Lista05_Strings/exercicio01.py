# -*- coding: utf-8 -*-

"""
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings 
possuem o mesmo comprimento e são iguais ou diferentes no conteúdo
"""

print("Compara duas strings!")

string01 = input("Informe a primeira string: ")
string02 = input("Informe a segunda string: ")

print(f"Tamanho de {string01} : {len(string01)} caracteres")
print(f"Tamanho de {string02} : {len(string02)} caracteres")

if len(string01) != len(string02):
    print(f"As strings {string01} e {string02} possuem tamanhos diferentes!")
    print(f"As strings {string01} e {string02} possuem conteudos diferentes!")
else:
    print(f"Strings com tamanho igual! {len(string01)} caracteres!")
    if string01 == string02:
        print(f"As strings {string01} e {string02} possuem o mesmo conteudo!")
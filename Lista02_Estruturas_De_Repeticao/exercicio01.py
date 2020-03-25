# -*- coding: utf-8 -*- 

"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e 
continue pedindo até que o usuário informe um valor válido.
""" 

def ler_numero(nota = None):
    nota = int(input("Digite uma nota entre zero e dez: "))
    if nota >= 0 and nota <= 10:
        print(f"Nota valida: {nota}")
        return False # Quebra o loop
    else:
        print(f"Nota invalida: {nota}\nPor favor informe uma nota entre zero e dez!")
        ler_numero(nota)

while(ler_numero()):
    ler_numero()
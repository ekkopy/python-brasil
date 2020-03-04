# -*- coding: utf-8 -*-

"""
Exercício 04 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.1
"""

letra = input("Digite uma letra: ")
letra = letra.lower()

# Lista de vogais e consoantes
vogal = ['a', 'e', 'i', 'o', 'u']
cons = ['b', 'c,' 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

if letra in vogal:
    print(f"{letra} é uma vogal!")
else:
    print(f"{letra} é uma consoante!")
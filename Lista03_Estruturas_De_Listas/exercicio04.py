# -*- coding> utf-8 -*-

"""
Faça um Programa que leia um vetor de 10 caracterese diga quantas consoantes foram lidas. 
Imprima as consoantes.
"""

consoantes = []

vogais = ['a', 'e', 'i', 'o', 'u']

novasConsoantes =  []

for letra in range(0, 10):
    consoantes.append(input("Digite o " + str(letra) + " caractere: ").lower())

totalConsoantes = 0

for x in range(0, 10):
    if not consoantes[x] in vogais:
        novasConsoantes.append(consoantes[x])
        totalConsoantes += 1

print(f"Total de consoantes: {totalConsoantes}\nConsoantes: {novasConsoantes}")
# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

lista_numeros =  []

for x in range(1, 11):
    numero = int(input("Digite o " + str(x) + "º numero: "))
    lista_numeros.append(numero)

lista_numeros.reverse() # alternativo: lista_numeros[::-1]

for numeros in lista_numeros:
    print(numeros)
    
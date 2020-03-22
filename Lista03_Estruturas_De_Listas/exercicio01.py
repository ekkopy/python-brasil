# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""

lista = []

for x in range(1, 6):
    numero = int(input("Digite o " + str(x) + "º numero: "))
    lista.append(numero)

for numeros in lista: print(f"Numeros: {numeros}")
# -*- coding: utf-8 -*-


"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores.
"""

vetorEntrada = []
vetorPar = []
vetorImpar = []

for x in range(0, 20):
    vetorEntrada.append(int(input("Digite o " + str(x) + "º numero: ")))

for y in vetorEntrada:
    if y % 2 == 0:
        vetorPar.append(y)
    else:
        vetorImpar.append(y)

print(f"Vetor Par => {vetorPar}")
print(f"Vetor Impar => {vetorImpar}")
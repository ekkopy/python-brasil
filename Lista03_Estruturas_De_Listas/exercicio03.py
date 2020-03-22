# -*- coding: utf-8 -*-


"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

for x in range(0, 4):
    notas.append(float(input("Digite a " + str(x) + " nota: ")))

soma = 0
print("\nNotas informadas!")

for y in range(0, 4):
    print(f"Nota: {y}")
    soma += notas[y]

print(f"Média das notas: {soma/4}")
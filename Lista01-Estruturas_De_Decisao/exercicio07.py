# -*- coding: utf-8 -*-

"""
Exrecício 07 - Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 == n2 and n1 == n3:
    print(f"Os numeros sao iguais: {n1}, {n2} e {n3}")
else:
    # Acha o maior
    if n1 > n2 and n1 > n3:
        print(f"O maior numero é: {n1}")
    elif n2 > n1 and n2 > n3:
        print(f"O maior numero é: {n2}")
    else:
        print(f"O maior numero é: {n3}")
    # Acha o menor
    if n1 < n2 and n1 < n3:
        print(f"O menor numero é: {n1}")
    elif n2 < n1 and n2 < n3:
        print(f"O menor numero é: {n2}")
    else:
        print(f"O menor numero é: {n3}")
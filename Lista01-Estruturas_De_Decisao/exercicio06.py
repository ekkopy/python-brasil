# -*- coding: utf-8 -*-

"""
Exercício 06 - aça um Programa que leia três números e mostre o maior deles.
""" 
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 == n2 and n1 == n3:
    print(f"Os numeros sao iguais: {n1}, {n2} e {n3}")
elif n1 > n2 and n1 > n3:
    print(f"O maior numero é: {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior numero é: {n2}")
else:
    print(f"O maior numero é: {n3}")


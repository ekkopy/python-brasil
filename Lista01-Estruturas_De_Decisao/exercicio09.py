# -*- coding: utf-8 -*-

"""
Exercício 09 - Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
n3 = int(input("Digite o terceiro numero: "))

if n1 == n2 and n1 == n3:
    print(f"Numeros iguais! {n1}, {n2} e {n3}")
else:
    if n1 >= n2 and n1 >= n3:
        print(n1)
        if n2 >= n3:
            print(n2)
            print(n3)
        else:
            print(n3)
            print(n2)
    elif n2 >= n3:
        print(n2)
        if n1 >= n3:
            print(n1)
            print(n3)
        else:
            print(n3)
        print(n1)
    else:
        print(n3)
        if n1 >= n2:
            print(n1)
            print(n2)
        else:
            print(n2)
            print(n1)
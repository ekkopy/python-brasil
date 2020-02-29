#-*- coding: utf-8 -*-

"""
  Exercício 01 - Faça um programa que peça dois números e imprima o maior deles
"""
n1 = float(input("Informe o primeiro numero: "))
n2 = float(input("Informe o segundo numero: "))

if n1 > n2:
    print(f"{n1} e maior que {n2}")
elif n2 > n1:
    print(f"{n2} e maior que {n1}")
else:
    print(f"{n1} e {n2} sao iguais!")
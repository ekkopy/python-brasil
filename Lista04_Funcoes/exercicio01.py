# -*- coding: utf-8 -*-


"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
"""

def repeatNumber(numbr):
    for x in range(numbr):
        x += 1
        print(f"{str(x) * x}")

repeatNumber(int(
    input("Digite um numero: ")))

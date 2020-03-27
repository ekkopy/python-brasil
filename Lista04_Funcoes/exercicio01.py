# -*- coding: utf-8 -*-

def repeatNumber(numbr):
    for x in range(numbr):
        x += 1
        print(f"{str(x) * x}")

repeatNumber(int(
    input("Digite um numero: ")))

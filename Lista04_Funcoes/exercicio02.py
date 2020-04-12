# -*- coding: utf-8 -*-

"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
"""

def repetirAteN(numero):
    x = 1
    if isinstance(numero, int):
       while x <= numero:
            y = 1
            separador = ''
            while y <= x:
               separador += f"{str(y)}\t"
               y+=1
            print(separador)
            x+=1

repetirAteN(
    int(input("Informe um numero: "))
)

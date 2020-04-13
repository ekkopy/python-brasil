# -*- coding: utf-8 -*-

"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
 se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
"""

def returnElement(number) -> str:
    if number > 0:
        return 'P'
    return 'N'

print(returnElement(
       int(input("Digite um numero: "))
    )
)
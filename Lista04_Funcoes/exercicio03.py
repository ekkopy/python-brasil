# -*- coding: utf-8 -*-

"""
Faça um programa, com uma função que necessite de três argumentos, 
e que forneça a soma desses três argumentos.
"""

def somarArgs(args = []) -> int:
   count = 0
   for x in args:
       count += x
   return count

numeros = []

for x in range(1, 4):
    numeros.append(int(
        input("Digite o " + str(x) + " numero: ")))

print(f"Somatório: {somarArgs(numeros)}")
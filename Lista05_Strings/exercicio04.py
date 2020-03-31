# -*- coding: utf-8 -*-

"""
Nome na vertical em escada. 
Modifique o programa anterior de forma a mostrar o nome em formato de escada.
"""

nome = input("Informe seu nome: ")

for x in range(0, len(nome) + 1):
    print(nome[:x])
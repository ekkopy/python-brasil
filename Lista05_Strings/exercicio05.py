# -*- coding: utf-8 -*-

"""
Nome na vertical em escada invertida. 
Altere o programa anterior de modo que a escada seja invertid
"""

nome = input("Informe seu nome: ")

for x in range(len(nome) + 1, -1, -1):
    print(nome[:x])
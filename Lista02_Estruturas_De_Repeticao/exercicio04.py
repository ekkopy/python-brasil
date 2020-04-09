# -*- coding: utf-8 -*-


"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que 
calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento.
"""

popA = 80000
crescA = 1.03
popB = 200000
crescB = 1.015

ano = 1
while (popA <= popB):
    popA *= crescA
    popB *= crescB
    ano += 1

print(f"Serao necessarios: {ano} anos para que a populacao do pais A ultrapasse a populacao do pais B")
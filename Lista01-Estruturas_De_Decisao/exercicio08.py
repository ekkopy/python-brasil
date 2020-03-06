# -*- coding: utf-8 -*-


"""
Exercício 08 - Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

produto01 = float(input("Digite o primeiro numero: "))
produto02 = float(input("Digite o segundo numero: "))
produto03 = float(input("Digite o terceiro numero: "))

# Comparação de preços entre produtos
if produto01 == produto02 and produto01 == produto03:
    print(f"Produtos com preços iguais: R${produto01},00, R${produto02},00 e R${produto03}, 00")
elif produto01 < produto02 and produto01 < produto03:
    print(f"Você deve comprar o produto01! => Preço: R${produto01},00")
elif produto02 < produto01 and produto02 < produto03:
    print(f"Você deve comprar o produto02! => Preço: R${produto02}, 00")
else:
    print(f"Você deve comprar o produto03! => Preço: R${produto03}, 00")
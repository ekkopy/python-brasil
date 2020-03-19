# -*- coding: utf-8 -*-

"""
Faça um Programa que peça a temperatura em graus Farenheit, 
transforme e mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""

fh = float(input("Informe a temperatura em Farenheit: "))
celsius = (fh - 32) * 5/9
print(f"{fh}ºF convertido para celsius equivalem a {round(celsius, 3)}ªC")
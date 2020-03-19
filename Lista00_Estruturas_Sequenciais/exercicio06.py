# -*- coding: utf-8  -*-

"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""

from math import pi

raio = int(input("Informe a medida do raio: "))
print(f"Area do circulo do raio: {raio} e aproximadamente: {(raio * raio) * pi} mm²")
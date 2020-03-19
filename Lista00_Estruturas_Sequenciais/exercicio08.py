# -*- coding: utf-8 -*-

"""
Faça um Programa que pergunte quanto você ganha por hora e o 
número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês.
"""

salario_hora = float(input("Qual o valor da sua hora de trabalho ? "))
numero_horas = float(input("Quantas horas você trabalha por mês ?  "))
print(f"Seu salário mensal: {salario_hora * numero_horas}")
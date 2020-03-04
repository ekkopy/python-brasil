# -*- coding: utf-8 -*-

"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda  nota: "))

media = (nota01 + nota02) / 2
media = int(media)

if media == 10:
    print(f"Aluno aprovado com distincao!")
elif media >= 7:
    print(f"Aprovado!\nMedia: {media}")
else: # Media menor que 7
    print(f"Reprovado!\nMedia: {media}")    

# -*- coding: utf-8 -*-

"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

nome = ""
while len(nome) <= 3:
    nome = input("Digite seu nome: ")
    if len(nome) <= 3:
        print(f"Nome deve deve ter mais que 3 caracteres: {nome}")


idade = -1
while idade < 0 or idade > 150:
    idade = int(input("Digite sua idade: "))
    if idade < 0 or idade > 150:
        print(f"Idade deve ser maior que zero e menor que 150: {idade}")

salario = -1
while salario < 0:
    salario = float(input("Digite seu salario: "))
    if salario < 0:
        print(f"Salario deve ser maior que zero: {salario}")

sexo = ''
while sexo != 'f' and sexo != 'm':
    sexo = input("Digite o sexo (f - feminino ou m - masculino):  ")
    sexo = sexo.lower()
    if sexo != 'f' and sexo != 'm':
        print(f"Sexo deve ser f ou m: {sexo}")

estado_civil = ['s', 'c', 'v', 'd']
estado = ''
while not estado in estado_civil:
    print("S - Solteiro(a), C - Casado(a), V - Viuvo(a), D - Divorciado(a)")
    estado = input("Informe seu estado civil: ")
    estado = estado.lower()
    if not estado in estado_civil:
        print(f"Estado civil invalido: {estado}")

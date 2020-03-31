# -*- coding: utf-8 -*-

"""
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

a-) quantos espaços em branco existem na frase.
b-) quantas vezes aparecem as vogais a, e, i, o, u.
"""

string = input("Digite a string: ")
vogais = {'a', 'e', 'i', 'o', 'u'}

count_espaco = 0
count_vogais = 0

for x in string:
    if x in vogais:
        count_vogais += 1
    if x == " ":
        count_espaco += 1  

print(f"Quantidade de vogais: {count_vogais}")
print(f"Quantidade de espaços: {count_espaco}")
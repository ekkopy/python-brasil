# -*- coding: utf-8 -*-

from os import path

"""
Faça um programa que:
Solicite ao usuário que digite o nome de um arquivo texto (caminho completo);
Solicite ao usuário que digite uma palavra;
Verifique em todo arquivo quais as linhas contêm a palavra. Todas as linhas localizadas devem ser salvas em um 
novo arquivo texto com o nome FIND_<nome_arquivo_original>, contendo o seguinte :
"""

#caminho = "C:\python_play\exercicios_slides\exercicio01.txt"

caminho =  input("Informe o path do arquivo: ")
assert path.exists(caminho), f"Caminho não encontrado! {caminho}"

palavra = input("Digite a palavra que deseja procurar: ")
mydct = {}
count = 1
with open(caminho, 'r') as arquivo_original:
    for linha in arquivo_original:
        row = linha.split('\n')
        if palavra in row:
            mydct[count] = palavra
        count += 1
    arquivo_original.close()

print(f"Gravando conteúdo no arquivo d FIND_arquivo_original.txt\n")

with open('FIND_arquivo_original', 'w+') as arquivo_find:
    arquivo_find.write('Arquivo Original\n')
    arquivo_find.write(f"Palavra procurada{palavra}\n")
    for x in mydct:
        arquivo_find.write(f"Nº da linha: {x} - Palavra: {mydct[x]}\n")
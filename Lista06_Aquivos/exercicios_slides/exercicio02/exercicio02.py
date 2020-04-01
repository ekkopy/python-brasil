# -*- coding: utf-8 -*-

from os import listdir, path

"""
Faça um programa que:
Solicite ao usuário que digite a unidade e nome de um diretório qualquer (path);
Solicite ao usuário que digite uma palavra;
Verifique em todos os arquivos texto (.txt) quais as linhas contêm a palavra. Todas as linhas localizadas devem ser salvas em um novo arquivo texto com o nome FIND_GERAL, contendo o seguinte :

<Palavra localizada>

[<Nome do arquivo original 1>][<nº linha>]<linha de texto>
[<Nome do arquivo original 2>][<nº linha>]<linha de texto>
[<Nome do arquivo original N>][<nº linha>]<linha de texto>
"""
caminho = input("Informe o diretório para leitura: ")
assert path.exists(caminho), f"Diretório não encontrado: {caminho}"

palavraProcurada = input("Qual palavra deseja procurar? ")
lista_arquivos = []
lista_linhas = []
contador = 1
loopArquivo = 0
loopLinha = 0

# Começa leitura dos arquivos
for arquivo in listdir(caminho):
    if arquivo.endswith(".txt"):
        with open(arquivo, 'r') as arquivoEntrada:
          for linhas in arquivoEntrada:
            linha = linhas.split('\n')
            if palavraProcurada in linha:
                lista_linhas.append(contador)
                lista_arquivos.append(arquivo)
            contador += 1
        contador = 1    
        arquivoEntrada.close()

while loopArquivo < len(lista_arquivos):
    while loopLinha <= loopArquivo:
        with open('FIND_GERAL.txt', 'a') as arquivoSaida:
            arquivoSaida.write(f"Arquivo: {lista_arquivos[loopArquivo]} - Linha: {lista_linhas[loopLinha]} - Palavra: {palavraProcurada}\n")
        arquivoSaida.close()
        loopLinha += 1
    loopArquivo += 1

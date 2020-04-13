# -*- coding: utf-8 -*-


"""
Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
O arquivo de saída possui o seguinte formato:
[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""


def validarEnderecoIp(ip) -> bool:
    blocosIp = ip.split('.')
    if len(blocosIp) != 4:
        return False
    for bloco in blocosIp:
        blc = int(bloco)
        if blc < 0 or blc > 255:
            return False
    return True  

ipsValidos = []
ipsInvalidos = []

with open('entrada.txt', 'r') as arquivoEntrada:
    linhArquivo = arquivoEntrada.readlines()
    for ip in linhArquivo:
        if validarEnderecoIp(ip.strip('.')):
            ipsValidos.append(ip)
        else:
            ipsInvalidos.append(ip)
    arquivoEntrada.close()

with open('saida.txt', 'w') as arquivoSaida:
    arquivoSaida.write("Enderecos validos\n")
    for ipValido in ipsValidos:
        arquivoSaida.write(ipValido)
        #arquivoSaida.write('\n')
    arquivoSaida.write('\nEnderecos Invalidos\n')
    for ipInvalido in ipsInvalidos:
        arquivoSaida.write(ipInvalido)
        #arquivoSaida.write('\n')
    arquivoSaida.close()

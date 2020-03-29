# -*- coding: utf-8 -*-

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

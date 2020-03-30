# -*- codidng: utf-8 -*-

def byteParaMegaByte(byte) -> float:
    try:
        return round((byte / (1024 * 1024)), 2)
    except ZeroDivisionError:
        return 0

def calcPercentual(valor, percentual) -> float:
    try:
        return valor / percentual
    except ZeroDivisionError:
        return 0

usuario_linha = []
usuarios = []
espacosUtilizados = []
espacoTotal = 0.0

with open('usuarios.txt', 'r') as usuarios_servidor:
    usuario_linha = usuarios_servidor.readlines()
    usuarios_servidor.close()

for linha in usuario_linha:
    campos = linha.split()
    usuario = campos[0]
    espacoUtilizado = int(campos[1])
    usuarios.append(usuario)
    espacosUtilizados.append(espacoUtilizado)
    espacoTotal += espacoUtilizado


with open('relatorio.txt', 'w') as relatorio:
    relatorio.write("""
    ACME Inc.               Uso do espaço em disco pelos usuários
    ------------------------------------------------------------------------
    Nr.  Usuário        Espaço utilizado     % do uso """)
    for x in range(0, len(usuarios)):
        espacoMB = byteParaMegaByte(espacosUtilizados[x])
        percentual = calcPercentual(espacosUtilizados[x], espacoTotal)
        relatorio.write(f"\n\t{x + 1} {usuarios[x]} \t\t {espacoMB} MB \t\t\t  {round((percentual * 100.0), 2)}%\n")

    relatorio.write(f"\nEspaço total: {round((espacoTotal / (1024 * 1024)), 2)} MB\n")
    relatorio.write(f"\nEspaço médio ocupado: {round(espacoTotal / len(usuarios) / (1024 * 1024), 2)} MB")
    relatorio.close()
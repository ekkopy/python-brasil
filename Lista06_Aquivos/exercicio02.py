# -*- codidng: utf-8 -*-


"""
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
"""

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
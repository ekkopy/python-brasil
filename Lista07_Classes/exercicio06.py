# -*- coding: utf-8 -*-

from myclass.tv import Tv

tv = Tv()

def volume():
    opcao = int(input("Você gostaria de: 1-Aumentar ou 2-Diminuir o volume ? "))
    if opcao == 1:
        tv.aumentarVoluime()
    elif opcao == 2:
        tv.diminuirVolume()
    else:
        print(f"Opção invalida! {opcao}")
        volume()

def canal():
    canal = int(input("Qual canal deseja? "))
    tv.definirCanal(canal)

menu = """
    | /~~~~~~~~\ ||||
    ||          |...|
    ||          |   |
    | \________/  O |
    ~~~~~~~~~~~~~~~
    [*] Aluno: Thiago Martins de Oliveira Silva
    [*] RA: 317112142

    Opções: 
    1 - Qual canal deseja sintonizar ? 
    2 - Aumentar volume: 
    3 - Diminuir volume: 
    4 - Desligar TV
"""
print(menu)

continuar = 1

while continuar != 2:
    canal()
    volume()
    continuar = int(input("Deseja continuar ? 1-Sim e 2-Nao: "))
    print(tv.volume)

print("Desligando a tv...")
del tv



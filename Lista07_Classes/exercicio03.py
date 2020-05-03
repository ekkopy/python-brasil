# -*- coding: utf-8 -*-

from myclass.retangulo import Retangulo

base = float(input("Informe a base do retangulo: "))
altura = float(input("Informe a altura do retangulo: "))

# Inicializa os atributos
retangulo = Retangulo(base, altura)

# Display menu
menu = """
    1 - Mudar o valor dos lados (base e altura)\n
    2 - Retornar o valor dos lados\n
    3 - Calcular Area\n
    4 - Calcular perimetro
"""

print(menu)

opcao = int(input("Qual opcao você deseja ?"))

if opcao == 1:
    base = float(input("Digite o novo valor da base: "))
    altura = float(input("Digite o novo valor da altura: "))
    retangulo.mudarValorDosLados(base, altura)
elif opcao == 2:
    retangulo.retornarValorDosLados()
elif opcao == 3:
    print(f"Valor da area: {retangulo.calcularArea()}")
elif opcao == 4:
    print(f"Calculo de perimetro: {retangulo.calcularPerimetro()}")
else:
    print(f"Opção invalida: {opcao}...")
    print("Saindo...")
# -*- coding: utf-8 -*-

def somaImposto(taxaImposto, custo) -> float:
    custo = custo + (custo * taxaImposto / 100)
    return custo

taxaImposto = float(input("Informe o valor da taxa de imposto: "))
custo = float(input("Informe o valor do produto: "))

print(f"Preço dos impostos sobre o produto e: {somaImposto(taxaImposto, custo)}")
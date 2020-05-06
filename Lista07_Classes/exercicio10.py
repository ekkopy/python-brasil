# -*- coding: utf-8 -*-

from myclass.bomba import BombaCombustivel

print("""
  ------------------------
  | Bomba de Combustivel |
  -----------------------  
""")

tipoCombustivel = input("Informe o tipo do combustivel: ")
valorLitro = float(input("Informe tipo de combustivel: "))
quantidadeCombustivel = float(input("Informe a quantidade de Combustivel que deseja abastecer: "))

# Instancia da classe
bombaCombust = BombaCombustivel(tipoCombustivel, valorLitro, quantidadeCombustivel)

print(f"""
Tipo de combustivel: {tipoCombustivel}\n
Valor do litro: R$ {valorLitro}\n
Quantidade abastecida: {quantidadeCombustivel}
""")

abastecerPorLtr = float(input("Informe a quantidade que deseja abastecer por Litro: "))

bombaCombust.abastercerPorLitro(abastecerPorLtr)
print(f"Quantidade de combustivel: {bombaCombust.quantidadeCombustivel}")

novoCombustivel = input("Informe um novo tipo de combustivel: ")

bombaCombust.alterarCombustivel(novoCombustivel)

abastecerPorVlr = float(input("Informe a quantia para abastecer em R$ "))

bombaCombust.abastecerPorValor(abastecerPorVlr)

print(f"""
Novo tipo de combustivel: {bombaCombust.tipoCombustivel}\n
Quantia abastecida: R$ {abastecerPorVlr}, 00\n
Quantidade abastecida: {bombaCombust.quantidadeCombustivel}
""")
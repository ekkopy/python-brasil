# -*- coding: utf-8 -*-

"""
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e
imprima a data com o nome do mês por extenso.
"""

meses = {
    1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 
    5: "Maio", 6: "Junho", 7: "Julho", 8: "Agosto",
    9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

data = input("Informe sua data de nascimento: ")
dia, mes, ano = data.split('/')

print(f"Você nasceu em {dia} de {meses[int(mes)]} de {ano}")    
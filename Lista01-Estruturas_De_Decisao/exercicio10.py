# -*- coding: utf-8 -*-

"""
Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", 
"Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

print("""
   \tM - Matutino\n
   \tV - Vespertino\n
   \tN = Noturno\n
""")

turno = input("Digite o turno que você estuda: ")

if turno == "m":
    print(f"{turno} => Turno Matutino")
elif turno == "v":
    print(f"{turno} => Turno Vespertino")
elif turno == "n":
    print(f"{turno} => Turno Noturno")
else:
    print(f"Turno inválido: {turno}")

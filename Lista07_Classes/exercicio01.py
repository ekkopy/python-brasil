# -*- coding: utf-8 -*-

from myclass.bola import Bola

bola = Bola()

bola.cor = input("Digite uma cor: ")
bola.circunferencia = float(input("Informe a cirncunferencia: "))
bola.material = input("Informe o material: ")

print(f""" 
   Cor: {bola.mostraCor()}
   Material: {bola.material}
   circunferencia: {bola.circunferencia}
""")

bola.trocaCor(input("Digite uma nova cor: "))

print(f""" 
   Cor: {bola.cor}
   Material: {bola.material}
   circunferencia: {bola.circunferencia}
""")

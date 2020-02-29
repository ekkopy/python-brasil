# -*- coding: utf-8 -*-

"""
Exercício 03 - Verifique se uma letra digitada é F ou M.
"""
print("F - para Feminino\nM - para Masculino:")

sexo = input("Informe o sexo: ")[0]
sexo = sexo.lower()

if sexo == "f":
    print(f"Você informou {sexo} de Feminino!")
elif sexo == "m":
    print(f"Você informou {sexo} de Masculino!")
else:
    print(f"Sexo inválido: {sexo}")
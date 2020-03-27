# -*- coding: utf-8 -*-

def somarArgs(args = []) -> int:
   count = 0
   for x in args:
       count += x
   return count

numeros = []
for x in range(1, 4):
    numeros.append(int(
        input("Digite o " + str(x) + " numero: ")))

print(f"Somatório: {somarArgs(numeros)}")
# -*- coding: utf-8 -*-

vetorEntrada = []
vetorPar = []
vetorImpar = []

for x in range(0, 20):
    vetorEntrada.append(int(input("Digite o " + str(x) + "º numero: ")))

for y in vetorEntrada:
    if y % 2 == 0:
        vetorPar.append(y)
    else:
        vetorImpar.append(y)

print(f"Vetor Par => {vetorPar}")
print(f"Vetor Impar => {vetorImpar}")
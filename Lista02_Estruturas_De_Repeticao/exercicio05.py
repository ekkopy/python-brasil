# -*- coding: utf-8 -*-

"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
""" 

popA = 0
crescA = 0

while popA <= 0:
    popA = int(input("Informe a populacao do pais A: "))
    if popA <= 0:
        print(f"Populacao deve ser um valor positivo! {popA}")

while crescA <= 0:
    crescA = float(input("Informe o percentual de crescimento do pais A: "))
    if crescA <= 0:
        print(f"Percentual de crescimento deve ser um valor positivo: {crescA}")

popB = popA

while popB <= popA:
    popB = int(input("Informe a populacao do pais B: "))
    if popB <= popA:
        print(f"Populacao do pais B deve ser maior que a populacao do pais A! {popB}")

crescB = crescA

while crescB >= crescA:
    crescB = float(input("Informe o percentual de crescimento do pais B: "))
    if crescB >= crescA:
        print (f"Percentual de crescimento do pais B deve ser menor que o do pais A! {crescB}")

crescA = 1 + (crescA / 100.0)
crescB = 1 + (crescB / 100.0)

ano = 1
while popA <= popB:
    popA *= crescA
    popB *= crescB
    ano += 1

print (f"Serao necessarios {ano} anos para que a populacao do pais A ultrapasse a populacao do pais B")

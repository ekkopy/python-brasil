# -*- coding: utf-8 -*-

def repeatTillN(numbr):
   for x in range(1, numbr + 1):
    for y in range(x, x+1):
        print(f"{y} ", end='')  # com o end você quebra o \n
    
repeatTillN(
    int(input("Digite um numero: "))
)
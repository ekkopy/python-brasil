# -*- coding: utf-8 -*-

def returnElement(number) -> str:
    if number > 0:
        return 'P'
    return 'N'

print(returnElement(
       int(input("Digite um numero: "))
    )
)
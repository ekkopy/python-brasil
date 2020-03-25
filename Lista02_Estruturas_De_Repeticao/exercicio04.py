# -*- coding: utf-8 -*-

popA = 80000
crescA = 1.03
popB = 200000
crescB = 1.015

ano = 1
while (popA <= popB):
    popA *= crescA
    popB *= crescB
    ano += 1

print(f"Serao necessarios: {ano} anos para que a populacao do pais A ultrapasse a populacao do pais B")
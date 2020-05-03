# -*- coding: utf-8 -*-


class Retangulo:

    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura 
    
    def mudarValorDosLados(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
    
    def retornarValorDosLados(self):
        print (f"Valor da base: {self.base}\nValor da altura: {self.altura}")
 
    def calcularArea(self) -> float:
        return self.base * self.altura
    
    def calcularPerimetro(self) -> float:
        return 2 * self.base + 2 * self.altura
    
   
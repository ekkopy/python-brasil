# -*- coding: utf-8 -*-

class Bola:
    """
    Classe para representar uma bola
    """

    cor = ""
    circunferencia = 0
    material = ""

    def trocaCor(self, novacor):
        self.cor = novacor

    def mostraCor(self):
        return self.cor
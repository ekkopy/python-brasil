# -*- coding: utf-8 -*-

class Tv:

    def __init__(self):
        self.volume = 0
        self.canal = 0

    def definirCanal(self, canal) -> float:
        if canal >= 0 and canal <= 100:
            self.canal = canal
            return self.canal

    def aumentarVoluime(self) -> float:
        if self.volume <= 100:
            self.volume += 1
            return self.volume
        
    def diminuirVolume(self) -> float:
        if self.volume > 0:
            self.volume -= 1
            return self.volume
 

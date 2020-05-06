# -*- coding: utf-8 -*-


class BombaCombustivel:
    tipoCombustivel = None
    valorLitro = 0
    quantidadeCombustivel = 0

    def __init__(self,
                 tipoCombustivel,
                 valorLitro,
                 quantidadeCombustivel
                 ):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.alterarQuantidadeCombustivel(quantidadeCombustivel)

    def abastecerPorValor(self, valorAbastecimento) -> float:
        litros = valorAbastecimento / self.valorLitro
        if litros <= self.quantidadeCombustivel:
            self.alterarQuantidadeCombustivel(
                self.quantidadeCombustivel - litros
            )

    def abastercerPorLitro(self, litros):
        if litros <= self.quantidadeCombustivel:
            self.alterarQuantidadeCombustivel(
                self.quantidadeCombustivel - litros
            )
            
    def alterarValor(self, novoValorLitro) -> float:
        self.valorLitro = novoValorLitro
        return self.valorLitro

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel
        return self.tipoCombustivel

    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel



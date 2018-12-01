#!/usr/bin/env python
import copy
from pprint import pprint
import random
from random import random, randint

class ProblemaMochila(object):
    """Encontrar a raiz de uma funcao."""

    class Estado(object):
        """Modelagem de um estado do problema."""

        def __init__(self):
            """Para este problema, começa com a mochila vazia."""

            """Peso, Valor"""
            self.prateleira = [
                [5, 20],
                [5, 20],
                [10, 100],
                [10, 100],
                [12, 120],
                [12, 120],
                [12, 120],
                [12, 120],
                [14, 110],
                [20, 90],
                [20, 90],
                [20, 90],
                [15, 30]
            ]

            self.mochila = []
            self.carga_atual = 0
            self.capacidade = 100
            self.valor_acumulado = 0

        def copy(self):
            estado = ProblemaMochila.Estado()

            estado.mochila = self.mochila.copy()
            estado.prateleira = self.prateleira.copy()
            estado.carga_atual = self.carga_atual
            estado.capacidade = self.capacidade
            estado.valor_acumulado = self.valor_acumulado
            return estado

        def __repr__(self):
            return f'Mochila: {self.mochila}\nPrateleira: {self.prateleira}\nValor Acumulado: {self.valor_acumulado}\nCarga Atual: {self.carga_atual}\n'

    @property
    def estado_inicial(self):
        """Gera um estado inicial"""
        estado = ProblemaMochila.Estado()
        return estado

    def funcao_objetivo(self, estado):
        """Avalia o valor dos itens acumulados no estado atual."""
        return estado.carga_atual


    def funcao_sucessora(self, estado):
        """Gera o estado vizinho"""
        estado_suc = estado.copy()

        """escolhe  um item aleatório da prateleira e adiciona a mochila"""
        index = randint(0, len(estado_suc.prateleira) - 1)

        item = estado_suc.prateleira[index]

        if item[0] < estado_suc.capacidade - estado_suc.carga_atual:
            estado_suc.mochila.append(item)
            estado_suc.prateleira.remove(item)

            estado_suc.carga_atual = estado_suc.carga_atual + item[0]
            estado_suc.valor_acumulado = estado_suc.valor_acumulado + item[1]

        return estado_suc

#!/usr/bin/env python
import copy
from pprint import pprint
from random import random, randint

class ProblemaMochila(object):
    """Encontrar a raiz de uma funcao."""

    class Estado(object):
        """Modelagem de um estado do problema."""

        def __init__(self):
            """Para este problema, começa com a mochila vazia."""

            """Peso - Valor"""
            self.prateleira = [
                [5, 20],
                [5, 20],
                [10, 100],
                [10, 100],
                [12, 120],
                [14, 110],
                [20, 90],
                [15, 30]
            ]

            self.mochila = []
            self.carga_atual = 0
            self.capacidade = 100
            self.valor_acumulado = 0


    @property
    def estado_inicial(self):
        """Gera um estado inicial aleatório"""
        estado = ProblemaMochila.Estado()
        return estado

    def funcao_objetivo(self, estado):
        """Avalia o custo do estado atual."""
        return estado.carga_atual


    def funcao_sucessora(self, estado):
        """Gera o estado vizinho"""

        return None;


    def adiciona_item(self, estado_pai, prateleira):

        estado = estado_pai

        """escolhe  um item aleatório"""
        item = prateleira[randint(0, estado.prateleira.size())]

        if item[0] < estado.carga_atual - estado.capacide:

            estado.mochila.append(item)
            estado.mochila.remove(item)

            estado.carga_atual = estado.carga_atual + item[0]
            estado.valor_acumulado = estado.valor_acumulado + item[1]

        return estado




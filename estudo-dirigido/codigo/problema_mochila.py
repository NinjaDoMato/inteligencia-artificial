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
                [14, 110],
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
            estado.prateleira = self.mochila.copy()
            estado.carga_atual = self.carga_atual
            estado.capacidade = self.capacidade
            estado.valor_acumulado = self.valor_acumulado
            return estado


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

        #while estado_suc.carga_atual < estado_suc.capacidade:

        """escolhe  um item aleatório da prateleira e adiciona a mochila"""

        índice = random.randrange(len(estado_suc.prateleira))
        item = estado_suc.prateleira[índice]

        if item[0] < estado_suc.carga_atual - estado_suc.capacide:
            estado_suc.mochila.append(item)
            estado_suc.mochila.remove(item)

            estado_suc.carga_atual = estado_suc.carga_atual + item[0]
            estado_suc.valor_acumulado = estado_suc.valor_acumulado + item[1]

        return estado_suc
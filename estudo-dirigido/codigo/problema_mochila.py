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
            self.prateleira = [
                ["joia", 5, 100],
                ["bolsa", 10, 100],
                ["sorvete", 15, 30]
            ]
            self.carga_atual = 0
            self.itens_atuais = []

            self.valor_acumulado = 0
            self.capacidade = 100

    @property
    def estado_inicial(self):
        """Gera um estado inicial aleatório"""

        estado = ProblemaMochila.Estado()

        estado.itens_atuais = [
            ["bolsa", 10, 100],
        ]
        estado.prateleira = [
                ["joia", 5, 100],
                ["sorvete", 15, 30]
            ]

        estado.carga_atual = 10
        estado.valor_acumulado = 100,
        estado.capacidade = 90

        return estado

    def funcao_objetivo(self, estado):
        """Avalia o custo do estado atual."""



        return None;

    def funcao_sucessora(self, estado):
        """Gera o estado vizinho"""
        return None;

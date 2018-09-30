#!/usr/bin/env python
import copy
from pprint import pprint
from random import random, randint

class ProblemaRaiz(object):
    """Encontrar a raiz de uma funcao."""

    @property
    def estado_inicial(self):
        """Para este problema, parte de um estado aleatorio."""
        sinal = 1 if randint(0, 1) == 1 else -1
        inteiro = randint(1, 10)
        return sinal * inteiro * random()

    def funcao_objetivo(self, estado):
        """Avalia o custo do estado atual."""
        x = estado
        return x ** 2 - 2

    def funcao_sucessora(self, estado):
        """Gera o estado vizinho"""
        sinal = 1 if randint(0, 1) == 1 else -1
        return estado + sinal * random()
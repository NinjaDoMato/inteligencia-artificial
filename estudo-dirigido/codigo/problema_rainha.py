#!/usr/bin/env python
import copy
from pprint import pprint
from random import random, randint


class ProblemaRainha(object):
    """Encontrar a raiz de uma funcao."""

    def __init__(self):
        self.n = 4

    @property
    def estado_inicial(self):
        """Para este problema, parte de um estado aleatorio."""
        estado = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]

        cont = 0
        while cont < self.n:
            i = randint(0, self.n - 1)
            j = randint(0, self.n - 1)
            if estado[i][j] == 0:
                estado[i][j] = 1
                cont += 1

        return estado

    def funcao_objetivo(self, estado):
        """Avalia o custo do estado atual."""
        conflitos = 0

        # conflitos em linhas
        for i in range(self.n):
            soma = 0
            for j in range(self.n):
                soma += estado[i][j]
            if soma > 1:
                conflitos += soma

        # conflitos em colunas
        for i in range(self.n):
            soma = 0
            for j in range(self.n):
                soma += estado[j][i]
            if soma > 1:
                conflitos += soma

        # conflitos na diagonal
        # TODO: verificar se tem conflito na diagonal

        return conflitos

    def funcao_sucessora(self, estado):
        """Gera o estado vizinho"""
        pos_vazia = (0, 0)
        pos_rainha = (0, 0)

        while True:
            i = randint(0, self.n - 1)
            j = randint(0, self.n - 1)
            if estado[i][j] == 0:
                pos_vazia = (i, j)
                break

        while True:
            i = randint(0, self.n - 1)
            j = randint(0, self.n - 1)
            if estado[i][j] == 1:
                pos_rainha = (i, j)
                break

        # copy: permite realizar a copia de objetos
        # deepcopy: realiza a copia recursiva dos objetos e seus atributos internos
        vizinho = copy.deepcopy(estado)

        vizinho[pos_rainha[0]][pos_rainha[1]] = 0
        vizinho[pos_vazia[0]][pos_vazia[1]] = 1

        return vizinho

#!/usr/bin/env python

import pandas as pd
import numpy as np
from problema import Problema

# Constantes para o problema dos missionarios e canibais

class Labirinto(Problema):

    """Definicao do problema do labirinto."""

    class Estado(object):
        """Modelagem de um estado do problema."""

        def __init__(self):
            self.linha = 0
            self.coluna = 0
            self.bloco = ''

            # Referencia para o estado pai. Usado para descobrir qual eh
            # a solucao do problema
            self.pai = None
            self.custo = 0
            self.acao = ''

        def copy(self):
            estado = Labirinto.Estado()
            estado.linha = self.lina.copy()
            estado.coluna = self.coluna.copy()
            estado.bloco = self.coluna.copy()

            return estado

        def __repr__(self):
            return f'[{self.linha}][{self.coluna}] | {self.bloco}'

        def __eq__(self, other):
            return self.linha == other.linha and self.coluna == other.coluna

    @property
    def estado_inicial(self):
        """Retorna o estado inicial do problema."""

        estado = Labirinto.Estado()
        estado.linha = 1
        estado.coluna = 0
        estado.bloco = 'E'









'''
arquivo = 'maze01.txt'

    # Lê a porra do arquivo
    file = open(arquivo, 'r')

    conteudo = file.readlines()

    file.close()

    print(conteudo[1][0])

'''
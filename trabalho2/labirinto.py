#!/usr/bin/env python
from problema import Problema
import pandas as pd

# Constantes para a resolução do labirinto

arquivo = 'maze01.txt'


class Labirinto(Problema):

    """Definicao do problema do labirinto."""

    class Estado(object):
        """Modelagem de um estado do problema."""

        def __init__(self):
            file = open('maze01.txt', 'r')
            labirinto = file.readlines()
            file.close()

            self.linha = 0
            self.coluna = 0
            self.bloco = ''
            self.labirinto = labirinto

            # Referencia para o estado pai. Usado para descobrir qual eh
            # a solucao do problema
            self.pai = None
            self.custo = 0
            self.acao = ''

        def copy(self):
            estado = Labirinto.Estado()
            estado.linha = self.linha#.copy()
            estado.coluna = self.coluna#.copy()
            estado.bloco = self.coluna#.copy()
            estado.labirinto = self.labirinto

            return estado

        def __repr__(self):
            #teste = pd.DataFrame(self.labirinto)
            #return f'{teste}'

            return f'[{self.linha}][{self.coluna}] - {self.bloco}'

        def __eq__(self, other):
            return self.linha == other.linha and self.coluna == other.coluna

    @property
    def estado_inicial(self):
        """Retorna o estado inicial do problema."""

        estado = Labirinto.Estado()
        estado.linha = 1
        estado.coluna = 0
        estado.bloco = estado.labirinto[estado.linha][estado.coluna]

        return estado

    def solucao(self, estado):
        """Gera uma lista com a solucao de um problema a partir de um estado."""

        # Percorre toda a lista de estados ate o estado inicial
        solucao_final = []

        while estado.pai is not None:
            solucao_final.append(estado)
            estado = estado.pai

        # Inclui o estado inicial na lista
        solucao_final.append(estado)

        # Retorna a solucao
        return solucao_final.reverse()


    def funcao_objetivo(self, estado):
        """Verifica se a funcao atingiu o seu objetivo."""

        # Chegou na saída do labirinto (S)
        return estado.bloco == 'S'

    def __valida_restricoes(self, estado):
        # Verifica se atingiu uma parede
        # Se o bloco atual for diferente de ' ', 'E' ou 'S', então é uma parede
        if estado.bloco == ' ' or estado.bloco == 'E' or estado.bloco == 'S':
            return estado
        else:
            return None

    def __go_left(self, estado_pai, labirinto, acao):
        '''Move o agente para a esquerda'''

        estado = estado_pai.copy()

        # Salva a ação realizada
        estado.acao = acao

        estado.linha = estado_pai.linha - 1
        estado.coluna = estado_pai.coluna
        estado.bloco = estado.labirinto[estado.linha][estado.coluna]

        estado.pai = estado_pai

        # Verifica se o estado é valido
        return self.__valida_restricoes(estado)

    def __go_right(self, estado_pai, labirinto, acao):
        '''Move o agente para a direita'''

        estado = estado_pai.copy()

        # Salva a ação realizada
        estado.acao = acao

        estado.linha = estado_pai.linha + 1
        estado.coluna = estado_pai.coluna
        estado.bloco = labirinto[estado.linha][estado.coluna]

        estado.pai = estado_pai

        # Verifica se o estado é valido
        return self.__valida_restricoes(estado)

    def __go_up(self, estado_pai, labirinto, acao):
        '''Move o agente para a cima'''

        estado = estado_pai.copy()

        # Salva a ação realizada
        estado.acao = acao

        estado.linha = estado_pai.linha
        estado.coluna = estado_pai.coluna - 1
        estado.bloco = labirinto[estado.linha][estado.coluna]

        estado.pai = estado_pai

        # Verifica se o estado é valido
        return self.__valida_restricoes(estado)

    def __go_down(self, estado_pai, labirinto, acao):
        '''Move o agente para a baixo'''

        estado = estado_pai.copy()

        # Salva a ação realizada
        estado.acao = acao

        estado.linha = estado_pai.linha
        estado.coluna = estado_pai.coluna + 1
        estado.bloco = labirinto[estado.linha][estado.coluna]

        estado.pai = estado_pai

        # Verifica se o estado é valido
        return self.__valida_restricoes(estado)

    def funcao_sucessora(self, estado):
        """Gera os estados sucessores a partir de um estado."""

        # Ações possiveis:
        # - Mover agente para esquerda
        # - Mover agente para direita
        # - Mover agente para cima
        # - Mover agente para baixo

        sucessores = []

        a1 = self.__go_left(estado, estado.labirinto, 'LEFT')
        a2 = self.__go_right(estado, estado.labirinto, 'LEFT')
        a3 = self.__go_up(estado, estado.labirinto, 'LEFT')
        a4 = self.__go_down(estado, estado.labirinto, 'LEFT')

        # Cria uma lista apenas com os estados validos
        if a1: sucessores.append(a1)
        if a2: sucessores.append(a2)
        if a3: sucessores.append(a3)
        if a4: sucessores.append(a4)

        return sucessores
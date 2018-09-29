#!/usr/bin/env python
from pprint import pprint
from typing import List

from problema import Problema
from labirinto import Labirinto


class BuscaGulosa(object):

    def busca_gulosa(self, problema: Labirinto):
        """Agente que implementa a busca em gulosa:

            :param problema: definicao do problema
            :return: lista com os estados para chegar na solucao do problema

        """

        # Calcula distancia estimada do estado inicial até o estado final
        # Busca estados sucessores
        # Escolhe o melhor estado sucessor

        atual = problema.estado_inicial

        visitados = [problema.estado_inicial]

        while True:

            print(f'=' * 80)
            print(f'> Estado sendo avaliado:')
            print(f'{atual}')

            # 4. Verifica se achou a solucao objetivo
            if problema.funcao_objetivo(atual):
                print('Solucao encontrada.')
                return problema.solucao(atual)

            # 5. Geracao dos estados sucessores
            sucessores = problema.funcao_sucessora(atual)

            aux = atual.copy()

            # Escolhe o melhor estado dos estados sucessores gerados
            for sucessor in sucessores:
                if sucessor > atual and not visitados.__contains__(sucessor):
                    atual = sucessor.copy()

            visitados.append(atual)

            # Se não encontrou um sucessor melhor, volta para o estado pai
            if atual == aux:
                atual = atual.pai

            # print('-'*80)
            print('sucessor:')

            for x in sucessores:
                print(x)

            print(f'Escolhido: {atual}')

            print(f'> Estados sucessores: {len(sucessores)}')
#!/usr/bin/env python

from pprint import pprint
from typing import List
from problema import Problema


class BuscaEmProfundidade(object):

    _estado = Problema.estado_inicial
    
    def busca_profundidade(self, problema: Problema, estado: Problema.estado_inicial = Problema.estado_inicial):

        while True:
            print(f'> Estado sendo avaliado:')
            print(f'{estado}')
            
            if problema.funcao_objetivo(estado):
                print('\n >>>> Solucao encontrada <<<< \n')
                return problema.solucao(estado)
            
            sucessores = problema.funcao_sucessora(estado)

            for sucessor in sucessores:
                return self.busca_profundidade(problema, sucessor)

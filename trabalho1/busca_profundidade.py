#!/usr/bin/env python

from torre_hanoi import TorreHanoi


class BuscaEmProfundidade():

    def busca_profundidade(self, problema: ProblemaTorreHanoi):

        borda = [problema.estado_inicial]

        while True:

            if not borda:

                print('Falha ao encontrar solução')
                return []

            estado = borda.pop(0)

            print(estado)
            print(type(estado))

            if problema.funcao_objetivo(estado):

                print('Solução encontrada!')
                return problema.solucao(estado)

            borda.append(problema.funcao_sucessora(estado))
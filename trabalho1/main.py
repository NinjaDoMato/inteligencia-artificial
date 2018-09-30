#!/usr/bin/env python

from busca_largura import Buscalargura
from busca_profundidade import BuscaEmProfundidade
from busca_custo_uniforme import BuscaCustoUniforme
from torre_hanoi import ProblemaTorreHanoi
from problema import Problema


def main():
    # Definicao do problema da Torre de Hanoi
    problema = ProblemaTorreHanoi()

    busca = BuscaEmProfundidade()
    solucao = busca.busca_profundidade(problema)

    print(solucao)

if __name__ == '__main__':
    main()
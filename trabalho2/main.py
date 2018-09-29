#!/usr/bin/env python

from pprint import pprint
from labirinto import Labirinto
from busca_gulosa import BuscaGulosa

def main():
    # Definicao do problema do labirinto
    problema = Labirinto()

    busca = BuscaGulosa()
    solucao = busca.busca_gulosa(problema)
    pprint(solucao)


if __name__ == '__main__':
    main()

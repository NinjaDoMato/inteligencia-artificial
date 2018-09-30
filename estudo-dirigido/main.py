#!/usr/bin/env python
import copy
from random import random, randint
from problema_rainha import ProblemaRainha
from problema_raiz import ProblemaRaiz
from hill_climbing import HillClimbing
from tabu_search import TabuSearch

def main():
    # Definicao do problema
    p = ProblemaRaiz()

    #p = ProblemaRainha()

    hc = HillClimbing(max_alt=100, max_sem_alt=10)
    hc.executa(p)

    #tb = TabuSearch(max_alt=90000, max_sem_alt=10)
    #tb.executa(p)

if __name__ == '__main__':
    main()

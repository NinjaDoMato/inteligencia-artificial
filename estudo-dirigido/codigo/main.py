#!/usr/bin/env python
import copy
from random import random, randint
from problema_rainha import ProblemaRainha
from problema_mochila import ProblemaMochila
from problema_raiz import ProblemaRaiz
from hill_climbing import HillClimbing
from tabu_search import TabuSearch
from tabu_search_grasp import TabuSearchGrasp

def main():
    # Definicao do problema
    p = ProblemaRaiz()

    pm = ProblemaMochila()

    hc = HillClimbing(max_alt=1000, max_sem_alt=10)
    hc.executa(pm)

    ###tb = TabuSearch(max_alt=1000, max_sem_alt=10)
    ###tb.executa(p)

    ##tbg = TabuSearchGrasp(max_alt=1000, max_sem_alt=10)
    ##tbg.executa(p)
#
    #tbg = TabuSearchGrasp(max_alt=1000, max_sem_alt=10)
    #tbg.executa(p)

if __name__ == '__main__':
    main()

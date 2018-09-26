#!/usr/bin/env python

from problema import Problema

class TorreHanoi(Problema):

    torreA = []
    torreB = []
    torreC = []

    class Estado(object):

        def __init__(self):
            self.torreA = []
            self.torreB = []
            self.torreC = []
            self.pai = None
            self.custo = 0
            self.acao = ''

        def copy(self):
            estado = ProblemaTorreHanoi.Estado()
            estado.torreA = self.torreA.copy()
            estado.torreB = self.torreB.copy()
            estado.torreC = self.torreC.copy()

            return estado

        def __repr__(self):
            return f'{self.torreA} \n {self.torreB} \n {self.torreC}'

    @property
    def estado_inicial(self):
        estado = ProblemaTorreHanoi.Estado()
        estado.torreA = [5, 4, 3, 2, 1]
        estado.torreB = []
        estado.torreC = []
        estado.pai = None

        return estado

    def solucao(self):
        solucao_final = []

        while estado.pai is not None:
            solucao_final.append(estado)
            estado = estado.pai

        solucao_final.append(estado)

        return solucao_final.reverse()

    def funcao_objetivo(self, estado):
        return estado.torreC == [5, 4, 3, 2, 1]

    def __mover_(self, estado_pai, acao):

        estado = estado_pai.copy()
        estado.acao = acao

        tamanhoA = len(estado.torreA)
        tamanhoB = len(estado.torreB)
        tamanhoC = len(estado.torreC)

        if acao == 'AB' and (tamanhoB == 0 or (estado.torreA[tamanhoA - 1] < estado.torreB[tamanhoB - 1])):
            estado.torreB.append(estado.torreA.pop(-1))

        elif acao == 'AC' and (tamanhoC == 0 or (estado.trreA[tamanhoA - 1] < estado.torreC[tamanhoC - 1])):
            estado.torreC.append(estado.torreA.pop(-1))

        elif acao == 'BA' and (tamanhoA == 0 or (estado.torreB[tamanhoB - 1] < estado.torreA[tamanhoA - 1])):
            estado.torreA.append(estado.torreB.pop(-1))

        elif acao == 'BC' and (tamanhoC == 0 or (estado.torreB[tamanhoB - 1] < estado.torreC[tamanhoC - 1])):
            estado.torreC.append(estado.torreB.pop(-1))

        elif acao == 'CA' and (tamanhoA == 0 or (estado.torreC[tamanhoC - 1] < estado.torreA[tamanhoA - 1])):
            estado.torreA.append(estado.torreC.pop(-1))

        elif acao == 'CB' and (tamanhoB == 0 or (estado.torreC[tamanhoC - 1] < estado.torreB[tamanhoB - 1])):
            estado.torreB.append(estado.torreC.pop(-1))

        else:
            return None

        estado.pai = estado_pai
        return estado

    def __valida_restricoes(self, estado):
        print(estado)
        print(estado.torreA)
        print(estado.torreB)
        print(estado.torreC)

    def funcao_sucessora(self, estado):
        sucessores = []

        ac1 = self.__mover(estado, 'AB')
        ac2 = self.__mover(estado, 'AC')
        ac3 = self.__mover(estado, 'BA')
        ac4 = self.__mover(estado, 'BC')
        ac5 = self.__mover(estado, 'CA')
        ac6 = self.__mover(estado, 'CB')

        if ac1:
            sucessores.append(a1)
        if ac2:
            sucessores.append(a2)
        if ac3:
            sucessores.append(a3)
        if ac4:
            sucessores.append(a4)
        if ac5:
            sucessores.append(a5)
        if ac6:
            sucessores.append(a6)

        return sucessores

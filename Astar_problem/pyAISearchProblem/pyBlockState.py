import math
import copy
import numpy as np

from pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearchProblem.pyState import AISearchState

'''
Abstrae el estado del problema
'''

class BlockState(AISearchState):
    # definición del entorno del problema: tablero, objetivo y lista objetivo
    def __init__(self, goal):
        self.tablero = [[],[],[]]
        self.goal = goal
        self.listaGoal = self.toList(goal)

    # getters y setters pilas
    def setCubosP0(self,cubos): self.tablero[0] = cubos.copy()
    def setCubosP1(self,cubos): self.tablero[1] = cubos.copy()
    def setCubosP2(self,cubos): self.tablero[2] = cubos.copy()

    def getCubosP0(self): return self.tablero[0]
    def getCubosP1(self): return self.tablero[1]
    def getCubosP2(self): return self.tablero[2]


    # mover cubo de origen a destino
    def changeP0(self,destino): 
        self.tablero[destino].append(self.tablero[0].pop())

    def changeP1(self,destino): 
        self.tablero[destino].append(self.tablero[1].pop())

    def changeP2(self,destino): 
        self.tablero[destino].append(self.tablero[2].pop())
        

    # desapila y convierte en lista
    # si el origen es: [['C'], ['B'], ['A']] la salida es: ['T','C','T','B','T','A']
    def toList(self, tablero):
        miLista = []
        for pila in tablero:
            if len(pila)>0:                
                for i in range(0, len(pila)):
                    if(i==0):
                        miListaAux=[]
                        miListaAux.append('T')              # T: tablero
                        miListaAux.append(pila[i])
                        miLista.append(miListaAux)
                    if(i>0):
                        miListaAux=[]
                        miListaAux.append(pila[i-1])
                        miListaAux.append(pila[i])
                        miLista.append(miListaAux)
        return miLista


    # comprobación si la pila está vacía
    # si la pila está vacía no puede hacer ninguna acción
    def notEmpty(self,pila):
        if pila == 0:
            return len(self.tablero[0]) != 0
        if pila == 1:
            return len(self.tablero[1]) != 0
        if pila == 2:
            return len(self.tablero[2]) != 0        


    # devolver tablero
    def returnSol(self):
        return self.tablero


    # cálculo heurística
    def getH(self): 
        contadorResultado = 0
        listaEstado = self.toList(self.tablero)

        i = 0
        while (i < len(self.listaGoal)):
            if(listaEstado[i] not in self.listaGoal):
                contadorResultado+=1
            i = i+1
                
        return contadorResultado
        

    # comprobar si dos estados son iguales
    def __eq__(self,s):
        if len(self.getCubosP0())==len(s.getCubosP0()) and len(self.getCubosP1())==len(s.getCubosP1()) and len(self.getCubosP2())==len(s.getCubosP2()):
            for i in range(0,len(self.getCubosP0())):
                if(self.getCubosP0()[i]!=s.getCubosP0()[i]):
                    return False
            for i in range(0,len(self.getCubosP1())):
                if(self.getCubosP1()[i]!=s.getCubosP1()[i]):
                    return False
            for i in range(0,len(self.getCubosP2())):
                if(self.getCubosP2()[i]!=s.getCubosP2()[i]):
                    return False
            return True    
        else:
            return False
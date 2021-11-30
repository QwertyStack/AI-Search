import math
import copy
import numpy as np

from pyAISearchProblem.pyProblem import AISearchProblem
from pyAISearchProblem.pyState import AISearchState
from pyAISearchProblem.pyBlockState import BlockState

'''
Modela el problema sobre el que queremos realizar la búsqueda
'''

class BlockProblem(AISearchProblem):
    # definición de la situación inicial de bloques y sus acciones
    def __init__(self, origin, target):      
        self.origin=origin    
        self.target=target
        self.state=BlockState(self.target) 
        self.state.setCubosP0(self.origin[0])
        self.state.setCubosP1(self.origin[1])
        self.state.setCubosP2(self.origin[2])        
        self.actions=["P0P1","P0P2","P1P0","P1P2", "P2P0", "P2P1"]


    # devuelve el estado
    def getStateInit(self):
        return self.state
    

    # comprobar si se puede llevar a cabo una acción
    def canTakeAction(self,a,state):
        if a == "P0P1" or a == "P0P2":
            if state.notEmpty(0):                   # no debe estar vacía la pila de origen, en este caso la 0
                return True

        if a == "P1P0" or a == "P1P2":
            if state.notEmpty(1):
                return True

        if a == "P2P0" or a == "P2P1":
            if state.notEmpty(2):
                return True

        return False


    # realizar acción, mover de una pila origen a otra destino 
    def takeAction(self,a,state):
        if a == "P0P1":
            if state.notEmpty(0):                           # comprobar si se puede realizar la acción       
                newState=copy.deepcopy(state)               # nuevo estado en el que se moverá un cubo 
                newState.changeP0(1)                        # mover cubo
                return newState                             # devolver el nuevo estado
            else:
                return False

        if a == "P0P2":
            if state.notEmpty(0):
                newState=copy.deepcopy(state)
                newState.changeP0(2)
                return newState
            else:
                return False

        if a == "P1P0":
            if state.notEmpty(1):
                newState=copy.deepcopy(state)
                newState.changeP1(0)
                return newState
            else:
                return False

        if a == "P1P2":
            if state.notEmpty(1):
                newState=copy.deepcopy(state)
                newState.changeP1(2)
                return newState
            else:
                return False

        if a == "P2P0":
            if state.notEmpty(2):
                newState=copy.deepcopy(state)
                newState.changeP2(0)
                return newState
            else:
                return False

        if a == "P2P1":
            if state.notEmpty(2):
                newState=copy.deepcopy(state)
                newState.changeP2(1)
                return newState
            else:
                return False

        raise RuntimeError("I can't take action in takeAction()")


    # expansión de nodo
    def sucessors(self,state):
        print("Nodo expandido: ", state.returnSol())
        sucessors = []
        for a in self.actions:                                       # recorrer todas las acciones que se pueden hacer
            if self.canTakeAction(a,state):                          # comporbar si se puede tomar la acción
                newState=self.takeAction(a,state)                    # realizar la acción             
                sucessors.append((a,newState,1))                     # añadir el nuevo estado a los hijos (acción, nuevoEstado, coste del camino = 1)
                print("     Hijo: ", newState.returnSol())           # impresión para árbol de búsqueda
        return sucessors


    # comprobación del estado actual para ver si se ha llegado al objetivo
    def isGoal(self,state):
        if ( len(self.target[0])==len(state.getCubosP0()) ) and ( len(self.target[1])==len(state.getCubosP1()) ) and ( len(self.target[2])==len(state.getCubosP2()) ):
            for i in range(0,len(self.target[0])):
                if(self.target[0][i]!=state.getCubosP0()[i]):
                    return False
            for i in range(0,len(self.target[1])):
                if(self.target[1][i]!=state.getCubosP1()[i]):
                    return False
            for i in range(0,len(self.target[2])):
                if(self.target[2][i]!=state.getCubosP2()[i]):
                    return False
            return True    
        else:
            return False
  
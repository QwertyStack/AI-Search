import copy
from pyAISearchProblem.pyProblem import AISearchProblem


# Abstrae el estado del problema
class AIFichaState(object):
    # constructor de la clase: tablero, profundidadm jugador y profundidad máxima
    def __init__(self,startPlayer):
        self.board=["", "", "", "", ""]
        self.depth=0
        self.player=startPlayer                 # puede ser tanto A como B, pero por defecto es A
        self.profundidad = 1                    # profundidad máxima, inicialmente va a ser 1
    
    
    # mover ficha
    def setPiece(self,loc,ficha):
        for i in range(0, len(self.board)):     # recorrer el tablero
            if self.board[i] == ficha:
                self.board[i] = ""              # eliminar ficha de la posición antigua
        self.board[loc] = ficha                 # agregar ficha en la nueva posición
    

    # poner un jugador en el tablero
    def setPlayer(self,loc):
        self.setPiece(loc,self.player)      
    

    # mover jugador --> nuevo nodo
    def movePlayer(self,pos):
        newState = copy.deepcopy(self)          # nuevo estado sobre el que realizar los cambios
        newState.setPlayer(pos)
        newState.incDepth()
        newState.changePlayer()
        return newState
 

    # comprobar posiciones libres tablero donde mover ficha
    # (para un tablero de 5 posiciones siempre serán 3)
    def freeLocations(self):
        holes=[]                                        # lista con las posiciones disponibles
        ficha = self.player
        indexFicha= self.board.index(ficha) 

        # ficha en primera posicion
        if(indexFicha == 0):
            if(self.board[1]==""):                      # comprobar que la posición es vacía
                holes.append(1)                         # agregar la posición a la lista
            else:
                holes.append(2)                         # agregar la posición de salto, hay una ficha en la posición adyacente

        # ficha en última posicion        
        if(indexFicha == 4):
            if(self.board[3]==""):
                holes.append(3)
            else:
                holes.append(2)

        # ficha entre medias       
        if(indexFicha>0 and indexFicha < 4):
            # izquierda
            if(self.board[indexFicha-1]==""):
                holes.append(indexFicha-1)
            else:
                if(indexFicha-2 >= 0):
                    holes.append(indexFicha-2)          # agregar la posición de salto
            # derecha
            if(self.board[indexFicha+1]==""):
                holes.append(indexFicha+1)
            else:
                if(indexFicha+2<=4):
                    holes.append(indexFicha+2)          # agregar la posición de salto

        return holes
    

    # controlar la profundidad del árbol   
    def levelFull(self):
        return self.depth == self.profundidad


    # definir la profundidad máxima del árbol
    def setProfundidad(self,pf):
        self.profundidad=pf
    
    
    # cambio de jugador
    def changePlayer(self):
        if self.player=="A": 
            self.player="B"
            return
        self.player="A"
    
    
    # aumentar profundidad
    def incDepth(self):
        self.depth+=1
    
    
    # comprobar si se ha terminado
    def isTerminal(self):
        return self.win("A") or self.win("B") or self.levelFull()
    

    # cálculo distancia
    def win(self,ficha):
        if ficha == "B":
            return self.board[0] == ficha                   # B gana si está en la posición 0
        if ficha == "A":
            return self.board[len(self.board)-1] == ficha   # A gana si está en la posición 4


    # cálculo d(min) - d(max)
    def distancia(self):
        indexA = self.board.index("A")
        indexB = self.board.index("B")
        
        return indexB - ((len(self.board)-1) - indexA)


    # función de evaluación
    def utility(self):
        if self.win("A"): 
            return 10e100                                   # revolver +inf
        
        if self.win("B"): 
            return -10e100                                  # devolver -inf

        if not self.win("A") and not self.win("B"):            
            return  self.distancia()                        # devolver cálculo d(min) - d(max)
    
    
    # imprimir con formato qué ocurre en cada estado (profundidad, jugador, e(s))
    def __str__(self):
        s="["
        for i in range(0 ,len(self.board)):
            if(self.board[i] != ""):
                s+=self.board[i]
                if(i!=len(self.board)-1):
                    s+=","
            else:
                if(i==len(self.board)-1):
                    s+="_"
                else:
                    s+="_,"
        s+="]"
        s+=" --- Profundidad: "+str(self.depth)+" --- Jugador que debe mover: "+self.player+" --- e de este estado: "+ str(self.utility())
        return s



# ----------------------------------------------------------------------------------------------------------------------------------


# Modela el problema sobre el que queremos realizar la búsqueda
class AIFichaProblem(AISearchProblem):
    # constructor: inicializa el estado, por defecto comienza la ficha A
    def __init__(self, startPlayer="A"):
        self.currentState=AIFichaState(startPlayer)
    
    
    # obtener los sucesores del nodo
    def expand(self,state):
        successors=[]
        for pos in state.freeLocations():
            newState=state.movePlayer(pos)
            successors.append(newState)
            print(newState)                         # impresión del hijo
        return successors
        
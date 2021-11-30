from pyAIFichaProblem import AIFichaProblem,AIFichaState
from pyAIMinMax import AIMinMax


# contextualizar el problema
def inicio(s):
    print("Dime en qué posiciones colocar A y B:")

    jugador1 = -1
    while jugador1 <0 or jugador1 >4:
        jugador1 = int(input())
    
    jugador2 = -1
    while jugador2 == jugador1 or jugador2 <0 or jugador2 >4:
        jugador2 = int(input())

    s.setPlayer(jugador1)
    s.changePlayer()
    s.setPlayer(jugador2)
    s.changePlayer()
    

if __name__ == '__main__':
    p = AIFichaProblem()                                # crear el problema
    mm = AIMinMax(p)                                    # crear el problema con las caraterísticas de MinMax   
    s = AIFichaState("A")                               # creación del estado inicial, el jugador que comenzará será A por defecto
    
    print("Si quiere maximizar escriba: max, si quiere minimizar escriba: min ")
    maxmin = str(input()) 
    inicio(s)
    print("Indique la profundidad máxima ")
    profundidad = int(input())
    s.setProfundidad(profundidad)

    # si se va a comenzar minimizando o maximizando comenzará la ficha B o A respectivamente
    if(maxmin == "max" or maxmin== "MAX"):
        print(s)                                        # imprimir el estado original
        valor = mm.maxValue(s)        
    if(maxmin == "min" or maxmin== "MIN"):
        s.changePlayer()                                # cambiar el jugador, ya que debe comenzar B
        print(s)
        valor = mm.minValue(s)
        
    print("valor resultado: ", valor)                   # función de evaluación

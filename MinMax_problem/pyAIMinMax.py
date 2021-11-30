from pyAISearchSolver import AISearchSolver

class AIMinMax(AISearchSolver):
    def __init__(self, problem):
        super().__init__(problem)


    def maxValue(self,state):
        maxUpToNow=-10e100                                      # valor máximo hasta ahora: -inf
        if state.isTerminal():                                  # comprobar si se ha terminado
            return state.utility()                              # devolver la función de evaluación
        succesors=self.problem.expand(state)                    # obtener los hijos
        for s in succesors:                                     # recorrer los hijos
            maxUpToNow=max(maxUpToNow,self.minValue(s))         # por cada hijo comparar con el valor máximo hasta ahora
        return maxUpToNow                                       # devolver el valor máximo

        
    def minValue(self,state):
        minUpToNow= 10e100                                      # valor mínimo hasta ahora: +inf
        if state.isTerminal():
            return state.utility()
        succesors=self.problem.expand(state)
        for s in succesors:
            minUpToNow=min(minUpToNow,self.maxValue(s))         # por cada hijo comparar con el valor mínimo hasta ahora
        return minUpToNow                                       # devolver el valor mínimo

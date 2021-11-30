from pyAISearchProblem.pyBlockProblem import BlockProblem
from pyAISearchProblem.pyBlockState import BlockState
from busquedaNormal.pyAISearchSolverGraph import AISearchSolverGraph


if __name__ == '__main__':

    # BlockProblem(estado original, estado solución)
    pp=BlockProblem([[], ['A', 'C','B'], []], [['C','B','A'],[],[]])
    sg=AISearchSolverGraph(pp)
    found=sg.search()
    
    if not found:
        print("Solution not found")
    else:
        print("\n---- SOLUCION: ----")
        listaResultado=[]                           # almacenar la salida para poner el formato deseado
        cn=sg.getCurrentNode()
        
        while cn.getFather():
            listaResultado.insert(0,cn)
            cn=cn.getFather()
        
        listaResultado.insert(0,cn)

        # mostrar nodos solución
        for i in listaResultado:
            print("Nodo: ", i.getState().returnSol(), "  ->  Profundidad: ", i.getCostPath(),"  ->  f* = g(",i.getDepth(),") + h*(",i.getState().getH(),") =", i.getF(), "  ->  Accion: ", i.getAction())

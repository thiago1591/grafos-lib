from classes.grafo_lib import *

lib = GrafoLib({
    "tipo_representacao": 'matriz',
    "caminho_grafo_arq": "inputs/grafo_0.txt"
})

lib.grafo.print_graph()

# lib.BFS(0)
# lib.DFS(0)
# lib.encontrarComponentesConexos()
# lib.encontrarDistanciaECaminhoMinimo()
# lib.encontrarMST()
# lib.encontrarDistanciaMedia()
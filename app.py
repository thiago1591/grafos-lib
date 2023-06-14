from classes.grafo_lib import *

lib = GrafoLib({
    "tipo_representacao": 'matriz',
    "caminho_grafo_arq": "inputs/grafo_0.txt"
})
lib.executarEncontrarDistanciaECaminhoMinimo2Vertices(1, 4)
#lib.grafo.print_graph()

# lib.BFS(0)
# lib.DFS(0)
# lib.encontrarComponentesConexos()
# lib.encontrarDistanciaECaminhoMinimo()
# lib.encontrarMST()
# lib.encontrarDistanciaMedia()
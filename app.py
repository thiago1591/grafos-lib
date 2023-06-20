from classes.grafo_lib import *

lib = GrafoLib({
    "tipo_representacao": 'matriz',
    "caminho_grafo_arq": "inputs/grafo_5.txt"
})
# lib.executarEncontrarDistanciaUmVerticeParaTodos(1)
# lib.grafo.print_graph()

# lib.executarBFS(1)
lib.executarDFS(1)
# lib.executarEncontrarComponentesConexos()
# lib.executarEcontrarDistanciaMedia()

# lib.BFS(0)
# lib.DFS(0)
# lib.encontrarComponentesConexos()
# lib.encontrarDistanciaECaminhoMinimo()
# lib.encontrarMST()
# lib.encontrarDistanciaMedia()

lib.executarGerarInformacoes()
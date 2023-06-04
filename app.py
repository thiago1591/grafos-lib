from classes.grafo_lib import *

lib = GrafoLib({
    "tipo_representacao": 'lista',
    "caminho_grafo_arq": "inputs/grafo_1.txt"
})

lib.BFS(0)
lib.DFS(0)
lib.encontrarComponentesConexos()
lib.encontrarDistanciaECaminhoMinimo()
lib.encontrarMST()
lib.encontrarDistanciaMedia()
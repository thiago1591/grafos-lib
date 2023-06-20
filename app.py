from classes.grafo_lib import *
import sys
sys.setrecursionlimit(1000000)

lib = GrafoLib({
    "tipo_representacao": 'lista',
    "caminho_grafo_arq": "inputs/grafo_5.txt"
})

#lib.executarMST()
#lib.executarBFS(22)
#lib.executarDFS(22)
#lib.encontrarComponentesConexos()
#lib.executarEncontrarComponentesConexos()
lib.executarEcontrarDistanciaMedia()
#lib.executarEncontrarDistancia2Vertices(1, 10000)
#lib.executarEncontrarDistanciaUmVerticeParaTodos(22)
#lib.calcularDistribuiçãoEmpirica()
#lib.executarMST()
lib.executarGerarInformacoes()

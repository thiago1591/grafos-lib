import sys

from classes.grafo_lista_adj import GrafoListaAdj
from classes.grafo_matriz_adj import GrafoMatrizAdj
from utils.obter_arestas import obterArestas
from algoritmos.BFS import BFS
from algoritmos.DFS import DFS

class GrafoLib:
    def __init__(self, config):
        self.tipo_representacao = config['tipo_representacao']
        self.caminho_arq = config['caminho_grafo_arq']
        self.instanciarGrafo()

    def instanciarGrafo(self):
        arestas = obterArestas(self.caminho_arq)
        if(self.tipo_representacao == "lista"):
            self.grafo = GrafoListaAdj(arestas)
        elif(self.tipo_representacao == "matriz"):
            self.grafo = GrafoMatrizAdj(arestas)
        else:
            print('Escolha um valor válido')
            sys.exit()

    def executarBFS(self, initialVertice):
        print('executando BFS')
        ...
    
    def executarDFS(self, initialVertice):
        print('executando DFS')
        ...

    def executarEncontrarComponentesConexos(self):
        print('executando encontrarComponentesConexos')
        ...

    def executarEcontrarDistanciaMedia(self):
        print('executando encontrarDistanciaMedia')
        ...
    
    def executarEncontrarDistanciaECaminhoMinimo2Vertices(self, v1, v2):
        distance, path = self.grafo.dijkstra2Vertices(self.grafo, v1, v2)

        print(f"A distância entre o vértice {v1} e o vértice {v2} é: {distance}")
        print(f"O caminho mais curto é: {path}")
    
    def executarEncontrarMST(self):
        print('executando encontrarMST')
        ...

    def executarPrintGraph(self):
        print(self.grafo)
    

        
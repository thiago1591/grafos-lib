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
        self.criarGrafo()

    def criarGrafo(self):
        arestas = obterArestas(self.caminho_arq)
        if(self.tipo_representacao == "lista"):
            self.grafo = GrafoListaAdj(arestas)
        elif(self.tipo_representacao == "matriz"):
            self.grafo = GrafoMatrizAdj(arestas)
        else:
            print('Escolha um valor válido')
            sys.exit()

    def BFS(self, initialVertice):
        print('executando BFS')
        ...
    
    def DFS(self, initialVertice):
        print('executando DFS')
        ...

    def encontrarComponentesConexos(self):
        print('executando encontrarComponentesConexos')
        ...

    def encontrarDistanciaECaminhoMinimo(self):
        print('executando encontrarDistanciaECaminhoMinimo')
        ...
    
    def encontrarMST(self):
        print('executando encontrarMST')
        ...

    def encontrarDistanciaMedia(self):
        print('executando encontrarDistanciaMedia')
        ...
    
    

        
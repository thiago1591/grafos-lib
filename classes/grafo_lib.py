import sys

from classes.grafo_lista_adj import GrafoListaAdj
from classes.grafo_matriz_adj import GrafoMatrizAdj
from utils.obter_arestas import obterArestas

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
            print('Representação inválida. Escolha entre "lista" e "matriz"')
            sys.exit()

    def executarBFS(self, initialVertice):
        visited = self.grafo.BFS_tree(1)

        for key, value in visited.items():
            print("Vértice:", key, "Nível:", value)
    
    def executarDFS(self, initialVertice):
        print('executando DFS')
        ...

    def executarEncontrarComponentesConexos(self):
        print('executando encontrarComponentesConexos')
        ...

    def executarEcontrarDistanciaMedia(self):
        print('executando encontrarDistanciaMedia')
        ...
    
    def executarEncontrarDistancia2Vertices(self, v1, v2):
        distancia, caminho = self.grafo.dijkstra2Vertices(v1, v2)

        print(f"A distância entre o vértice {v1} e o vértice {v2} é: {distancia}")
        print(f"O caminho mais curto é: {caminho}")
    
    def executarEncontrarDistanciaUmVerticeParaTodos(self, origem):
        distancias, caminhos = self.grafo.dijkstraTodosVertices(origem)

        for vertice in range(len(self.grafo.adj)):
            distancia = distancias[vertice]
            caminho = caminhos[vertice]
            print(f"Distância para o vértice {vertice}: {distancia}")
            print(f"Caminho para o vértice {vertice}: {caminho}")
    
    def executarEncontrarMST(self):
        print('executando encontrarMST')
        ...

    def executarPrintGraph(self):
        print(self.grafo.adj)
    

        
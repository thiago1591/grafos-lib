import sys

from classes.grafo_lista_adj import GrafoListaAdj
from classes.grafo_matriz_adj import GrafoMatrizAdj
from utils.obter_arestas import obterArestas
import itertools

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

    def executarBFS(self, initialNode):
        visited = self.grafo.BFS_tree(initialNode)

        for key, value in visited.items():
            print("Vértice:", key, "Nível:", value)
    
    def executarDFS(self):
        visited = {}
        level = 0

        for vertex in self.grafo.adj:
            if vertex not in visited:
                self.grafo.DFS_tree(vertex, level, visited)

        for key, value in visited.items():
            print("Vértice:", key, "Nível:", value)

    def encontrarComponentesConexos(self):
        visited = {}
        components = []
        level = 0

        for vertex in self.grafo.adj:
            if vertex not in visited:
                component = []
                self.grafo.DFS_tree(vertex, level, visited, component)
                components.append(component)

        components.sort(key=len, reverse=True)

        return components
    
    def executarEncontrarComponentesConexos(self):
        components = self.encontrarComponentesConexos()

        print("Número de componentes conexos:", len(components))

        for i, component in enumerate(components, 1):
            print("Componente", i, ":", component, "---> Tamanho: ", len(component))

    def executarEcontrarDistanciaMedia(self):
        components = self.encontrarComponentesConexos()
        distances = []

        for component in components:
            verticesCombination = list(itertools.combinations(component, 2))

            for vertices in verticesCombination:
                distance, _ = self.grafo.encontrarDistanciaECaminhoMinimo2Vertices(vertices[0], vertices[1])
                distances.append(distance)

        mean = sum(distances) / len(distances)
        print("média das distâncias: {:.2f}".format(mean))

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
    

        
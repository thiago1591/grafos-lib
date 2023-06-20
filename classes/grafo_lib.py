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
        arestas, n_arestas = obterArestas(self.caminho_arq)

        self.n_arestas = n_arestas

        if(self.tipo_representacao == "lista"):
            self.grafo = GrafoListaAdj(arestas)
        elif(self.tipo_representacao == "matriz"):
            self.grafo = GrafoMatrizAdj(arestas)
        else:
            print('Representação inválida. Escolha entre "lista" e "matriz"')
            sys.exit()

    def executarBFS(self, initialNode):
        visited = self.grafo.BFS_tree(initialNode)

        if (visited == False):
            print("Vértice inicial não existe no grafo")
            return False

        output_file = open("outputs/bfs_result.txt", "w", encoding="utf-8")

        output_file.write("Árvore BFS (ordenado por ordem de acesso)\n")
        for key, value in visited.items():
            output_file.write("Vértice: " + str(key) + " Nível: " + str(value) + "\n")

        output_file.close()
    
    def executarDFS(self, initialNode):
        visited = {}
        level = 0

        self.grafo.DFS_tree(initialNode, level, visited)

        output_file = open("outputs/dfs_result.txt", "w", encoding="utf-8")

        output_file.write("Árvore DFS (ordenado por ordem de acesso)\n")
        for key, value in visited.items():
            output_file.write("Vértice: " + str(key) + " Nível: " + str(value) + "\n")

        output_file.close()

    def encontrarComponentesConexos(self):
        components = self.grafo.encontrarComponentesConexos()

        components.sort(key=len, reverse=True)

        return components
    
    def executarEncontrarComponentesConexos(self):
        components = self.encontrarComponentesConexos()

        print("Número de componentes conexos:", len(components))

        for i, component in enumerate(components, 1):
            print("Componente", i, ":", component, "---> Tamanho: ", len(component))

    def executarEcontrarDistanciaMedia(self):
        components = self.encontrarComponentesConexos()
        print(components)
        
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

    def calcularDistribuiçãoEmpirica(self):
        contagem_graus = {}
        total_vertices = len(self.grafo.graus)

        for num in range(1, max(self.grafo.graus)+1):
            contagem_graus[num] = 0

        for grau in self.grafo.graus:
            if grau in contagem_graus:
                contagem_graus[grau] += 1
            else:
                contagem_graus[grau] = 1

        distribuicao_empirica = [(grau, contagem_graus[grau] / total_vertices) for grau in contagem_graus]

        distribuicao_empirica.sort(key=lambda x: x[0])

        return distribuicao_empirica

    def executarGerarInformacoes(self):
        output_file = open("outputs/result.txt", "w", encoding="utf-8")

        output_file.write("# n = " + str(self.grafo.num_vertices) + "\n")
        output_file.write("# m = " + self.n_arestas)
        output_file.write("# d_medio = " + str(self.grafo.grau_medio) + "\n")
        
        distribuicao = self.calcularDistribuiçãoEmpirica()

        for grau, probabilidade in distribuicao:
            output_file.write(str(grau) + " " + str(probabilidade) + "\n")

        output_file.close()
        
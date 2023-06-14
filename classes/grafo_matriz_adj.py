import heapq
from classes.grafo import Grafo
from utils.checa_pesos_negativos import checaPesosNegativos
from collections import deque

class GrafoMatrizAdj(Grafo):
    def __init__(self, input_data):
        self.num_vertices = 0
        self.adj = []
        self.criar_grafo(input_data)

    def criar_grafo(self, input_data):
        for edge in input_data:
            node1, node2, weight = edge
            self.num_vertices = max(self.num_vertices, node1+1, node2+1)
        self.adj = [[0] * self.num_vertices for _ in range(self.num_vertices)]

        for edge in input_data:
            node1, node2, weight = edge
            self.adicionar_aresta(node1, node2, weight)

    def obter_vertices(self):
        return range(self.num_vertices)

    def obter_arestas(self):
        arestas = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adj[i][j] != 0:
                    arestas.append((i, j, self.adj[i][j]))
        return arestas

    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.adj[vertice1][vertice2] = peso
        self.adj[vertice2][vertice1] = peso

    def existe_aresta(self, vertice1, vertice2):
        return self.adj[vertice1][vertice2] != 0

    def encontrar_vertice(self, v):
        return self.adj[v]
    
    def print_graph(self):
        arestas = []
        for i in range(self.num_vertices):
            print(f'Adjacency list of vertex ${i} :')
            for j in range(self.num_vertices):
                if self.adj[i][j] != 0:
                    print(f'-> {j} (weight: {self.adj[i][j]})')
        return arestas

    def checaGrafoEPonderado(self):
        for linha in self.adj:
            for peso in linha:
                if peso > 1:
                    return True
        return False
    
    def dijkstra2Vertices(self, v1, v2):
        pesos_negativos = checaPesosNegativos(self.adj)

        if(pesos_negativos): return

        num_vertices = len(self.graph)
        distances = [float('inf')] * num_vertices
        distances[v1] = 0
        paths = [[] for _ in range(num_vertices)]
        paths[v1] = [v1]
        queue = [(0, v1)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in enumerate(self.graph[current_vertex]):
                if weight == 0:
                    continue

                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    heapq.heappush(queue, (distance, neighbor))

        return distances[v2], paths[v2]
    
    def BFS(grafo, v1, v2):
        num_vertices = len(grafo)
        visited = [False] * num_vertices
        distances = [float('inf')] * num_vertices
        paths = [[] for _ in range(num_vertices)]
        queue = deque()

        visited[v1] = True
        distances[v1] = 0
        queue.append(v1)

        while queue:
            current_vertex = queue.popleft()

            for neighbor in range(num_vertices):
                if grafo[current_vertex][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    distances[neighbor] = distances[current_vertex] + 1
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    queue.append(neighbor)

        return distances[v2], paths[v2]

    def encontrarDistanciaECaminhoMinimo2Vertices(self):
        grafoEPonderado = self.checaGrafoEPonderado()
        if(grafoEPonderado is False):
            return self.BFS()
        else:
            return self.dijkstra2Vertices()
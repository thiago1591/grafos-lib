import heapq
from classes.grafo import Grafo
from collections import deque

class GrafoMatrizAdj(Grafo):
    def __init__(self, arestas):
        self.num_vertices = 0
        self.adj = []
        self.criar_grafo(arestas)
        self.graus = self.obter_graus()
        self.grau_medio = self.obter_grau_medio()

    def criar_grafo(self, arestas):
        self.ponderado = len(arestas[0]) > 2
        if(self.ponderado):
            for edge in arestas:
                node1, node2, weight = edge
                self.num_vertices = max(self.num_vertices, node1+1, node2+1)
            self.adj = [[0] * self.num_vertices for _ in range(self.num_vertices)]

            for edge in arestas:
                node1, node2, weight = edge

                self.adicionar_aresta(node1, node2, weight)
        else:
            for edge in arestas:
                node1, node2 = edge
                self.num_vertices = max(self.num_vertices, node1+1, node2+1)
            self.adj = [[0] * self.num_vertices for _ in range(self.num_vertices)]

            for edge in arestas:
                node1, node2 = edge

                self.adicionar_aresta(node1, node2, 1)

    def obter_vertices(self):
        return range(self.num_vertices)

    def obter_graus(self):
        graus = []

        for i in range(len(self.adj)):
            grau = sum(1 for j in self.adj[i] if j != 0)
            graus.append(grau)
        
        return graus

    def obter_grau_medio(self):
        graus = self.graus
        grau_medio = sum(graus) / len(graus)
        return grau_medio

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
    
    def checa_pesos_negativos(self):
        for row in self.adj:
            for weight in row:
                if weight < 0:
                    return False
    
    def dijkstra2Vertices(self, v1, v2):
        pesos_negativos = self.checa_pesos_negativos()

        if(pesos_negativos): return

        num_vertices = len(self.adj)
        distances = [float('inf')] * num_vertices
        distances[v1] = 0
        paths = [[] for _ in range(num_vertices)]
        paths[v1] = [v1]
        queue = [(0, v1)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in enumerate(self.adj[current_vertex]):
                if weight == 0:
                    continue

                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    heapq.heappush(queue, (distance, neighbor))

        return distances[v2], paths[v2]
    
    def dijkstraTodosVertices(self, origem):
        num_vertices = len(self.adj)
        distancias = [float('inf')] * num_vertices
        caminhos = [[] for _ in range(num_vertices)]
        distancias[origem] = 0
        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho in range(num_vertices):
                peso = self.adj[vertice_atual][vizinho]

                if peso > 0:
                    nova_distancia = distancias[vertice_atual] + peso

                    if nova_distancia < distancias[vizinho]:
                        distancias[vizinho] = nova_distancia
                        caminhos[vizinho] = caminhos[vertice_atual] + [vizinho]
                        heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        return distancias, caminhos
    
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

    def BFS_tree(self, initialNode):
        visited = {}
        queue = []

        visited[initialNode] = 0
        queue.append(initialNode)

        while queue:
            s = queue.pop(0)

            for neighbour in range(len(self.adj[s])):
                if self.adj[s][neighbour] != 0 and neighbour not in visited:
                    visited[neighbour] = visited[s] + 1  # Definir o nível do vizinho
                    queue.append(neighbour)

        return visited

    def DFS_tree(self, node, level, visited, component = []):
        visited[node] = level
        component.append(node)

        for neighbour in range(len(self.adj[node])):
            if self.adj[node][neighbour] != 0 and neighbour not in visited:
                self.DFS_tree(neighbour, level+1, visited)

    def encontrarDistanciaECaminhoMinimo2Vertices(self, v1, v2):
        if(self.ponderado is False):
            return self.BFS(self.adj, v1, v2)
        else:
            return self.dijkstra2Vertices(v1, v2)
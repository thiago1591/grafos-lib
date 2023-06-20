from collections import defaultdict, deque
from classes.grafo import Grafo
import heapq

class GrafoListaAdj(Grafo):
    def __init__(self, arestas):
        self.adj = defaultdict(set)
        self.criar_grafo(arestas)
        self.num_vertices = len(self.obter_vertices())
        self.graus = self.obter_graus()
        self.grau_medio = self.obter_grau_medio()

    def criar_grafo(self, arestas):
        self.ponderado = len(arestas[0]) > 2

        if(self.ponderado):
            for u, v, p in arestas:
                self.adj[u].add((v,p))
                self.adj[v].add((u,p))
        else:
            for u, v in arestas:
                self.adj[u].add((v,1))
                self.adj[v].add((u,1))

    def obter_vertices(self):
        return list(self.adj.keys())

    def obter_graus(self):
        graus = []

        vertices_ordenado = sorted(self.adj.items())

        for _, vertice_adj in vertices_ordenado:
            grau = len(vertice_adj)
            graus.append(grau)
            
        return graus

    def obter_grau_medio(self):
        graus = self.graus
        grau_medio = sum(graus) / len(graus)
        return grau_medio

    def obter_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]
        
    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]

    def encontrar_vertice(self, v):
        return self.adj[v]

    def print_graph(self):
        for vertex in self.adj:
            print(f"Adjacency list of vertex {vertex}:")
            for neighbor, weight in self.adj[vertex]:
                print(f" -> {neighbor} (weight: {weight})")
    
    def checa_pesos_negativos(self):
        for vertice, arestas in self.adj.items():
            for vizinho, peso in arestas:
                if peso < 0:
                    return True
        return False
    
    def dijkstra2Vertices(self, v1, v2):
        pesos_negativos = self.checa_pesos_negativos()

        if(pesos_negativos): return

        distances = {vertex: float('inf') for vertex in self.adj}
        distances[v1] = 0
        paths = {vertex: [] for vertex in self.adj}
        paths[v1] = [v1]
        queue = [(0, v1)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.adj[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    heapq.heappush(queue, (distance, neighbor))

        return distances[v2], paths[v2]
    
    def dijkstraTodosVertices(self, origem):
        distancias = defaultdict(lambda: float('inf'))
        caminhos = defaultdict(list)
        distancias[origem] = 0
        fila_prioridade = [(0, origem)]

        while fila_prioridade:
            distancia_atual, vertice_atual = heapq.heappop(fila_prioridade)

            if distancia_atual > distancias[vertice_atual]:
                continue

            for vizinho, peso in self.adj[vertice_atual]:
                nova_distancia = distancias[vertice_atual] + peso

                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
                    caminhos[vizinho] = caminhos[vertice_atual] + [vizinho]
                    heapq.heappush(fila_prioridade, (nova_distancia, vizinho))

        return distancias, caminhos

    def BFS(self, v1, v2):
        visited = set()
        distances = {}
        paths = {}

        queue = deque()
        queue.append(v1)
        visited.add(v1)
        distances[v1] = 0
        paths[v1] = [v1]

        while queue:
            current_vertex = queue.popleft()

            if current_vertex == v2:
                break

            for neighbor in self.adj[current_vertex]:
                if neighbor not in visited:
                    print(neighbor)
                    visited.add(neighbor)
                    queue.append(neighbor)
                    distances[neighbor] = distances[current_vertex] + 1
                    paths[neighbor] = paths[current_vertex] + [neighbor]

        if v2 not in distances:
            return float('inf'), []

        return distances[v2], paths[v2]
    
    def BFS_tree(self, initialNode):
        visited = {}
        queue = []

        visited[initialNode] = 0
        queue.append(initialNode)

        while queue:
            s = queue.pop(0)

            for neighbour, _ in self.adj[s]:
                if neighbour not in visited:
                    visited[neighbour] = visited[s] + 1
                    queue.append(neighbour)
        
        return visited

    def DFS_tree(self, node, level, visited, component = []):
        visited[node] = level
        component.append(node)

        for neighbour, _ in self.adj[node]:
            if neighbour not in visited:
                self.DFS_tree(neighbour, level+1, visited, component)

    def encontrarDistanciaECaminhoMinimo2Vertices(self, v1, v2):
        if(self.ponderado is False):
            return self.BFS(self.adj, v1, v2)
        else:
            return self.dijkstra2Vertices(v1, v2)
        
    def prim(self):
        mst = defaultdict(set)
        
        start_vertex = list(self.adj.keys())[0]
        
        visited = set([start_vertex])
        
        edges = [
            (weight, start_vertex, neighbor)
            for neighbor, weight in self.adj[start_vertex]
        ]
        heapq.heapify(edges)
        
        while edges:
            weight, u, v = heapq.heappop(edges)
            
            if v not in visited:
                mst[u].add((v, weight))
                mst[v].add((u, weight))
                
                visited.add(v)
                
                for neighbor, weight in self.adj[v]:
                    if neighbor not in visited:
                        heapq.heappush(edges, (weight, v, neighbor))
        
        return dict(mst)
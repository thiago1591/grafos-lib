from collections import defaultdict, deque
from classes.grafo import Grafo
import heapq

class GrafoListaAdj(Grafo):
    def __init__(self, arestas):
        self.adj = defaultdict(set)
        self.criar_grafo(arestas)

    def criar_grafo(self, arestas):
        self.ponderado = len(arestas[0]) > 2

        if(self.ponderado):
            for u, v, p in arestas:
                self.adj[u].add((v,p))
                self.adj[v].add((u,p))
        else:
            for u, v in arestas:
                self.adj[u].add(p)
                self.adj[v].add(p)

    def obter_vertices(self):
        return list(self.adj.keys())

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
                    visited.add(neighbor)
                    queue.append(neighbor)
                    distances[neighbor] = distances[current_vertex] + 1
                    paths[neighbor] = paths[current_vertex] + [neighbor]

        if v2 not in distances:
            return float('inf'), []

        return distances[v2], paths[v2]
    
    def encontrarDistanciaECaminhoMinimo2Vertices(self, v1, v2):
        if(self.ponderado is False):
            return self.BFS(self.adj, v1, v2)
        else:
            return self.dijkstra2Vertices(self.adj, v1, v2)
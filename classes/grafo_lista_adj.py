from collections import defaultdict
from classes.grafo import Grafo
import heapq
from utils.checa_pesos_negativos import checaPesosNegativos

class GrafoListaAdj(Grafo):
    def __init__(self, arestas):
        self.adj = defaultdict(set)
        self.criar_grafo(arestas)

    def criar_grafo(self, arestas):
        for u, v, p in arestas:
            self.adj[u].add((v,p))
            self.adj[v].add((u,p))

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

    def checaGrafoEPonderado(self):
        for vertice, vizinhos in self.adj.items():
            for vizinho, peso in vizinhos:
                if peso is not None:
                    return True
        return False
    
    def dijkstra2Vertices(self, v1, v2):
        pesos_negativos = checaPesosNegativos(self.adj)

        if(pesos_negativos): return

        distances = {vertex: float('inf') for vertex in self.graph}
        distances[v1] = 0
        paths = {vertex: [] for vertex in self.graph}
        paths[v1] = [v1]
        queue = [(0, v1)]

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    paths[neighbor] = paths[current_vertex] + [neighbor]
                    heapq.heappush(queue, (distance, neighbor))

        return distances[v2], paths[v2]

    def BFS():
        ...
    
    def encontrarDistanciaECaminhoMinimo2Vertices(self):
        grafoEPonderado = self.checaGrafoEPonderado()
        if(grafoEPonderado is False):
            result = self.BFS()
        else:
            result = self.dijkstra2Vertices()
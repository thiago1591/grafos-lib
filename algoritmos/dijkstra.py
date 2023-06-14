import heapq

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, start, end):
        if isinstance(self.graph, list):
            return self.dijkstra_para_matriz(start, end)
        elif isinstance(self.graph, dict):
            return self.dijkstra_para_lista(start, end)
        else:
            raise ValueError("Tipo de representação de grafo não suportado")

    def dijkstra_para_matriz(self, start, end):
        num_vertices = len(self.graph)
        distances = [float('inf')] * num_vertices
        distances[start] = 0
        paths = [[] for _ in range(num_vertices)]
        paths[start] = [start]
        queue = [(0, start)]

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

        return distances[end], paths[end]

    def dijkstra_para_lista(self, start, end):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0
        paths = {vertex: [] for vertex in self.graph}
        paths[start] = [start]
        queue = [(0, start)]

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

        return distances[end], paths[end]

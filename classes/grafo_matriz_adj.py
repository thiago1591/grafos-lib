class GrafoMatrizAdj:
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
            for j in range(i + 1, self.num_vertices):
                if self.adj[i][j] != 0:
                    arestas.append((i, j))
        return arestas

    def adicionar_aresta(self, vertice1, vertice2, peso):
        self.adj[vertice1][vertice2] = peso
        self.adj[vertice2][vertice1] = peso

    def existe_aresta(self, vertice1, vertice2):
        return self.adj[vertice1][vertice2] != 0

    def encontrar_vertice(self, v):
        return self.adj[v]

class Grafo:
    def __init__(self, graph):
        self.graph = graph

    def criar_grafo(self, arestas):
        raise NotImplementedError("Método criar_grafo deve ser implementado nas subclasses")

    def obter_vertices(self):
        raise NotImplementedError("Método obter_vertices deve ser implementado nas subclasses")

    def obter_arestas(self):
        raise NotImplementedError("Método obter_arestas deve ser implementado nas subclasses")
        
    def existe_aresta(self, u, v):
        raise NotImplementedError("Método existe_aresta deve ser implementado nas subclasses")

    def encontrar_vertice(self, v):
        raise NotImplementedError("Método encontrar_vertice deve ser implementado nas subclasses")

    def print_graph(self):
        raise NotImplementedError("Método print_graph deve ser implementado nas subclasses")
    
    def checaGrafoEPonderado(self):
        raise NotImplementedError("Método checaGrafoEPonderado deve ser implementado nas subclasses")
    
    def dijkstra2Vertices(self, v1, v2):
        raise NotImplementedError("Método dijkstra2Vertices deve ser implementado nas subclasses")
    
    def BFS(self):
        raise NotImplementedError("Método BFS deve ser implementado nas subclasses")
    
    def encontrarDistanciaECaminhoMinimo2Vertices(self):
        raise NotImplementedError("Método encontrarDistanciaECaminhoMinimo2Vertices deve ser implementado nas subclasses")
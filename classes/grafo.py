from abc import ABC, abstractmethod

class Grafo(ABC):
    @abstractmethod
    def criar_grafo(self, arestas):
        raise NotImplementedError("Método criar_grafo deve ser implementado nas subclasses")

    @abstractmethod
    def obter_vertices(self):
        raise NotImplementedError("Método obter_vertices deve ser implementado nas subclasses")

    @abstractmethod
    def obter_graus(self):
        raise NotImplementedError("Método obter_graus deve ser implementado nas subclasses")

    @abstractmethod
    def obter_grau_medio(self):
        raise NotImplementedError("Método obter_grau_medio deve ser implementado nas subclasses")

    @abstractmethod
    def obter_arestas(self):
        raise NotImplementedError("Método obter_arestas deve ser implementado nas subclasses")
    
    @abstractmethod
    def existe_aresta(self, u, v):
        raise NotImplementedError("Método existe_aresta deve ser implementado nas subclasses")

    @abstractmethod
    def encontrar_vertice(self, v):
        raise NotImplementedError("Método encontrar_vertice deve ser implementado nas subclasses")

    @abstractmethod
    def print_graph(self):
        raise NotImplementedError("Método print_graph deve ser implementado nas subclasses")
    
    def checa_pesos_negativos(self):
        raise NotImplementedError("Método print_graph deve ser implementado nas subclasses")
    
    @abstractmethod
    def dijkstra2Vertices(self, v1, v2):
        raise NotImplementedError("Método dijkstra2Vertices deve ser implementado nas subclasses")
    
    @abstractmethod
    def dijkstraTodosVertices(self, v1, v2):
        raise NotImplementedError("Método dijkstraTodosVertices deve ser implementado nas subclasses")
    
    @abstractmethod
    def verificarVerticeInicialExiste(self, initialNode):
        raise NotImplementedError("Método verificarVerticeInicialExiste deve ser implementado nas subclasses")

    @abstractmethod
    def BFS(self, v1, v2):
        raise NotImplementedError("Método BFS deve ser implementado nas subclasses")
    
    @abstractmethod
    def BFS_tree(self, initialNode):
        raise NotImplementedError("Método BFS_tree deve ser implementado nas subclasses")

    @abstractmethod
    def run_DFS_tree(self, node, level, visited, component):
        raise NotImplementedError("Método run_DFS_tree deve ser implementado nas subclasses")

    @abstractmethod
    def DFS_tree(self, initialNode, level, visited, component = []):
        raise NotImplementedError("Método DFS_tree deve ser implementado nas subclasses")

    @abstractmethod
    def encontrarComponentesConexos(self):
        raise NotImplementedError("Método encontrarComponentesConexos deve ser implementado nas subclasses")

    @abstractmethod
    def encontrarDistanciaECaminhoMinimo2Vertices(self):
        raise NotImplementedError("Método encontrarDistanciaECaminhoMinimo2Vertices deve ser implementado nas subclasses")
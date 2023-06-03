from collections import defaultdict


class GrafoListaAdj(object):
    """ Implementação básica de um grafo. """

    def __init__(self, arestas):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.adiciona_arestas(arestas)


    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())


    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v, p in arestas:
            self.adiciona_arco(u, v, p)


    def adiciona_arco(self, u, v, p):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add((v,p))
        self.adj[v].add((u,p))


    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]


    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]
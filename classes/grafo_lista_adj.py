from collections import defaultdict


class GrafoListaAdj(object):
    def __init__(self, arestas):
        self.adj = defaultdict(set)
        self.adiciona_arestas(arestas)


    def get_vertices(self):
        return list(self.adj.keys())


    def get_arestas(self):
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


    def adiciona_arestas(self, arestas):
        for u, v, p in arestas:
            self.adiciona_arco(u, v, p)


    def adiciona_arco(self, u, v, p):
        self.adj[u].add((v,p))
        self.adj[v].add((u,p))


    def existe_aresta(self, u, v):
        return u in self.adj and v in self.adj[u]


    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]
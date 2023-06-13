from collections import defaultdict


class GrafoListaAdj(object):
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
    
    # def __len__(self):
    #return len(self.adj)
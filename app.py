from classes.grafo_lista_adj import GrafoListaAdj
from classes.grafo_matriz_adj import GrafoMatrizAdj

def ler_input(nome_arquivo):
    arestas = []
    
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        
        ttVerticesNum = linhas[0]
        linhas.pop(0)
        for linha in linhas:
            aresta = linha.split()
            origem = int(aresta[0])
            destino = int(aresta[1])
            peso = int(aresta[2])
            arestas.append((origem, destino, peso))
    return arestas

arestas = ler_input('inputs/grafo_1.txt')

tipo_grafico = input("""
Escolha o tipo de representação do Grafo: 
Digite 1 para lista de adjacência
Digite 2 para matriz de adjacência
""")
if(tipo_grafico == 1):
    grafo = GrafoListaAdj(arestas)
if(tipo_grafico == 2):
    grafo = GrafoMatrizAdj(arestas)
print(grafo)


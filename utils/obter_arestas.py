def obterArestas(nome_arquivo):
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
def obterArestas(nome_arquivo):
    arestas = []
    
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        linhas.pop(0)
        
        for linha in linhas:
            aresta = linha.split()
            possui_peso = len(aresta) > 2
            if(possui_peso):
                origem = int(aresta[0])
                destino = int(aresta[1])
                peso = int(aresta[2])
                arestas.append((origem, destino, peso))
            else:
                origem = int(aresta[0])
                destino = int(aresta[1])
                arestas.append((origem, destino))
    return arestas
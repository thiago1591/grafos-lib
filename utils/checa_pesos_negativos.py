def checaPesosNegativos(graph):
    for row in graph:
        for weight in row:
            if weight < 0:
                return False
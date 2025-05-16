def display_adjacency_list():
    nodes, edges = map(int, input().split(' '))
    start_nodes = list(map(int, input().split(' ')))
    end_nodes = list(map(int, input().split(' ')))
    weights = list(map(int, input().split(' ')))
    
    mat = {}
    for node in range(1, nodes + 1):
        mat[node] = []
    
    for idx in range(edges):
        mat[start_nodes[idx]].append((end_nodes[idx], weights[idx]))
    
    for i in mat:
        connections = mat[i]
        if not connections:
            print(f"{i}:")
        else:
            print(f"{i}:", end=" ")

            
        for i in range(len(connections)):
            if i == len(connections) - 1:
                print(connections[i])
            else:
                print(connections[i], end=" ")

display_adjacency_list()

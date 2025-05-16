def directed_weighted_graph():
    nodes, edges = map(int, input().split(' '))
    adj_mat = [[0]*nodes for i in range(nodes)]

    for _ in range(edges):
        from_node, to_node, weight = map(int, input().split(' '))
        adj_mat[from_node - 1][to_node - 1] = weight

    for row in adj_mat:
        print(*row)

directed_weighted_graph()
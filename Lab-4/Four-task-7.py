import math

def coprime_query():
    nodes, queries = map(int, input().split())
    adjacency_list = [[] for _ in range(nodes)]

    for u in range(1, nodes + 1):
        for v in range(1, nodes + 1):
            if u != v and math.gcd(u, v) == 1:
                adjacency_list[u - 1].append(v)


    for _ in range(queries):
        index, position = map(int, input().split())
        
        if len(adjacency_list[index - 1]) >= position:
            print(adjacency_list[index - 1][position - 1])
        else:
            print(-1)

coprime_query()

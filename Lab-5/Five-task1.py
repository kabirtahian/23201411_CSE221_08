def BFS(G, s, n):
    colour = [0] * (n + 1)
    Q = [0] * (n + 10)
    front = 0
    rear = 0
    bfs_order = []

    colour[s] = 1
    Q[rear] = s
    rear += 1

    while front < rear:
        u = Q[front]
        front += 1
        bfs_order.append(u)

        for v in G[u]:
            if colour[v] == 0:
                colour[v] = 1
                Q[rear] = v
                rear += 1

    return bfs_order

    
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)



result = BFS(g, 1, n)
print(' '.join(map(str, result)))
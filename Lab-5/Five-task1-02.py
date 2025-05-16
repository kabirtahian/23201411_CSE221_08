from collections import deque

def bfs(g, s, n):
    queue = deque()
    queue.append(s)

    visited = [False for _ in range(n+1)]
    visited[s] = True

    while len(queue) > 0:
        u = queue.popleft()
        print(u, end=" ")

        for v in g[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

            

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

result = bfs(g, 1, n)
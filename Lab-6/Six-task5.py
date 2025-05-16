import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

distance = [-1] * (n + 1)

def bfs(start):
    for i in range(1, n + 1):
        distance[i] = -1
    q = deque([start])
    distance[start] = 0
    farthest = start

    while q:
        u = q.popleft()
        for v in g[u]:
            if distance[v] == -1:
                distance[v] = distance[u] + 1
                q.append(v)
                if distance[v] > distance[farthest]:
                    farthest = v

    return farthest, distance[farthest]

a, _ = bfs(1)

b, length = bfs(a)

print(length)
print(a, b)

import heapq
import sys

def min_danger_levels(n, graph):
    danger = [float('inf')] * (n + 1)
    danger[1] = 0

    pq = [(0, 1)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > danger[u]:
            continue
        for v, w in graph[u]:
            new_danger = max(d, w)
            if new_danger < danger[v]:
                danger[v] = new_danger
                heapq.heappush(pq, (new_danger, v))

    return danger[1:]


input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w)) 


result = min_danger_levels(n, graph)

for val in result:
    print(val if val != float('inf') else -1, end=' ')
print()

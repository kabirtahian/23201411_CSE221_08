import heapq
import sys

def dijkstra(n, graph, start):
    dist = [float('inf')] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


input = sys.stdin.readline
n, m, s, t = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist_s = dijkstra(n, graph, s)
dist_t = dijkstra(n, graph, t)


minTime = float('inf')
meet_node = -1

for i in range(1, n + 1):
    maxTime = max(dist_s[i], dist_t[i])
    if dist_s[i] != float('inf') and dist_t[i] != float('inf'):
        if maxTime < minTime or (maxTime == minTime and i < meet_node):
            minTime = maxTime
            meet_node = i


if meet_node == -1:
    print(-1)
else:
    print(f"{minTime} {meet_node}")

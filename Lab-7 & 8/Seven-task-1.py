import sys
import heapq


def dijkstra(n, graph, src, dest):
    dist = [float('inf')] * (n + 1)
    prev = [-1] * (n + 1)
    dist[src] = 0

    heap = [(0, src)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(heap, (dist[v], v))

    if dist[dest] == float('inf'):
        return -1, []
    
    path = []
    node = dest
    while node != -1:
        path.append(node)
        node = prev[node]
    path.reverse()

    return dist[dest], path


n, m, s, d = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))


graph = [[] for _ in range(n + 1)]
for i in range(m):
    graph[u[i]].append((v[i], w[i]))


distance, path = dijkstra(n, graph, s, d)


if distance == -1:
    print(-1)
else:
    print(distance)
    print(' '.join(map(str, path)))

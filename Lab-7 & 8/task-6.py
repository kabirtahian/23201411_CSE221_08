import heapq
import sys
input = sys.stdin.readline

def second_shortest_path(n, m, s, d, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    INF = float('inf')
    dist1 = [INF] * (n + 1)
    dist2 = [INF] * (n + 1)

    dist1[s] = 0
    pq = [(0, s)]

    while pq:
        cost, u = heapq.heappop(pq)
        for v, w in graph[u]:
            new_cost = cost + w
            if new_cost < dist1[v]:
                dist2[v] = dist1[v]
                dist1[v] = new_cost
                heapq.heappush(pq, (new_cost, v))
            elif dist1[v] < new_cost < dist2[v]:
                dist2[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return dist2[d] if dist2[d] != INF else -1


n, m, s, d = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(second_shortest_path(n, m, s, d, edges))

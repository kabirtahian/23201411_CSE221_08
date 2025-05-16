import heapq
import sys

def dijkstra_node_weight(n, graph, weights, start, end):
    dist = [float('inf')] * (n + 1)
    dist[start] = weights[start]

    pq = [(weights[start], start)] 

    while pq:
        cost, u = heapq.heappop(pq)
        if u == end:
            return cost
        if cost > dist[u]:
            continue
        for v in graph[u]:
            new_cost = cost + weights[v]
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(pq, (new_cost, v))

    return -1


input = sys.stdin.readline
n, m, s, d = map(int, input().split())
weights_input = list(map(int, input().split()))
weights = [0] + weights_input 

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)


result = dijkstra_node_weight(n, graph, weights, s, d)

print(result)

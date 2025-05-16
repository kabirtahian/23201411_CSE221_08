import heapq
import sys
input = sys.stdin.readline

def solve(n, m, u, v, w):
    from collections import defaultdict

    graph = [[] for _ in range(n + 1)]
    for u, v, w in zip(u, v, w):
        graph[u].append((v, w))


    INF = float('inf')
    dist = [[INF] * 2 for _ in range(n + 1)]

    pq = []

    for v, w in graph[1]:
        p = w % 2
        if w < dist[v][p]:
            dist[v][p] = w
            heapq.heappush(pq, (w, v, p)) 

    while pq:
        cost, u, parity = heapq.heappop(pq)
        if cost > dist[u][parity]:
            continue
        for v, w in graph[u]:
            new_parity = w % 2
            if new_parity == parity:
                continue
            new_cost = cost + w
            if new_cost < dist[v][new_parity]:
                dist[v][new_parity] = new_cost
                heapq.heappush(pq, (new_cost, v, new_parity))

    ans = min(dist[n][0], dist[n][1])
    print(ans if ans != INF else -1)

n, m = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))
w = list(map(int, input().split()))

solve(n, m, u, v, w)

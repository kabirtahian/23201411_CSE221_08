from collections import deque, defaultdict
import sys

def advising(N, M, prereq):
    graph = defaultdict(list)
    inDeg = [0] * (N + 1)

    for a, b in prereq:
        graph[a].append(b)
        inDeg[b] += 1

    queue = deque()
    for i in range(1, N + 1):
        if inDeg[i] == 0:
            queue.append(i)

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            inDeg[neighbor] -= 1
            if inDeg[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == N:
        print(' '.join(map(str, topo_order)))
    else:
        print(-1)

N, M = map(int, input().split())
prereq = []
for _ in range(M):

    a, b = map(int, input().split())
    prereq.append((a, b))

advising(N, M, prereq)
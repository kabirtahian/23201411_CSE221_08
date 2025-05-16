import sys
input = sys.stdin.readline

N, R = map(int, input().split())
g = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

subtree = [0] * (N + 1)
visited = [False] * (N + 1)
stack = [(R, -1, 0)]
parent = [-1] * (N + 1)
postorder = []

while stack:
    node, par, state = stack.pop()
    if state == 0:
        parent[node] = par
        stack.append((node, par, 1)) 
        for nei in g[node]:
            if nei != par:
                stack.append((nei, node, 0))
    else:

        size = 1
        for nei in g[node]:
            if nei != parent[node]:
                size += subtree[nei]
        subtree[node] = size


Q = int(input())
for _ in range(Q):
    X = int(input())
    print(subtree[X])

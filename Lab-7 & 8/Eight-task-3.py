import sys

def find(parent, x):

    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def unite(parent, rank, a, b):
    # Union by rank
    a = find(parent, a)
    b = find(parent, b)
    if a == b:
        return False
    if rank[a] < rank[b]:
        a, b = b, a
    parent[b] = a
    if rank[a] == rank[b]:
        rank[a] += 1
    return True



input = sys.stdin.readline
N, M = map(int, input().split())
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

parent = list(range(N+1))
rank = [0] * (N+1)
edges.sort()
in_mst = [False] * M
mst_cost = 0
adj = [[] for _ in range(N+1)]
cnt = 0
for i, (w, u, v) in enumerate(edges):
    if unite(parent, rank, u, v):
        in_mst[i] = True
        mst_cost += w
        adj[u].append((v, w))
        adj[v].append((u, w))
        cnt += 1
        if cnt == N - 1:
            break

if cnt < N - 1:
    print(-1)
    sys.exit()

def dfs(u, p):
    for v, w in adj[u]:
        if v == p:
            continue
        depth[v] = depth[u] + 1
        up[v][0] = u
        maxEdge[v][0] = w
        for k in range(1, LOG):
            up[v][k] = up[ up[v][k-1] ][k-1]
            maxEdge[v][k] = max(maxEdge[v][k-1], maxEdge[ up[v][k-1] ][k-1])
        dfs(v, u)

LOG = (N+1).bit_length()
up = [[0] * LOG for _ in range(N+1)]
maxEdge = [[0] * LOG for _ in range(N+1)]
depth = [0] * (N+1)


for k in range(LOG):
    up[1][k] = 1
    maxEdge[1][k] = 0
depth[1] = 0
dfs(1, 0)


def get_max_on_path(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    mx = 0
    for k in range(LOG-1, -1, -1):
        if diff & (1 << k):
            mx = max(mx, maxEdge[u][k])
            u = up[u][k]
    if u == v:
        return mx
    for k in range(LOG-1, -1, -1):
        if up[u][k] != up[v][k]:
            mx = max(mx, maxEdge[u][k], maxEdge[v][k])
            u = up[u][k]
            v = up[v][k]
    mx = max(mx, maxEdge[u][0], maxEdge[v][0])
    return mx

sec_max = float('inf')
for i, (w, u, v) in enumerate(edges):
    if in_mst[i]:
        continue
    mx = get_max_on_path(u, v)
    if w > mx:
        sec_max = min(sec_max, mst_cost - mx + w)

print(sec_max if sec_max < float('inf') else -1)

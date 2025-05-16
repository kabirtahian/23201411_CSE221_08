import sys
input = sys.stdin.read
sys.setrecursionlimit(10**7)

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    root_u = find(u)
    root_v = find(v)

    if root_u == root_v:
        return False

    if size[root_u] < size[root_v]:
        root_u, root_v = root_v, root_u

    parent[root_v] = root_u
    size[root_u] += size[root_v]
    return True

data = input().split()
n = int(data[0])
m = int(data[1])

edges = []
index = 2
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    edges.append((w, u, v))
    index += 3

edges.sort()

parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

total_cost = 0
for weight, u, v in edges:
    if union(u, v):
        total_cost += weight

print(total_cost)

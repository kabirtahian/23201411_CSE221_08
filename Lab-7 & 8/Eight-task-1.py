import sys
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)

    if rootX != rootY:

        if size[rootX] < size[rootY]:
            rootX, rootY = rootY, rootX
        parent[rootY] = rootX
        size[rootX] += size[rootY]

    return size[find(rootX)]

n, k = map(int, input().split())
parent = [i for i in range(n + 1)]
size = [1] * (n + 1)

for _ in range(k):
    a, b = map(int, input().split())
    print(union(a, b))

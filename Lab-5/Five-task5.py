import sys
sys.setrecursionlimit(2 * 100000 + 5)

n, m = map(int, input().split())

g = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)


color = {i: 'White' for i in range(1, n + 1)} 
cycle = [False]  


def cyclic_dfs(u):
    color[u] = "Grey"  
    for v in g[u]:
        if color[v] == 'White':
            cyclic_dfs(v)
        elif color[v] == "Grey":
            cycle[0] = True
    color[u] = "Black"  


for v in range(1, n + 1):
    if color[v] == 'White':
        cyclic_dfs(v)

if cycle[0]:
    print("YES")
else:
    print("NO")
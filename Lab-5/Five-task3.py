from collections import deque


def shortest_path(g, n, s, d):

    for i in g:
        i.sort()
        
    queue = deque()
    visited = [False for _ in range(n + 1)]
    short_path = [float('inf') for _ in range(n + 1)]
    parents = [-1 for _ in range(n + 1)]
    
    queue.append(s)
    visited[s] = True
    short_path[s] = 0

    while len(queue) > 0:
        u = queue.popleft()

        for v in g[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                short_path[v] = short_path[u] + 1
                
                parents[v] = u

    if not visited[d]:
        print("-1")
    else:
        print(short_path[d])
        pathh(s, d, parents)

def pathh(s, d, parents):
    curr = d
    route = []
    while curr != s:
        route.append(curr)
        curr = parents[curr]
    
    route.append(s)
    print(' '.join(map(str, route[::-1])))

n, m, s, d = map(int, input().split())
u = list(map(int, input().split()))
v = list(map(int, input().split()))

g = [[] for _ in range(n + 1)]


for i in range(m):
    g[u[i]].append(v[i])
    g[v[i]].append(u[i])

shortest_path(g, n, s, d)
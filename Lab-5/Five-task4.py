from collections import deque
def sKd(g, n, s):
    queue = deque()
    queue.append(s)
    short_path = [float('inf') for _ in range(n + 1)]
    parents = [-1 for _ in range(n + 1)]
    short_path[s] = 0
    while len(queue) > 0:
        u = queue.popleft()

        for v in g[u]:
            if short_path[v] == float('inf'):
                queue.append(v)
                short_path[v] = short_path[u] + 1
                parents[v] = u

    return short_path, parents

def pathh(s, d, parents):
    curr = d
    route = []
    while curr != s:
        route.append(curr)
        curr = parents[curr]
        if curr == -1:
            return []
    route.append(s)
    route.reverse()
    return route

n, m, s, d, k = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

dis_s, parent_s = sKd(g, n, s)
dis_k, parent_k = sKd(g, n, k)

if dis_s[k] == float('inf') or dis_k[d] == float('inf'):
    print("-1")
else:
    print(dis_s[k] + dis_k[d])
    str1 = pathh(s, k, parent_s)
    str2 = pathh(k, d, parent_k)[1:]
    total_path = str1 + str2
    print(" ".join(map(str, total_path)))
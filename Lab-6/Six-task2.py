from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

color = [-1] * (n + 1)
ans = 0

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    count = [0, 0]
    color[start] = 0
    count[0] += 1

    while queue:
        u, c = queue.popleft()
        for v in g[u]:
            if color[v] == -1:
                color[v] = 1 - c
                count[1 - c] += 1
                queue.append((v, 1 - c))
            elif color[v] == c:
                pass
    return max(count)

for i in range(1, n + 1):
    if color[i] == -1:
        ans += bfs(i)

print(ans)

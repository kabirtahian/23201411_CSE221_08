from collections import deque

# Input
n = int(input())
x1, y1, x2, y2 = map(int, input().split())


x1 -= 1
y1 -= 1
x2 -= 1
y2 -= 1

psblmoves = [
    (2, 1), (2, -1), (-2, 1), (-2, -1),
    (1, 2), (1, -2), (-1, 2), (-1, -2)
]


visited = [[False] * n for _ in range(n)]
distance = [[-1] * n for _ in range(n)]

q = deque()
q.append((x1, y1))
visited[x1][y1] = True
distance[x1][y1] = 0

while q:
    x, y = q.popleft()
    if (x, y) == (x2, y2):
        break
    for dx, dy in psblmoves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            distance[nx][ny] = distance[x][y] + 1
            q.append((nx, ny))


print(distance[x2][y2])

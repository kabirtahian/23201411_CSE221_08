from collections import deque

def bfs(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        if grid[x][y] == 'D':
            count += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < h and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))
    return count


r, h = map(int, input().split())
grid = [input().strip() for _ in range(r)]
visited = [[False for _ in range(h)] for _ in range(r)]


result = 0
for i in range(r):
    for j in range(h):
        if not visited[i][j] and grid[i][j] != '#':
            result = max(result, bfs(i, j))

print(result)

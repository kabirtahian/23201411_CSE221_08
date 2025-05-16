import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
words = [input().strip() for _ in range(n)]

graph = [[] for _ in range(26)]
indegree = [0] * 26
used = [False] * 26


for word in words:
    for ch in word:
        used[ord(ch) - ord('a')] = True


for i in range(n - 1):
    w1, w2 = words[i], words[i + 1]
    min_len = min(len(w1), len(w2))
    mismatch_found = False
    for j in range(min_len):
        if w1[j] != w2[j]:
            u = ord(w1[j]) - ord('a')
            v = ord(w2[j]) - ord('a')
            if v not in graph[u]:
                graph[u].append(v)
                indegree[v] += 1
            mismatch_found = True
            break
    if not mismatch_found and len(w1) > len(w2):
        print(-1)
        sys.exit()


heap = []
for i in range(26):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

res = []
while heap:
    u = heapq.heappop(heap)
    res.append(chr(u + ord('a')))
    for v in sorted(graph[u]):
        indegree[v] -= 1
        if indegree[v] == 0:
            heapq.heappush(heap, v)

if len(res) != 26:
    print(-1)
else:
    print("".join(res))

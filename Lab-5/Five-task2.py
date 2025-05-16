import sys
sys.setrecursionlimit(2*100000+5)


def DFS(g, s, n):
    visited = set()
    
    st = [s]

    while st:
        v = st.pop()
        if v not in visited:
            print(v, end=" ")
            visited.add(v)

            u = g[v]
            for i in range(len(u)-1, -1, -1):
                new_u = u[i]
                if new_u not in visited:
                    st.append(new_u)


n, m = map(int, input().split(' '))
u = list(map(int, input().split(' ')))
v = list(map(int, input().split(' ')))

g = [[] for i in range(n+1)]

for i in range(m):
    g[u[i]].append(v[i])
    g[v[i]].append(u[i])


result = DFS(g, 1, n)
import sys

def check_euler_path():
    nodes, edges = map(int, sys.stdin.readline().split())
    odd_degrees = 0
    degree_count = [0] * (nodes + 1)
    

    from_nodes = list(map(int, sys.stdin.readline().split()))
    to_nodes = list(map(int, sys.stdin.readline().split()))
    
    for idx in range(edges):
        degree_count[from_nodes[idx]] += 1
        degree_count[to_nodes[idx]] += 1


    for i in degree_count:
        if i % 2 != 0:
            odd_degrees += 1


    if odd_degrees == 0 or odd_degrees == 2:
        print("YES")

    else:
        print("NO")



check_euler_path()

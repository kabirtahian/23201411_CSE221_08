def build_adjacency_matrix():
    size = int(input())
    adj_matrix = [[0]*size for _ in range(size)]
    
    for row in range(size):
        connections = list(map(int, input().split(' ')))
        for col in range(1, len(connections)):
            adj_matrix[row][connections[col]] = 1
    
    for row in adj_matrix:
        print(*row)

build_adjacency_matrix()

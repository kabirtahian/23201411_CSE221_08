def surrounding_cells():
    size = int(input())
    row, col = map(int, input().split())
    
    directions = [
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
        (row, col - 1),                   (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    ]
    
    neighbors = []
    for r, c in directions:
        if 0 < r <= size and 0 < c <= size:
            neighbors.append((r, c))
    
    neighbors.sort()
    
    print(len(neighbors))
    for r, c in neighbors:
        print(r, c)

surrounding_cells()
    
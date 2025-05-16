def sortingAgain(arr, n):

    swap = 0
    for i in range(n):
        midx = i

        for j in range(i+1, n):
            
            if (arr[j][1] > arr[midx][1]) or (arr[j][1] == arr[midx][1] and arr[j][0] < arr[midx][0]):
                midx = j
                
                
        if midx != i:
            arr[i], arr[midx] = arr[midx], arr[i]
            swap += 1
        
    return swap
    


n = int(input())
ids = list(map(int, input().split(" ")))
marks = list(map(int, input().split(" ")))

student = list(zip(ids, marks))

swap = sortingAgain(student, n)
print(f"Minimum swaps: {swap}")

for k in student:
    print(f"ID: {k[0]} Mark: {k[1]}")
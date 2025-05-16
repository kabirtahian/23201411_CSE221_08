def mergeArrays(n, arr1, m, arr2):
    i, j = 0, 0
    merged = [0] * (n + m)
    idx = 0

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            merged[idx] = arr1[i]
            i += 1
        else:
            merged[idx] = arr2[j]
            j += 1
        idx += 1

    while i < n:
        merged[idx] = arr1[i]
        i += 1
        idx += 1

    while j < m:
        merged[idx] = arr2[j]
        j += 1
        idx += 1

    print(" ".join(map(str, merged)))

n = int(input())
arr1 = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

mergeArrays(n, arr1, m, arr2)


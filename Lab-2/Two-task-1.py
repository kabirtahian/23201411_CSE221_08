def twoSumTrouble(N, S, A):
    left, right = 0, N-1
    
    while left < right:
        curr_sum = A[left] + A[right]

        if curr_sum == S:
            return f"{left+1} {right+1}"

        elif curr_sum < S:
            left += 1
        else:
            right -= 1


    return -1

n, s = map(int, input().split(" "))
arr = list(map(int, input().split(' ')))

print(twoSumTrouble(n, s, arr))
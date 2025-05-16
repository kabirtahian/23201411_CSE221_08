import sys

def lower_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

def upper_bound(arr, target):
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left

num_elements, num_queries = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

results = []
for _ in range(num_queries):
    lower_limit, upper_limit = map(int, sys.stdin.readline().split())
    lower_index = lower_bound(numbers, lower_limit)
    upper_index = upper_bound(numbers, upper_limit)
    results.append(str(upper_index - lower_index))

sys.stdout.write("\n".join(results) + "\n")

def firstOneIndex(binary_str):
    left, right = 0, len(binary_str) - 1
    position = -1 

    while left <= right:
        mid = (left + right) // 2

        if binary_str[mid] == '1':
            position = mid + 1
            right = mid - 1 
        else:
            left = mid + 1 

    return position


test_cases = int(input())

for _ in range(test_cases):
    binary_str = input()
    print(firstOneIndex(binary_str))




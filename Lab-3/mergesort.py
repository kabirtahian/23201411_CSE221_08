def merge_sort(arr):
    res = 0
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]


        merge_sort(left_arr)
        merge_sort(right_arr)


        i = 0               #left arr index
        j = 0               #right arr index
        k = 0               #merged arr index

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                res += 1
            k += 1

        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
    return res

n = int(input())
array_test = list(map(int, input().split(' ')))

print(merge_sort(array_test))

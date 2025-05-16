def max_subarray_length(size, limit, nums):
    longest = 0  
    window_sum = 0  
    left = 0  

    for right in range(size):  
        window_sum += nums[right] 
        
        while window_sum > limit:
            window_sum -= nums[left]  
            left += 1 

        longest = max(longest, right - left + 1)

    return longest 

size, limit = map(int, input().split())
nums = list(map(int, input().split()))

print(max_subarray_length(size, limit, nums))

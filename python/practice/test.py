def new_func(nums):
    i = 0
    for j in range(len(nums), 0, -1):
        if nums[j] != nums[j - 1]:
            nums[i] = nums[j]
            i += 1
    return i


arr = [1, 1, 2]
new_func(arr)
print(arr)
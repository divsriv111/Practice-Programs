def RemoveDuplicate2(arr):
    res = 1
    n = len(arr)
    for i in range(1, n):
        if arr[i] != arr[res - 1]:
            arr[res] = arr[i]
            res += 1
    return arr[:res]


arr = list(map(int, input().strip().split()))
print(RemoveDuplicate2(arr))

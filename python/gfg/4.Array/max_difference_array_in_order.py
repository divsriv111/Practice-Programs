def MaxDiff(arr):
    res = arr[1] - arr[0]
    minVal = arr[0]
    n = len(arr)
    for i in range(1, n):
        res = max(res, arr[i] - minVal)
        minVal = min(minVal, arr[i])

    return res


arr = list(map(int, input().strip().split()))
print(MaxDiff(arr))

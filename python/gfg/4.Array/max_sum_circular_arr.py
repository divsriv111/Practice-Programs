def MaxSumSubArray(arr):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1, len(arr)):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(maxEnding, res)
    return res


def MinSumSubArray(arr):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1, len(arr)):
        maxEnding = min(maxEnding + arr[i], arr[i])
        res = min(maxEnding, res)
    return res


def MaxSumCircularSubArray(arr):
    maxSubArr = MaxSumSubArray(arr)
    minSubArr = MinSumSubArray(arr)
    sumArr = sum(arr)
    return max(sumArr - minSubArr, maxSubArr)


arr = list(map(int, input().strip().split()))
print(MaxSumCircularSubArray(arr))

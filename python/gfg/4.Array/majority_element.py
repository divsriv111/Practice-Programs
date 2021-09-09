def MajorityElement(arr):
    d = {}
    maxRes = -1
    n = len(arr)
    for i in range(n - 1, -1, -1):
        if arr[i] in d:
            d[arr[i]] += 1
            if d[arr[i]] > n / 2:
                maxRes = i
        else:
            d[arr[i]] = 1
    return maxRes


arr = list(map(int, input().strip().split()))
print(MajorityElement(arr))

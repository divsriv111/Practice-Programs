def GetExtraElement(arr) -> int:
    res = 0
    for i in arr:
        res = res ^ i

    return res


n = int(input())
arr = list(map(int, input().strip().split()))[:n]

print(GetExtraElement(arr))
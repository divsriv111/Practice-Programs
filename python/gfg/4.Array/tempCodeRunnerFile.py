def IsSorted(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(IsSorted(arr))

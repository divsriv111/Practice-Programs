def ReverseArray(arr):
    n = len(arr)
    start = 0
    end = n - 1
    while end > start:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


arr = list(map(int, input().strip().split()))
print(ReverseArray(arr))

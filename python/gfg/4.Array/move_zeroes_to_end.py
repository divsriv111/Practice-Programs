def Method(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        if arr[start] == 0 and arr[end] != 0:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        else:
            start += 1
            end -= 1
    return arr


arr = list(map(int, input().strip().split()))
print(Method(arr))

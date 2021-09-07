def MoveZero(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[count] = arr[count], arr[i]
            count += 1
    return arr


arr = list(map(int, input().strip().split()))
print(MoveZero(arr))

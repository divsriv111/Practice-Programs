def Method(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] == x:
            return (arr[left], arr[right])
        elif arr[left] + arr[right] > x:
            high = high - 1
        else:
            low = low + 1
    return -1


x = int(input())
arr = list(map(int, input().strip().split()))
print(Method(arr))
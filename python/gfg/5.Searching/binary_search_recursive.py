def binary_search(arr, low, high, x):
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


x = int(input())
arr = list(map(int, input().strip().split()))
print(binary_search(arr, 0, len(arr) - 1, x))

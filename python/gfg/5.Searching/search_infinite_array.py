def binary_search(arr, x, low, high):
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


def search(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    while arr[i] < x:
        i = i * 2

    if arr[i] == x:
        return i

    return binary_search(arr, x, (i // 2) + 1, i - 1)


x = int(input())
arr = list(map(int, input().strip().split()))
print(search(arr, n))

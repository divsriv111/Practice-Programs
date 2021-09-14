def lastOccRecurrsive(arr, low, high, x, n):
    if low > high:
        return -1

    mid = (high + low) // 2
    if arr[mid] < x:
        return lastOccRecurrsive(arr, mid + 1, high, x, n)
    elif arr[mid] > x:
        return lastOccRecurrsive(arr, low, mid - 1, x, n)
    else:
        if mid == n - 1 or arr[mid + 1] != arr[mid]:
            return mid
        else:
            return lastOccRecurrsive(arr, mid + 1, high, x, n)


def lastOccIterative(arr, x):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2

        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            if mid == n - 1 or arr[mid + 1] != arr[mid]:
                return mid
            else:
                low = mid + 1
    return -1


x = int(input())
arr = list(map(int, input().strip().split()))
print(lastOccRecurrsive(arr, 0, len(arr) - 1, x, len(arr)))
print(lastOccIterative(arr, x))
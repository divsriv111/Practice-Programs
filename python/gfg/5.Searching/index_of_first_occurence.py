def firstOccRecurrsive(arr, low, high, x):
    if low > high:
        return -1

    mid = (high + low) // 2
    if arr[mid] < x:
        return firstOccRecurrsive(arr, mid + 1, high, x)
    elif arr[mid] > x:
        return firstOccRecurrsive(arr, low, mid - 1, x)
    else:
        if mid == 0 or arr[mid - 1] != arr[mid]:
            return mid
        else:
            return firstOccRecurrsive(arr, low, mid - 1, x)


def firstOccIterative(arr, x):
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
            if mid == 0 or arr[mid - 1] != arr[mid]:
                return mid
            else:
                high = mid - 1
    return -1


x = int(input())
arr = list(map(int, input().strip().split()))
print(firstOccRecurrsive(arr, 0, len(arr) - 1, x))
print(firstOccIterative(arr, x))
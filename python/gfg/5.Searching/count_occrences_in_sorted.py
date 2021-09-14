def firstOcc(arr, x):
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


def lastOcc(arr, x):
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


def countOcc(arr, x):
    first = firstOcc(arr, x)

    if first == -1:
        return 0
    else:
        return lastOcc(arr, x) - first + 1


def countOccNaive(arr, x):
    n = len(arr)
    low = 0
    high = n - 1
    count = 0
    index = 0
    while low <= high:
        mid = (low + high) // 2

        if x > arr[mid]:
            low = mid + 1
        elif x < arr[mid]:
            high = mid - 1
        else:
            index = mid
            break
    for i in range(index, n):
        if arr[i] == x:
            count += 1

    return count


x = int(input())
arr = list(map(int, input().strip().split()))
print(countOcc(arr, x))
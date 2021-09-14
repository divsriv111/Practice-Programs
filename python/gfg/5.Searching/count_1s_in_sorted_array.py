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


arr = list(map(int, input().strip().split()))
arr.sort()
first_occ = firstOccIterative(arr, 1)
print(first_occ)
if first_occ == -1:
    print(-1)
else:
    print(len(arr) - first_occ + 1)
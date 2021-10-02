def InsertionSort(arr, n):
    #O(n^2)
    #stable
    for i in range(n):
        key = arr[i]
        j = i - 1
        while (j >= 0 and arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr = list(map(int, input().strip().split()))
print(InsertionSort(arr, len(arr)))
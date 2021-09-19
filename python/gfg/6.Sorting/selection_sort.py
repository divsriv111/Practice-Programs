def SelectionSort(arr, n):
    #O(n^2)
    #unstable sorting algo
    for i in range(n - 1):
        mid_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[mid_index]:
                mid_index = j
        arr[mid_index], arr[i] = arr[i], arr[mid_index]
    return arr


arr = list(map(int, input().strip().split()))
print(SelectionSort(arr, len(arr)))
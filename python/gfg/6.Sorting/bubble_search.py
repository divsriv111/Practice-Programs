def BubbleSort(arr):
    #O(n^2)
    #stable sorting algo
    swapped = False
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if swapped == False:
            break
    return arr


arr = list(map(int, input().strip().split()))
print(BubbleSort(arr))
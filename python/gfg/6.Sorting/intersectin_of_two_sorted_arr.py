def intersectinOfArray(arr1, arr2):
    i = 0
    j = 0
    m = len(arr1)
    n = len(arr2)
    while i < m and j < n:
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1
            continue

        if arr1[i] < arr2[j]:
            i += 1

        elif arr1[i] > arr2[j]:
            j += 1
        else:
            print(arr1[i], end=' ')
            i += 1
            j += 1


arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))
intersectinOfArray(arr1, arr2)
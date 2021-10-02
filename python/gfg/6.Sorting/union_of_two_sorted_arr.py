def unionOfArray(arr1, arr2):
    i = 0
    j = 0
    m = len(arr1)
    n = len(arr2)
    while i < m and j < n:
        if i > 0 and arr1[i] == arr1[i - 1]:
            i += 1
            continue

        if j > 0 and arr2[j] == arr2[j - 1]:
            j += 1
            continue

        if arr1[i] < arr2[j]:
            print(arr1[i], end=' ')
            i += 1
        elif arr1[i] > arr2[j]:
            print(arr2[j], end=' ')
            j += 1
        else:
            print(arr1[i], end=' ')
            i += 1
            j += 1

        while i < m:
            print(arr1[i], end=' ')
            i += 1

        while j < n:
            print(arr2[j], end=' ')
            j += 1


arr1 = list(map(int, input().strip().split()))
arr2 = list(map(int, input().strip().split()))
unionOfArray(arr1, arr2)
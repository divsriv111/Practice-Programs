def Merge(arr1, arr2):
    i = 0
    j = 0
    res = []
    m = len(arr1)
    n = len(arr2)
    while i < m and j < n:
        if arr1[i] <= arr2[j]:
            res.append(arr1[i])
            i += 1
        else:
            res.append(arr2[j])
            j += 1

    while i < m:
        res.append(arr1[i])
        i += 1

    while j < n:
        res.append(arr2[j])
        j += 1

    return res


def Method(arr, n, low, mid, high):
    res = Merge(arr[low:mid + 1], arr[mid + 1:high + 1])
    arr[low:high + 1] = res
    return arr


low = int(input())
mid = int(input())
high = int(input())
arr = list(map(int, input().strip().split()))
print(Method(arr, len(arr), low, mid, high))
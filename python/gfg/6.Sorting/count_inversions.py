#inversions means how many elements are smaller than current element in right side
#will use merge sort for this task
def CountAndMerge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray
    res = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            res = res + (n1 - i)
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return res


def CountInv(arr, l, r):
    res = 0
    if l < r:

        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        res += CountInv(arr, l, m)
        res += CountInv(arr, m + 1, r)
        res += CountAndMerge(arr, l, m, r)

    return res


arr = [2, 4, 1, 3, 5]
n = len(arr)
print(f"Given array is: {arr}")

print(f"Inversions is: {CountInv(arr, 0, n - 1)}")
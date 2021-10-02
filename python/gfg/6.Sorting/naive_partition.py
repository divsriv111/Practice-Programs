def partition(arr, l, h, p):
    temp = [0] * (h - l + 1)
    index = 0
    for i in range(l, h + 1):
        if arr[i] <= arr[p] and i != p:
            temp[index] = arr[i]
            index += 1
    temp[index] = arr[p]
    index += 1
    for i in range(l, h + 1):
        if arr[i] > arr[p]:
            temp[index] = arr[i]
            index += 1
    for i in range(l, h + 1):
        arr[i] = temp[i - l]

    return arr


arr = [5, 13, 6, 9, 12, 11, 8]

print(partition(arr, 0, len(arr) - 1, 3))

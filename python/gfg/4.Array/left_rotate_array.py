def reverse(arr, low, high):
    while low < high:
        arr[high], arr[low] = arr[low], arr[high]
        low += 1
        high -= 1
    return arr


def LeftRotate(arr, d, n):
    arr = reverse(arr, 0, d - 1)
    arr = reverse(arr, d, n - 1)
    arr = reverse(arr, 0, n - 1)
    return arr


d = int(input())
arr = list(map(int, input().strip().split()))
print(LeftRotate(arr, d, len(arr)))

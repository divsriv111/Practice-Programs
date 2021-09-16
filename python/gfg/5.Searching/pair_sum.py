def PairSum(arr):
    left = 0
    right = len(arr) - 1
    while left <= right:
        if arr[left] + arr[right] == x:
            return (arr[left], arr[right])
        elif arr[left] + arr[right] > x:
            right = right - 1
        else:
            left = left + 1
    return -1


x = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()
print(PairSum(arr))
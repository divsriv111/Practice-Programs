def LargestElementIndex(arr):
    maxIndex = 0
    n = len(arr)
    for i in range(1, n):
        if arr[maxIndex] < arr[i]:
            maxIndex = i
    return maxIndex


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(LargestElementIndex(arr))

def SecondMaxElement(arr):
    maxIndex = 0
    lastMaxIndex = -1
    n = len(arr)
    for i in range(1, n):
        if arr[maxIndex] < arr[i]:
            lastMaxIndex = maxIndex
            maxIndex = i
        elif arr[maxIndex] != arr[i]:
            if lastMaxIndex == -1 or arr[i] > arr[lastMaxIndex]:
                lastMaxIndex = i
    return lastMaxIndex


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(SecondMaxElement(arr))

def printGroups(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            if arr[i] != arr[0]:
                print(f"From {i} to", end=" ")
            else:
                print(i - 1, end=" ")

    if arr[n - 1] != arr[0]:
        print(n - 1)


arr = list(map(int, input().strip().split()))
printGroups(arr)

def GetFrequency(arr):
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def method2(arr):
    freq = 1
    i = 1
    n = len(arr)
    while i < n:
        while i < n and arr[i] == arr[i - 1]:
            freq += 1
            i += 1

        print(arr[i - 1], freq)

        i += 1
        freq = 1


arr = list(map(int, input().strip().split()))
print(GetFrequency(arr))

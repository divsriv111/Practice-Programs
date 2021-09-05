def addBinary(arr):
    a = arr[0]
    b = arr[1]
    sum = bin(int(a, 2) + int(b, 2))
    return str(sum[2:])


n = int(input())
arr = list(map(str, input().strip().split()))[:n]
print(addBinary(arr))

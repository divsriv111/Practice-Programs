def plusOne(digits):
    a = "".join(map(str,digits))
    b = int(a)
    b = b + 1
    res = list(map(int, str(b)))
    return res


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(plusOne(arr))
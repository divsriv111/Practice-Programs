def FindSqrt(n):
    low = 1
    high = n - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        mysqrt = mid * mid
        if mysqrt > n:
            high = high - 1
        elif mysqrt < n:
            low = low + 1
            ans = mid - 1
        else:
            return mid

    return ans


n = int(input())
print(FindSqrt(n))
def SumOfN(n):
    if n == 1:
        return 1
    return n + SumOfN(n - 1)


n = int(input())
print(SumOfN(n))
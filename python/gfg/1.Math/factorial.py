def Fact(n) -> int:
    if (n == 0):
        return 1
    return n * Fact(n - 1)


n = int(input())
print(Fact(n))
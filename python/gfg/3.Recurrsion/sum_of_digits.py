def SumOfDigits(n):
    if n <= 9:
        return n
    return n % 10 + SumOfDigits(n // 10)


n = int(input())
print(SumOfDigits(n))
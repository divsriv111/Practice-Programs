import math

def CountDigits(n) -> int:
    return math.floor((math.log10(n) + 1))


n = int(input())
print(CountDigits(n))


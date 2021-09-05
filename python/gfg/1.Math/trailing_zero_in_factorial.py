def TrailingZeroes(n) -> int:
    if (n < 0):
        return -1

    count = 0
    # Keep dividing n by
    # 5 & update Count
    while (n >= 5):
        n //= 5
        count += n

    return count


n = int(input())
print(TrailingZeroes(n))
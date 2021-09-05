def CountSetBits2(n) -> int:
    #Brain Kerringam's algorithm
    #ensure the loop runs only set bit number of times
    count = 0
    while (n > 0):
        n = (n & (n - 1))
        count += 1
    return count


def IsPowerOf2(n) -> bool:
    # numbers that are power of two have only one bit set
    # of course exclude 1 and negative part
    if n <= 1:
        return False
    return CountSetBits2(n) == 1


def IsPow2(n) -> bool:
    #Most efficient one
    if n == 0:
        return False
    return (n & (n - 1)) == 0


i = int(input())
print(IsPowerOf2(i))
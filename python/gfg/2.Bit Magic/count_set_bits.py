def CountSetBits(n) -> int:
    count = 0
    while (n > 0):
        if (n & 1) == 1:
            count += 1
        n = n >> 1
    return count


def CountSetBits2(n) -> int:
    #Brain Kerringam's algorithm
    #ensure the loop runs only set bit number of times
    count = 0
    while (n > 0):
        n = (n & (n - 1))
        count += 1
    return count


i = input()
print(CountSetBits2(int(i[0])))
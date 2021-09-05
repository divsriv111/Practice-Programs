#code
from math import sqrt, floor


def isPerfect(N):
    if (sqrt(N) - floor(sqrt(N)) != 0):
        return False
    return True


def getNearestSqrt(N):
    if N == 1:
        print(0)
        return

    aboveN = -1
    belowN = -1
    n1 = 0

    n1 = N + 1
    while (True):
        if (isPerfect(n1)):
            aboveN = n1
            break
        else:
            n1 += 1

    n1 = N - 1
    while (True):
        if (isPerfect(n1)):
            belowN = n1
            break
        else:
            n1 -= 1

    diff1 = aboveN - N
    diff2 = N - belowN

    if (diff1 > diff2):
        print(belowN)
    elif diff1 == diff2:
        print(max(aboveN, belowN))
    else:
        print(aboveN)


# t = int(input())
# for i in range(t):
#     n = int(input())
getNearestSqrt(100)
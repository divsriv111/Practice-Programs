def GCD(a, b) -> int:
    if b == 0:
        return a
    return GCD(b, b % a)


def LCM(a, b) -> int:
    #O(log(min(a,b)))
    return (a * b) // GCD(a, b)


n = input().split(' ')
print(LCM(int(n[0]), int(n[1])))
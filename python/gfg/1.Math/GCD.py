def GCD(a, b) -> int:
    #O(log(min(a,b)))
    if b == 0:
        return a
    return GCD(b, b % a)


n = input().split(' ')
print(GCD(int(n[0]), int(n[1])))
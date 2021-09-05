def PrintPrimeFafactors(n):
    #O(sqrt(n)) when number is prime
    l = []
    if n <= 1:
        return
    while n % 2 == 0:
        l.append(2)
        n = n // 2

    while n % 3 == 0:
        l.append(3)
        n = n // 3

    i = 5
    while i * i <= n:
        while n % i == 0:
            l.append(i)
            n = n // i
        while n % (i + 2) == 0:
            l.append(i + 2)
            n = n // (i + 2)
        i = i + 6
    if n > 3:
        l.append(n)

    print(l)


n = int(input())
PrintPrimeFafactors(n)
def PrintNto1(n):
    if n == 0:
        return
    print(n)
    PrintNto1(n - 1)


n = int(input())
PrintNto1(n)
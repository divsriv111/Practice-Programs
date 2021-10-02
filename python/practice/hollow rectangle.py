def hollowRectangle(m, n):
    for i in range(m):
        for j in range(n):
            if (j == 0 or j == n - 1) or (i == 0 or i == m - 1):
                print('*', end='')
            else:
                print(' ', end='')
        print()


m = int(input())
n = int(input())
hollowRectangle(m, n)

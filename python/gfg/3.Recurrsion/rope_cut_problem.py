def MaxPieces(n, a, b, c):
    if n == 0:
        return 0
    if n < 0:
        return -1
    res = max(max(MaxPieces(n - a, a, b, c), MaxPieces(n - b, a, b, c)),
              MaxPieces(n - c, a, b, c))
    if res == -1:
        return -1
    return res + 1


n = int(input())
a = int(input())
b = int(input())
c = int(input())
print(MaxPieces(n, a, b, c))

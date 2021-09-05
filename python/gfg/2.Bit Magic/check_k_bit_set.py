def CheckKSetBit(n, k) -> bool:
    op = 1 << (k - 1)
    return (op & n) == op


i = input().split(' ')
print(CheckKSetBit(int(i[0]), int(i[1])))
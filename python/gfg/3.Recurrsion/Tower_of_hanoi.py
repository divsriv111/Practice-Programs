def TOH(n, a, b, c):
    if n == 1:
        print(f"Move 1 from {a} to {b}")
        return
    TOH(n - 1, a, c, b)
    print(f"Move {n} from {a} to {c}")
    TOH(n - 1, b, a, c)


n = int(input())
TOH(n, 'A', 'B', 'C')
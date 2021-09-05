def Jos(n, k):
    # O(n)
    # assumes position starts from 0
    if n == 1:
        return 0
    else:
        return (Jos(n - 1, k) + k) % n


def MyJos(n, k):
    # call when position starts from 1
    return Jos(n, k) + 1


n = int(input())
k = int(input())
print(Jos(n, k))

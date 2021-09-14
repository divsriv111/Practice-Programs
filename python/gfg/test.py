def check(x):
    return x and (not (x & (x - 1)))


def countPairs(arr):
    cnt = 0
    prod = [x & y for x in arr for y in arr if y > x]
    print(prod)
    for x in prod:
        if x and (not (x & (x - 1))):
            cnt += 1
    return cnt


countPairs([10, 7, 2, 8, 3])

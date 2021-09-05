def generate(n):
    if n == 1:
        return [[1]]
    res = [[1], [1, 1]]
    for i in range(n - 2):
        t = []
        m = len(res)
        l = res[m - 1]
        t.append(l[0])
        for i in range(len(l) - 1):
            t.append(l[i] + l[i + 1])
        t.append(l[len(l) - 1])
        res.append(t)
    return res


n = int(input())
print(generate(n))

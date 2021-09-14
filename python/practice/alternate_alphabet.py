def fun(s):
    res = ""
    count = 0
    for i in s:
        if i.isalpha():
            if count % 2 == 0:
                res += i.upper()
            else:
                res += i
        else:
            res += i

        count += 1
    return res


s = input()
print(fun(s))

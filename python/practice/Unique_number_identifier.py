def find_special_cars(S):
    nos = S.rstrip().split(', ')
    n = 0
    for i in nos:
        no = i[9:]
        c = [i for i in no]
        c.sort()
        k = "".join(c)
        if(k == i[9:] or k[::-1] == i[9:]):
            n += 1
    return n


S = str(input())
print (find_special_cars(S))

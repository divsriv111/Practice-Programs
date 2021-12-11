def rec(n):
    if n==0:
        return 0
    else:
        return rec(n[:-1])+temp

print(rec('qwerty'))

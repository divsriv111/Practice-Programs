def parse_brackets(expression):
    open = 0
    a = ''
    for i in expression:
        if i=='(':
            open += 1
            a += str(open)
        elif i == ')':
            a += str(open)
            open -= 1
    return a

print(parse_brackets("(a + b)*(5*(c - d))"))
print(parse_brackets("(5+(t * (10 - 6))) + (8 + f)"))
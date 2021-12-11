#code
def check_odd(s):
    n=len(s)
    a=''
    for x in range(0,n,2):
        a+=s[x]
    return a==a[::-1]

def check_even(s):
    n=len(s)
    a=''
    for x in range(1,n,2):
        a+=s[x]
    return a==a[::-1]

def check_parent(s):
    return s==s[::-1]
    
test=int(input())
for _ in range(test):
    s=input()
    if check_parent(s):
        print('PARENT')
    elif check_odd(s):
        print('ODD')
    elif check_even(s):
        print('EVEN')
    else:
        print('ALIEN')

        
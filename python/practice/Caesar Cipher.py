s = input()
n = int(input())
a = ''
for i in s:
    if ord(i) in range(97,123) or ord(i) in range(65,91):
        b = ord(i) + n
        if n < 0:
            if i.isupper():
                if b not in range(65,91):
                    b = 91 - (65 - b)
            elif i.islower():
                if b not in range(97,123):
                    b = 123 - (97 - b)
        elif n > 0:
            if i.isupper():
                if b not in range(65,91):
                    b = 65 + (b - 91)
            elif i.islower():
                if b not in range(97,123):
                    b = 97 + (b - 123)
        a += chr(b)
    else:
        a += i
print(a)
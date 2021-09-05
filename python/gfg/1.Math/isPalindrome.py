def IsPalindrome(n) -> bool:
    rev = 0
    original = n
    while (n != 0):
        rev = rev * 10 + n % 10
        n = n // 10

    return rev == original


n = int(input())
print(IsPalindrome(n))
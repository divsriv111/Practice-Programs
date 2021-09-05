def IsPalindrome(s, start, end):
    if start >= end:
        return True
    return s[start] == s[end] and IsPalindrome(s, start + 1, end - 1)


s = input()
print(IsPalindrome(s, 0, len(s) - 1))

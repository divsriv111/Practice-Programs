def longestCommonPrefix(A):
    if len(A) <= 1:
        return A[0]
    stack = [i for i in A[0]]
    prefix = []
    #flag = 0
    for i in A[1:]:
        a = ''
        temp = stack.copy()
        n = min(len(i), len(temp))
        for j in range(n-1):
            if temp[j] == i[j]:
                a += temp.pop(0)
        prefix.append(a)

    print(prefix)
    print(min(prefix))


longestCommonPrefix(["abcdefgh", "aefghijk", "abcefgh"])
longestCommonPrefix(["abab", "ab", "abcd"])

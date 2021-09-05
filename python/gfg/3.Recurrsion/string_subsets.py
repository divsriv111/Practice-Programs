def Subsets(s, curr="", i=0):
    if i == len(s):
        print(curr)
        return
    Subsets(s, curr, i + 1)
    Subsets(s, curr + s[i], i + 1)
    return


s = input()
Subsets(s)
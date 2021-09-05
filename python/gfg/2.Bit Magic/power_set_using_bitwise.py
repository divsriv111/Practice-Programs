def PrintPowerSets(str):
    n = len(str)
    powSize = int(2**n)  # as power set formula is 2^n - 1
    for counter in range(powSize):
        s = ""
        for j in range(n):
            if counter & (1 << j) != 0:
                s += str[j]
        print(s)


str = input()
PrintPowerSets(str)
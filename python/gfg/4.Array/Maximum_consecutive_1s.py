def MaxOnes(arr):
    maxStreak = 0
    temp = 0
    for i in arr:
        if i == 1:
            temp += 1
            maxStreak = max(maxStreak, temp)
        else:
            temp = 0
    return maxStreak


arr = list(map(int, input().strip().split()))
print(MaxOnes(arr))

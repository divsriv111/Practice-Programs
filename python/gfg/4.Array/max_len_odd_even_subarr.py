def maxOddEven(arr):
    res = 1
    curr = 1

    for i in range(1,len(arr)):
        if (arr[i] % 2 == 0 and arr[i - 1] % 2 != 0) or (arr[i] % 2 != 0 and arr[i - 1] % 2 == 0):
            curr+=1
            res = max(res, curr)
        else:
            curr = 1
	
	return res


arr = list(map(int, input().strip().split()))
print(maxOddEven(arr))
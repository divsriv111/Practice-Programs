def subArraySum(arr, n, sum):
    curr_sum = arr[0]
    start = 0

    for i in range(1,n+1): 
        while (curr_sum > sum and start < i-1) :
            curr_sum = curr_sum - arr[start]
            start+=1

        if curr_sum == sum: 
            print(f"Sum found between indexes {start} and {i-1}"); 
            return 1 

        if i < n: 
            curr_sum = curr_sum + arr[i]

	print("No subarray found"); 
	return 0


arr = list(map(int, input().strip().split()))
sum = int(input())
print(subArraySum(arr, len(arr), sum))
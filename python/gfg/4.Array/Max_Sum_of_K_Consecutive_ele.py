def maxSum(arr, n, k):
    n = len(arr)
    curr_sum = sum(arr[:k])
    max_sum = curr_sum
    for i in range(k, n):
        curr_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, curr_sum)

    return max_sum


k = int(input())
arr = list(map(int, input().strip().split()))
print(maxSum(arr, k))

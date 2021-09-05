def CountSubsets(arr, n, sum):
    if n == 0:
        return {True: 0, False: 1}[sum == 0]
    return CountSubsets(arr, n - 1, sum) + CountSubsets(arr, n - 1, sum - arr[n - 1])


n = int(input())
arr = list(map(int, input().strip().split()))[:n]
sum = int(input())
print(CountSubsets(arr, n, sum))

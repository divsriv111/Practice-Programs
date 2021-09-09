def fillPrefixSum(arr, n):
    prefixSum = [0] * (n + 1)

    prefixSum[0] = arr[0]
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]

    return prefixSum

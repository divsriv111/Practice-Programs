def activateFountain(arr):
    n = len(arr)
    count = 1
    interval = [0]*n
    for i in range(n + 1):
        left = max(i - arr[i - 1], 1)
        right = min(i + arr[i - 1], n)

        interval[left - 1] = right

    right = interval[0]
    currMax = right
    for i in range(n):
        currMax = max(currMax, interval[i])

        if i == right:
            count += 1
            right = currMax

    return count


loc = [0, 2, 1]
print(activateFountain(loc))

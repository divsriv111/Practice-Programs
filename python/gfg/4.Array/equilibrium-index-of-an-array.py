def equilibrium(arr):
    left_sum = []
    right_sum = []

    # Iterate from 0 to len(arr)
    for i in range(len(arr)):

        # If i is not 0
        if i:
            left_sum.append(left_sum[i - 1] + arr[i])
            right_sum.append(right_sum[i - 1] + arr[len(arr) - 1 - i])
        else:
            left_sum.append(arr[i])
            right_sum.append(arr[len(arr) - 1])

    # Iterate from 0 to len(arr)
    for i in range(len(arr)):
        if left_sum[i] == right_sum[len(arr) - 1 - i]:
            return i

    # If no equilibrium index found,then return -1
    return -1


arr = list(map(int, input().strip().split()))
print(equilibrium(arr))

def Leaders(arr):
    curr_leader = arr[-1]
    print(curr_leader, end=" ")
    n = len(arr)
    i = n - 2
    while i >= 0:
        if curr_leader < arr[i]:
            curr_leader = arr[i]
            print(curr_leader, end=" ")
        i -= 1


arr = list(map(int, input().strip().split()))
Leaders(arr)

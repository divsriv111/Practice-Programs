def Median(A, B):
    # Assumption both A and B cannot be empty
    n = len(A)
    m = len(B)
    if (n > m):
        return Median(B, A)  # Swapping to make A smaller

    start = 0
    end = n
    realmidinmergedarray = (n + m + 1) // 2

    while (start <= end):
        mid = (start + end) // 2
        leftAsize = mid
        leftBsize = realmidinmergedarray - mid

        # checking overflow of indices
        leftA = A[leftAsize - 1] if (leftAsize > 0) else float('-inf')
        leftB = B[leftAsize - 1] if (leftBsize > 0) else float('-inf')
        rightA = A[leftAsize] if (leftAsize < n) else float('inf')
        rightB = A[leftAsize] if (leftBsize < m) else float('inf')

        # if correct partition is done
        if leftA <= rightB and leftB <= rightA:
            if ((m + n) % 2 == 0):
                return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
            return max(leftA, leftB)

        elif (leftA > rightB):
            end = mid - 1
        else:
            start = mid + 1


arr1 = [-5, 3, 6, 12, 15]
arr2 = [-12, -10, -6, -3, 4, 10]
print("Median of the two arrays is {}".format(Median(arr1, arr2)))
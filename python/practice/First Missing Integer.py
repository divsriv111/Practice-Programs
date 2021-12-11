def firstMissingPositive(A):
    count = 1
    A.sort()
    for i in A:
        if i <= 0:
            continue
        if count != i:
            return count
        else:
            count += 1

    return count


print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([-8, -7, -6]))
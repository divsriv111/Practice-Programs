def GetMissingElement(a) -> int:
    x1 = a[0]
    x2 = 1
    n = len(a)
    for i in range(1, n):
        x1 = x1 ^ a[i]

    for i in range(2, n + 2):
        x2 = x2 ^ i

    return x1 ^ x2


# number of elements
n = int(input("Enter number of elements : "))
#[1,2,3,4,6]
# Below line read inputs from user using map() function
arr = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

print(GetMissingElement(arr))  #5

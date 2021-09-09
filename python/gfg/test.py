C = 100
n = 3
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(n):
    for j in range(n):

        Temp = A[i][j] + C
        A[i][j] = A[j][i]
        A[j][i] = Temp - C

for i in range(n):
    for j in range(n):
        print(A[i][j], end=" ")
    print("\n")

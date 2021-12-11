import numpy as np
from collections import defaultdict

def setZeroes(A):
    #A = np.array(A)
    B = np.array(A.copy())
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                B[:,j] = 0
                B[i] = 0
    return B.tolist()

print(setZeroes([[1,0,1],[1,1,1],[1,1,1]]))


"""
A = 
        m = len(A)
        n = len(A[0])
        cols = []
        for i in range(m):
            temp = 0
            for j in range(n):
                if temp == 1:
                    continue
                if A[i][j] == 0:
                    A[i] = [0] * n
                    cols.append(j)
                    temp = 1
        for i in range(m):
            for k in cols:
                A[i][k] = 0

        return A
"""
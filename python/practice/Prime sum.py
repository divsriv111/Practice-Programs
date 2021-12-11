import math
def generatePrime(l,h):
    for num in range(l, h + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                return(num)
def primesum(A):
    if A==2:
        return [1,1]
    #arr = []
    for num in range(2,int(math.sqrt(A))+1):
       temp = generatePrime(num,int(math.sqrt(A)))
       if (2+temp) == A:
           return [2,temp]

print(primesum(56))
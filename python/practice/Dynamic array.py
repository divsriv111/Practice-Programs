from sys import stdin, stdout
stdin = open('in', 'r')
stdout = open('out', 'w')

def dynamicArray(n, queries):
    # Write your code here
    result = []
    seqList = {}
    lastAnswer = 0
    for i in range(len(queries)):
        query_type = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        key_index = (x ^ lastAnswer) % n
        if(query_type == 1):
            if(key_index in seqList):
                seqList[key_index].append(y)
            else:
                seqList[key_index] = [y]
        else:
            lastAnswer = seqList[key_index][y % len(seqList[key_index])]
            result.append(lastAnswer)
    return result
        

first_multiple_input = stdin.readline().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])


queries = []

for _ in range(q):
    queries.append(list(map(int, stdin.readline().rstrip().split())))

stdout.write(str(dynamicArray(n, queries)))
#result = dynamicArray(n, queries)

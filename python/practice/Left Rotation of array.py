from sys import stdin, stdout
stdin = open('in', 'r')
stdout = open('out', 'w')


def left_rotate(arr, d):
    for _ in range(d):
        first = arr[0]
        for i in range(len(arr)-1):
            arr[i] = arr[i+1]
        arr[len(arr) - 1] = first
    
    print(' '.join(map(str,arr)))
           # original_index = i
           # new_index = i - d
           # if(new_index < 0):
           #     new_index = len(arr) + new_index
           # stdout.write(str(new_index)+' ')

           # print(arr)

           # arr[original_index] = arr[original_index] + arr[new_index]
           # arr[new_index] = arr[original_index] - arr[new_index]
           # arr[original_index] = arr[original_index] - arr[new_index]


if __name__ == '__main__':
    nd = stdin.readline().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, stdin.readline().rstrip().split()))

    left_rotate(a, d)

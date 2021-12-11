# from sys import stdin, stdout
# stdin = open('in', 'r')
# stdout = open('out', 'w')

n,m=map(int,input().split())
ch=[0 for _ in range(n+2)]
for _ in range(m):
    a,b,k=map(int,input().split())
    ch[a]+=k
    ch[b+1]-=k
v=0
m=0
for i in range(1,n+1):
    v+=ch[i]
    m=max(m,v)
print(m)
N=int(input())
a=[*map(int,input().split())]
S=[]
r=[-1]*N
for i in range(N):
 while S and a[S[-1]]<a[i]:r[S.pop()]=a[i]
 S.append(i)
print(*r)
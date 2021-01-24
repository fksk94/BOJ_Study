from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
dx = [input().rstrip() for i in range(N)]
bx = [input().rstrip() for i in range(M)]
dx.sort()
bx.sort()
j = 0
res = []
for i in range(N):
    while j < M:
        if sorted([bx[j], dx[i]])[1] != dx[i]:
            break
        if dx[i] == bx[j]:
            res.append(dx[i])
            break
        j+=1
print(len(res))
for i in res:
    print(i)
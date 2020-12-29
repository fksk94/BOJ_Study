from sys import stdin

input = stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
result = []
cnt = 1
i = 0
S = []

while i < N:
    if S and S[-1] == arr[i]:
        S.pop()
        i += 1
        result.append('-')
    else:
        S.append(cnt)
        cnt += 1
        result.append('+')
        if cnt > N+1:
            break
if len(result) == 2*N:
    for i in result:
        print(i)
else:
    print('NO')


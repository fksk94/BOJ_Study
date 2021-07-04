from sys import stdin
input = stdin.readline

N = int(input())
arr = [input().rstrip() for i in range(N)]
visit = [[False] * N for i in range(N)]
dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def dfs(x, y):
    S = [(x, y)]
    visit[x][y] = True
    cnt = 1
    while S:
        n, m = S.pop()
        for i in range(4):
            rn = n + dxy[i][1]
            rm = m + dxy[i][0]
            if 0 <= rm < N and 0 <= rn < N and visit[rn][rm] == False and arr[rn][rm] == '1':
                S.append((rn, rm))
                visit[rn][rm] = True
                cnt += 1
    return cnt

ans = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visit[i][j] == False:
            ans.append(dfs(i, j))
ans.sort()
print(len(ans))
for i in ans:
    print(i)
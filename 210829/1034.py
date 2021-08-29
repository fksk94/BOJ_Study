from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
k = int(input())

cnt = 0
if k % 2 == 0:
    for j in range(N):
        tmp_cnt = 0
        for jj in range(M):
            if arr[j][jj] == 1:
                tmp_cnt += 1
        if tmp_cnt == M:
            cnt += 1

res = cnt
for i in range(N):
    check = []
    cnt = 0
    limit_k = k
    for j in range(M):
        if arr[i][j] == 0:
            if limit_k == 0:
                limit_k -= 1
                break
            check.append(j)
            limit_k -= 1
    if limit_k == -1:
        continue
    if len(check) % 2 == k % 2:
        for j in range(N):
            tmp_cnt = 0
            for jj in range(M):
                if jj in check:
                    if arr[j][jj] != 1:
                        tmp_cnt += 1
                else:
                    if arr[j][jj] == 1:
                        tmp_cnt += 1
            if tmp_cnt == M:
                cnt += 1

    res = max(res, cnt)

print(res)
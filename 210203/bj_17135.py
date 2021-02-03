from itertools import combinations

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(N)]
loc = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            loc.append([i, j])
loc.sort(key=lambda x:x[1])
init = [loc[i][:] for i in range(len(loc))]

ans = []

for com in combinations(range(M), 3):
    loc = [init[i][:] for i in range(len(init))]
    cnt = 0
    while loc:
        get = set()
        for comx in com:
            check = False
            for i in range(1, D+1):
                for x in range(len(loc)):
                    if abs(loc[x][0]-N) + abs(loc[x][1]-comx) <= i:
                        get.add(x)
                        check = True
                        break
                if check:
                    break
        get_res = sorted(list(get), reverse=True)
        for i in get_res:
            loc.pop(i)
            cnt += 1
        get_res = []
        for i in range(len(loc)-1, -1, -1):
            loc[i][0] += 1
            if loc[i][0] == N:
                get_res.append(i)
        for i in get_res:
            loc.pop(i)
    ans.append(cnt)
print(max(ans))

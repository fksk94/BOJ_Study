from itertools import combinations

def bfs_com(x, cnt):
    global res1
    Q = connect.get(x)[:]
    while Q:
        tmpp = Q.pop()
        if visited[tmpp] and tmpp in com:
            visited[tmpp] = False
            Q.extend(connect.get(tmpp))
            cnt += arr[tmpp]
    if visited.count(False) == len(com):
        res1 = cnt

def bfs_tmp(x, cnt):
    global res2
    Q = connect.get(x)[:]
    while Q:
        tmpp = Q.pop()
        if visited[tmpp] and tmpp in tmp:
            visited[tmpp] = False
            Q.extend(connect.get(tmpp))
            cnt += arr[tmpp]
    if visited.count(False) == len(tmp):
        res2 = cnt

N = int(input())
arr = [0] + list(map(int, input().split()))
connect = dict()
for i in range(1, N+1):
    connect[i] = list(map(int, input().split()))[1:]

res = []

for i in range(1, N//2+1):
    for com in combinations(range(1, N+1), i):
        tmp = list(set(range(1, N+1))-set(com))
        res1, res2 = -1, -1
        visited = [True] * (N+1)
        visited[com[0]] = False
        bfs_com(com[0], arr[com[0]])
        visited = [True] * (N+1)
        visited[tmp[0]] = False
        bfs_tmp(tmp[0], arr[tmp[0]])
        if res1 != -1 and res2 != -1:
            res.append(abs(res1-res2))

if res:
    print(min(res))
else:
    print(-1)


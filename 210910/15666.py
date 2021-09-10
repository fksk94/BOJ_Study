from sys import stdin, setrecursionlimit
setrecursionlimit(2000000)
input = stdin.readline

def dfs(s):
    if len(res_item) == M:
        res.add(tuple(res_item))
        return
    for i in range(s, N):
        res_item.append(arr[i])
        dfs(i)
        res_item.pop()

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = set()
for i in range(N):
    res_item = [arr[i]]
    dfs(i)
for r in sorted(list(res)):
    print(*r)
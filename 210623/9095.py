from sys import stdin
input = stdin.readline

def dfs(cnt):
    global res
    if cnt >= x:
        if x == cnt:
            res += 1
        return
    for i in range(1, 4):
        dfs(cnt + i)
N = int(input())
for _ in range(N):
    x = int(input())
    res = 0
    dfs(0)
    print(res)
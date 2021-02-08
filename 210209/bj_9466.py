from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(300000)

def dfs(x, c):
    if check[x] == c:
        return re_dfs(x)
    elif check[x] == 0:
        check[x] = c
        return dfs(arr[x], c)

def re_dfs(x):
    if check[x] == -1:
        return
    check[x] = -1
    return re_dfs(arr[x])


T = int(input())
for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    check = [0] * (N+1)

    for i in range(1, N+1):
        if check[i] == 0:
            dfs(i, i)
    print(N-check.count(-1))
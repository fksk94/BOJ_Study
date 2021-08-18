from sys import stdin, setrecursionlimit
setrecursionlimit(200000)
input = stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
hi = []
def dfs(hi, s, cnt):
    if cnt == M:
        print(" ".join(hi))
        return
    for i in range(s, N):
        hi.append(str(arr[i]))
        dfs(hi, i, cnt + 1)
        hi.pop()

dfs(hi, 0, 0)
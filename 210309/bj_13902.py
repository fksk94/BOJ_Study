from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(200000)

def dpdp():
    for i in range(N + 1):
        for j in range(len(knap)):
            if i - knap[j] > -1:
                dp[i] = min(dp[i], dp[i-knap[j]]+1)
    print(dp[N])

N, M = map(int, input().split())
arr = list(map(int, input().split()))

knap = set(arr)
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        knap.add(arr[i]+arr[j])
knap = sorted(list(knap), reverse=True)
dp = [float('INF')] * (N+1)
dp[0] = 0
dpdp()
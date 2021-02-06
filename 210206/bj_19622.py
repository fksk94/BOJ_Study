from sys import stdin
import bisect
input = stdin.readline


N = int(input())
arr = [tuple(map(int, input().split())) for i in range(N)]
arr.sort(key=lambda x:x[1])
dp1 = [float('inf')] * (10**5)
dp2 = [float('inf')] * (10**5)

dp1[0] = arr[0][2]
dp2[0] = arr[0][1]

for i in range(1, N):
    tmp = bisect.bisect_left(dp2, arr[i][0]) - 1
    # 첫번째 값
    val1 = arr[i][2]
    if tmp >= 0:
        val1 = dp1[tmp] + arr[i][2]
    # 두번째 값
    val2 = dp1[i-1]
    dp1[i] = max(val1, val2)
    dp2[i] = arr[i][1]

print(dp1[N-1])
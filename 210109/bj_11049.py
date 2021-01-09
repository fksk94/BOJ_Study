def cal(a, b, c):
    # print(a * b * c)
    return a * b * c

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
dp = [[0]*500] + [[float('inf')]*500 for i in range(499)]

# dp 세로 축 돌기
for j in range(N):
    # dp 세로 까지 한번 더 돌기
    for i in range(j):
        # dp 가로축 돌기
        for z in range(N - j):
            dp[j][z] = min(dp[j][z], dp[j-i-1][z] + dp[i][z+j-i] + cal(arr[z][0], arr[z + j - i - 1][1], arr[z+j][1]))
print(dp[N-1][0])
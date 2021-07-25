from sys import stdin
input = stdin.readline

N = int(input())
for _ in range(N):
    M = int(input())
    sticker = [list(map(int, input().split())) for i in range(2)]
    if M == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue
    dp = [[0] * len(sticker[0]) for i in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    dp[0][1] = sticker[0][1] + sticker[1][0]
    dp[1][1] = sticker[1][1] + sticker[0][0]
    for i in range(2, len(dp[0])):
        for j in range(2):
            dp[j][i] = max(dp[j^1][i-1], dp[j][i-2], dp[j^1][i-2]) + sticker[j][i]
    last = len(dp[0])-1
    print(max(dp[0][last], dp[1][last], dp[0][last-1], dp[1][last-1]))
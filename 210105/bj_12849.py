from sys import stdin
input = stdin.readline

N = int(input())
dic = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 4, 5],
    4: [2, 3, 5, 6],
    5: [3, 4, 6, 7],
    6: [4, 5, 8],
    7: [5, 8],
    8: [6, 7]
}

dp = [0] * 9
dp[2] = 1
dp[3] = 1
for i in range(2, N+1):
    tmp = [0] * 9
    for j in range(1, 9):
        tmp[j] = sum([dp[x] for x in dic[j]])%1000000007
    dp = tmp
print(dp[1]%1000000007)

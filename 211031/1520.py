from sys import setrecursionlimit
setrecursionlimit(1000000)

a, b = map(int, input().split())
road = [list(map(int, input().split())) for i in range(a)]
dp = [[0] * b for i in range(a)]
visit = [[False] * b for i in range(a)]
dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    if visit[x][y] ==True:
        return dp[x][y]
    if x == a-1 and y == b-1:
        return 1
    visit[x][y] = True
    for dx, dy in dxy:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < a and 0 <= ny < b and road[nx][ny] < road[x][y]:
            dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(0,0))
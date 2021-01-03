from sys import stdin

def find(x, y, z):
    if x < 1 or y < 1 or z < 1:
        return 1
    if x > 20 or y > 20 or z > 20:
        return find(20, 20, 20)
    if dp[x][y][z] != float('inf'):
        return dp[x][y][z]
    if x < y and y < z:
        tmp = find(x, y, z-1) + find(x, y-1, z-1) - find(x, y-1, z)
        dp[x][y][z] = tmp
        return tmp
    else:
        tmp = find(x-1, y, z) + find(x-1, y-1, z) + find(x-1, y, z-1) - find(x-1, y-1, z-1)
        dp[x][y][z] = tmp
        return tmp

input = stdin.readline
dp = [[[float('inf')] * 21 for i in range(21)] for j in range(21)]
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a, b, c, find(a, b, c)))
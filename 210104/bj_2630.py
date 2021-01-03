from sys import stdin
import sys
input = stdin.readline
sys.setrecursionlimit(100000)

def find(sx, sy, ex, ey):
    check = arr[sx][sy]
    for i in range(sx, ex):
        for j in range(sy, ey):
            if arr[i][j] != check:
                find(sx, sy, sx + (ex-sx)//2, sy + (ey-sy)//2)
                find((sx + ex)//2, (ey+ sy)//2, ex, ey)
                find((sx + ex)//2, sy, ex, (sy + ey)//2)
                find(sx, (sy + ey)//2, (ex + sx)//2, ey)
                return
    if check:
        res[1] += 1
    else:
        res[0] += 1


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
res = [0, 0]
find(0, 0, N, N)
print(res[0])
print(res[1])
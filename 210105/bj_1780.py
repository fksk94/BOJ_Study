from sys import stdin
import sys
input = stdin.readline
sys.setrecursionlimit(100000)

def find(sx, sy, ex, ey):
    check = arr[sx][sy]
    for i in range(sx, ex):
        for j in range(sy, ey):
            if arr[i][j] != check:
                for x in range(3):
                    for y in range(3):
                        find(sx + (ex-sx)//3 * x, sy + (ey-sy)//3 * y, sx + (ex-sx)//3 * (x+1), sy + (ey-sy)//3 * (y+1))
                return
    if check == 1:
        res[1] += 1
    elif check == 0:
        res[0] += 1
    else:
        res[-1] += 1


N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
res = [0, 0, 0]
find(0, 0, N, N)
print(res[-1])
print(res[0])
print(res[1])
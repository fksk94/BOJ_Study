from sys import stdin
import sys
input = stdin.readline
sys.setrecursionlimit(100000)

def find(sx, sy, ex, ey):
    check = arr[sx][sy]
    for i in range(sx, ex):
        for j in range(sy, ey):
            if arr[i][j] != check:
                ans.append('(')
                find(sx, sy, sx + (ex-sx)//2, sy + (ey-sy)//2)
                while res:
                    ans.append(res.pop())
                find(sx, (sy + ey)//2, (ex + sx)//2, ey)
                while res:
                    ans.append(res.pop())
                find((sx + ex)//2, sy, ex, (sy + ey)//2)
                while res:
                    ans.append(res.pop())
                find((sx + ex)//2, (ey+ sy)//2, ex, ey)
                while res:
                    ans.append(res.pop())
                ans.append(')')
                return
    res.append(check)

N = int(input())
arr = [list(map(int, list(input().rstrip()))) for i in range(N)]
res = []
ans = []
find(0, 0, N, N)
while res:
    ans.append(res.pop())
for i in range(len(ans)):
    print(ans[i], end='')
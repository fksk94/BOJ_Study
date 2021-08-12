from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
begin = [list(input().rstrip()) for i in range(n)]
end = [list(input().rstrip()) for i in range(n)]
visit = [[False] * m for i in range(n)]
res = 0

chh = False
for i in range(n):
    for j in range(m):
        if begin[i][j] == end[i][j]:
            continue
        else:
            chh = True
            break
    if chh:
        break
else:
    print(res)
if chh:
    if n < 3 or m < 3:
        print(-1)
    else:
        for i in range(n-2):
            for j in range(m-2):
                if begin[i][j] != end[i][j]:
                    res += 1
                    for ri in range(i, i+3):
                        for rj in range(j, j + 3):
                            if begin[ri][rj] == "0":
                                begin[ri][rj] = "1"
                            else:
                                begin[ri][rj] = "0"
        ch = False
        for i in range(n):
            for j in range(m):
                if begin[i][j] == end[i][j]:
                    continue
                else:
                    print(-1)
                    ch = True
                    break
            if ch:
                break
        else:
            print(res)
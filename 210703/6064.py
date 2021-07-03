from sys import stdin
input = stdin.readline

N = int(input())
for i in range(N):
    a, b, c, d = map(int, input().split())
    cnt = 0
    if a % 2 == 0 and b % 2 == 0:
        if c % 2 != d % 2:
            print(-1)
            continue
    if a > b:
        s = c - d
        ch = False
        while s:
            s = (s - b) % a
            cnt += 1
            if cnt > 40002:
                ch = True
                print(-1)
                break
        if ch == False:
            print(b * cnt + d)
    else:
        s = d - c
        ch = False
        while s:
            s = (s - a) % b
            cnt += 1
            if cnt > 40002:
                ch = True
                print(-1)
                break
        if ch == False:
            print(a*cnt + c)
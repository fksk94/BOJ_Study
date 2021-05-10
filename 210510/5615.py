from sys import stdin
input = stdin.readline

N = int(input())
cnt = 0
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
a = [2, 3, 5, 7, 11]
for _ in range(N):
    n = (int(input())*2)+1
    if n < 9:
        cnt += 1
        continue
    if n < 38:
        if n in prime:
            cnt += 1
            continue
    for i in a:
        d = n - 1
        ch = False
        while d % 2 == 0:
            if pow(i, d, n) == n - 1:
                ch = True
            d //= 2
        tmp = pow(i, d, n)
        if tmp == 1 or tmp == n-1:
            ch = True
        if not ch:
            break
    else:
        cnt += 1

print(cnt)
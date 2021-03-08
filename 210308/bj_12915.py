from sys import stdin
input = stdin.readline

a, b, c, d, e = map(int, input().split())

ans = 0
while True:
    if c > 0:
        c -= 1
    elif b > 0 and d > 0:
        if a + b >= d + e:
            b -= 1
        else:
            d -= 1
    elif b > 0:
        b -= 1
    elif d > 0:
        d -= 1
    else:
        break

    if a > 0:
        a -= 1
    elif b > 0:
        b -= 1
    else:
        break

    if e > 0:
        e -= 1
    elif d > 0:
        d -= 1
    else:
        break

    ans += 1
print(ans)
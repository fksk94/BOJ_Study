from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
res = 0
res2 = 0

tmp = N
i = 1
while True:
    if tmp // 2**i:
        res2 += tmp // 2**i
        i += 1
    else:
        break
i = 1
while True:
    if tmp // 5**i:
        res += tmp // 5**i
        i += 1
    else:
        break

tmp = M
i = 1
while True:
    if tmp // 2**i:
        res2 -= tmp // 2**i
        i += 1
    else:
        break
i = 1
while True:
    if tmp // 5**i:
        res -= tmp // 5**i
        i += 1
    else:
        break

tmp = N - M
i = 1
while True:
    if tmp // 2**i:
        res2 -= tmp // 2**i
        i += 1
    else:
        break
i = 1
while True:
    if tmp // 5**i:
        res -= tmp // 5**i
        i += 1
    else:
        break

print(min(res, res2))
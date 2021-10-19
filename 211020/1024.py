from sys import stdin

input = stdin.readline

n, m = map(int, input().split())

for i in range(m, 101):
    e = n // i + int(i / 2)
    s = e - i + 1
    if s < 0:
        continue
    if e > n:
        continue
    if n * 2 == e*(e + 1) - s*(s - 1):
        print(*range(s, e+1))
        break
else:
    print(-1)
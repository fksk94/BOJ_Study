from sys import stdin
input = stdin.readline

N = int(input())
res = 0
for i in range(1, N+1):
    n = i
    while n % 5 == 0:
        n //= 5
        res += 1
print(res)
from sys import stdin
import math
input = stdin.readline

modx = 1000000007

def sqrt_mul(x, n):
    if n == 1:
        return x
    if n == 0:
        return 1
    if n % 2:
        return (x * sqrt_mul(x, n - 1)) % 1000000007
    else:
        tmp = sqrt_mul(x, n // 2)
        return ((tmp % 1000000007) * (tmp % 1000000007)) % 1000000007


T = int(input())
ans = 0
for _ in range(T):
    N, s = map(int, input().split())
    gcd = math.gcd(N, s)
    N //= gcd
    s //= gcd
    X = sqrt_mul(N, 1000000005) % 1000000007
    ans += (s * X) % modx
    ans %= modx
print(ans)
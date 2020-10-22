def factorial(n):
    if n == 0:
        return 1
    for i in range(n-1, 1, -1):
        n = (n*i)%1000000007
    return n

def pow(n, d):
    if d == 0:
        return 1
    elif d % 2:
        return (pow(n, d//2) ** 2 * n) %1000000007
    else:
        return (pow(n, d//2) ** 2) %1000000007

N, M = map(int, input().split())
print((factorial(N)* pow(factorial(N-M), 1000000005) * pow(factorial(M), 1000000005))%1000000007)
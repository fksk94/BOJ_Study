def factorial(n):
    if n == 0:
        return 1
    for i in range(n-1, 1, -1):
        n = (n*i)%K
    return n

def pow(n, d):
    if d == 0:
        return 1
    elif d % 2:
        return (pow(n, d//2) ** 2 * n) %K
    else:
        return (pow(n, d//2) ** 2) %K

N, M, K = map(int, input().split())
Narr = []
Marr = []
arr = []
res = 1
while True:
    a, b = divmod(N, K)
    c, d = divmod(M, K)
    Narr.append(b)
    Marr.append(d)
    N = a
    M = c
    if a == 0:
        break
while Narr:
    N = Narr.pop()
    M = Marr.pop()
    if N < M:
        print(0)
        break
    else:
        arr.append((factorial(N)* pow(factorial(N-M), K-2) * pow(factorial(M), K-2))%K)
else:
    for i in arr:
        res = res * i
    print(res%K)
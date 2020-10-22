def pow(n, m):
    if m == 0:
        return 1
    elif m % 2:
        tmp = pow(n, m // 2)
        return tmp * tmp * n % K
    else:
        tmp = pow(n, m // 2)
        return tmp * tmp % K

N, M, K= map(int, input().split())
print(pow(N,M))
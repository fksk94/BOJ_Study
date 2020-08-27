def fibo2(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
        f[i] = f[i] % 1000000007
    return f[n]


s = int(input())
print(fibo2(s))
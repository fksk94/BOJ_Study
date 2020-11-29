def sol():
    N, L, W, H = map(int, input().split())
    s = 0
    e = min(L, W, H)
    for i in range(10000):
        a = (e + s) / 2
        if (L // a) * (W // a) * (H // a) >= N:
            s = a
        else:
            e = a

    print(round(a, 10))
sol()
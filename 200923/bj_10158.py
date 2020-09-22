def solution():
    N, M = map(int, input().split())
    x, y = map(int, input().split())
    t = int(input())
    tx = t%(N*2)
    ty = t%(M*2)
    dx, dy = 1, 1
    while tx > 0:
        tx -= 1
        if x == N:
            dx = -1
        if x == 0:
            dx = 1
        x += dx
    while ty > 0:
        ty -= 1
        if y == 0:
            dy = 1
        if y == M:
            dy = -1
        y += dy
    print(x, y)
solution()
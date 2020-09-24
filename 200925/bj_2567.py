def solution():
    def check(x, y):
        count = 0
        if x+1 == 101:
            if paper[x][y] == 1:
                count += 1
        elif paper[x + 1][y] == 0 and paper[x][y] == 1:
            count += 1

        if x-1 == 0:
            if paper[x][y] == 1:
                count += 1
        elif paper[x - 1][y] == 0 and paper[x][y] == 1:
            count += 1

        if y+1 == 101:
            if paper[x][y] == 1:
                count += 1
        elif paper[x][y + 1] == 0 and paper[x][y] == 1:
            count += 1

        if y-1 == 0:
            if paper[x][y] == 1:
                count += 1
        elif paper[x][y - 1] == 0 and paper[x][y] == 1:
            count += 1

        return count

    T = int(input())
    cnt = 0
    paper = [[False]*101 for i in range(101)]
    for i in range(1, T+1):
        a, b = map(int, input().split())
        for k in range(a, a+10):
            for m in range(b, b+10):
                paper[k][m] = True
    for i in range(1, 101):
        for j in range(1, 101):
            cnt += check(i,j)
    print(cnt)
solution()
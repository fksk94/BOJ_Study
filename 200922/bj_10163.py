def solution():
    T = int(input())
    paper = [[False]*101 for i in range(101)]
    for i in range(1, T+1):
        a, b, c, d = map(int, input().split())
        for k in range(a, a+c):
            for m in range(b, b+d):
                paper[k][m] = i
    for j in range(1, T+1):
        print(sum([i.count(j) for i in paper]))
solution()
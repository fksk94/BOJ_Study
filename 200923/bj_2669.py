def solution():
    paper = [[False]*101 for i in range(101)]
    for i in range(1, 5):
        a, b, c, d = map(int, input().split())
        for k in range(a, c):
            for m in range(b, d):
                paper[k][m] = True
    print(sum([i.count(True) for i in paper]))
solution()
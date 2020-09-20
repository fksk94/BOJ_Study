def solution():
    T = int(input())
    paper = [[False]*100 for i in range(100)]
    for i in range(T):
        a, b = map(int, input().split())
        for k in range(a, a+10):
            for m in range(b, b+10):
                paper[k][m] = True
    print(sum([sum(i) for i in paper]))
solution()
import sys
def solution():
    N = int(sys.stdin.readline())
    T = int(sys.stdin.readline())
    for _ in range(1, T+1):
        X, Y = map(int, sys.stdin.readline().split())
        if (N // 2 + 1) < X:
            X = N - X + 1
        if (N // 2 + 1) < Y:
            Y = N - Y + 1
        if X <= Y :
            if X%3 == 0:
                print(3)
            else:
                print(X % 3)
        else:
            if Y % 3 == 0:
                print(3)
            else:
                print(Y % 3)
solution()
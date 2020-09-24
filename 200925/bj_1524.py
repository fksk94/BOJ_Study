import sys

def solution():
    def check():
        if not S:
            res.append('B')
            return
        if not B:
            res.append('S')
            return
        if S[0] >= B[0]:
            B.pop(0)
            return
        else:
            S.pop(0)
            return
    T = int(sys.stdin.readline())
    for _ in range(T):
        input()
        res = []
        a, b = list(map(int, sys.stdin.readline().split()))
        if a > 1 and b > 1:
            S = sorted(list(map(int, input().split())))
            B = sorted(list(map(int, input().split())))
            while not res:
                check()
            print(res[0])
        elif a == 0 and b == 0:
            print('C')
        elif a == 0:
            print("B")
        elif b == 0 :
            print("S")
        elif a == 1 and b == 1:
            S = [int(input())]
            B = [int(input())]
            while not res:
                check()
            print(res[0])
        elif a == 1 and b > 1:
            S = [int(input())]
            B = sorted(list(map(int, input().split())))
            while not res:
                check()
            print(res[0])
        elif b == 1 and a > 1:
            S = sorted(list(map(int, input().split())))
            B = [int(input())]
            while not res:
                check()
            print(res[0])
solution()
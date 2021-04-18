from sys import stdin
input = stdin.readline
import sys
sys.setrecursionlimit(200000)

R, C, M = map(int, input().split())
arr = [[(-1, -1, -1)] * (C+1) for i in range(R+1)]
sharks = [list(map(int, input().split())) for i in range(M)]
ans = 0
sharks.sort(key=lambda x: x[0], reverse=True)
sharks.sort(key=lambda x: x[1], reverse=True)
for i in range(1, C+1):
    for j in range(len(sharks)-1, -1, -1):
        if sharks[j][1] == i:
            ans += sharks[j][4]
            sharks.pop(j)
            break
        elif sharks[j][1] > i:
            break

    for j in range(len(sharks)):
        if sharks[j][3] == 1:
            sharks[j][0] -= sharks[j][2]
            if sharks[j][0] < 1:
                ch = False
            else:
                ch = True
            while True:
                if sharks[j][0] < 1:
                    ch = False
                    sharks[j][0] = abs(sharks[j][0]) + 2
                elif sharks[j][0] > R:
                    ch = True
                    sharks[j][0] = R - (sharks[j][0] - R)
                else:
                    if ch:
                        sharks[j][3] = 1
                    else:
                        sharks[j][3] = 2
                    break
        elif sharks[j][3] == 2:
            sharks[j][0] += sharks[j][2]
            if sharks[j][0] > R:
                ch = False
            else:
                ch = True
            while True:
                if sharks[j][0] < 1:
                    ch = True
                    sharks[j][0] = abs(sharks[j][0]) + 2
                elif sharks[j][0] > R:
                    ch = False
                    sharks[j][0] = R - (sharks[j][0] - R)
                else:
                    if ch:
                        sharks[j][3] = 2
                    else:
                        sharks[j][3] = 1
                    break
        elif sharks[j][3] == 3:
            sharks[j][1] += sharks[j][2]
            if sharks[j][1] > C:
                ch = False
            else:
                ch = True
            while True:
                if sharks[j][1] < 1:
                    ch = True
                    sharks[j][1] = abs(sharks[j][1]) + 2
                elif sharks[j][1] > C:
                    ch = False
                    sharks[j][1] = C - (sharks[j][1] - C)
                else:
                    if ch:
                        sharks[j][3] = 3
                    else:
                        sharks[j][3] = 4
                    break
        else:
            sharks[j][1] -= sharks[j][2]
            if sharks[j][1] < 1:
                ch = False
            else:
                ch = True
            while True:
                if sharks[j][1] < 1:
                    ch = False
                    sharks[j][1] = abs(sharks[j][1]) + 2
                elif sharks[j][1] > C:
                    ch = True
                    sharks[j][1] = C - (sharks[j][1] - C)
                else:
                    if ch:
                        sharks[j][3] = 4
                    else:
                        sharks[j][3] = 3
                    break
    sharks.sort(key=lambda x: x[0], reverse=True)
    sharks.sort(key=lambda x: x[1], reverse=True)
    for j in range(len(sharks) - 1, 0, -1):
        if sharks[j][0] == sharks[j-1][0] and sharks[j][1] == sharks[j-1][1]:
            if sharks[j][4] > sharks[j-1][4]:
                sharks.pop(j-1)
            else:
                sharks.pop(j)
print(ans)
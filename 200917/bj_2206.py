from copy import deepcopy
from collections import deque

def solution():
    def go(N, M, start, cnt):
        for i in range(4):
            rx = start[0] + dx[i]
            ry = start[1] + dy[i]
            if rx == N-1 and ry == M-1:
                result.append(cnt)
                return

            if  N > rx > -1 and M > ry > -1:
                if start[2] == 0:
                    if all[start[2]][rx][ry] == 0:
                        visit_plan.append((rx, ry, start[2]))
                        all[start[2]][rx][ry] = 1
                        all[start[2] + 1][rx][ry] = 1
                    else:
                        visit_plan.append((rx, ry, start[2]+1))
                if start[2] == 1:
                    if all[start[2]][rx][ry] == 0:
                        visit_plan.append((rx, ry, start[2]))
                        all[start[2]][rx][ry] = 1

    n, m = map(int, input().split())
    arr = [[int(j) for j in input()] for i in range(n)]
    another = deepcopy(arr)
    all = [arr, another]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    result = []
    cnt = 1
    visit_plan = deque([(0, 0, 0)])
    all[0][0][0] = 1
    all[1][0][0] = 1
    if n == 1 and m == 1:
        print(1)
    else:
        while visit_plan :
            cnt += 1
            # print(visit_plan)
            for _ in range(len(visit_plan)):
                go(n, m, visit_plan.popleft(), cnt)
                if result :
                    print(result[0])
                    break
            if result:
                break
        else :
            print("-1")
solution()
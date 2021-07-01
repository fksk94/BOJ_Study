from collections import deque
from sys import stdin
input = stdin.readline

def dslr(x):
    Q = deque([(x, "")])
    while Q:
        nx, res = Q.popleft()
        if nx == b:
            return res
        if visit[nx]:
            continue
        visit[nx] = True
        ne = (nx*2)%10000
        if visit[ne] == False:
            Q.append((ne, res + "D"))
        ne = (nx - 1) % 10000
        if visit[ne] == False:
            Q.append((ne, res + "S"))
        ne = ((nx * 10) % 10000) + nx //1000
        if visit[ne] == False:
            Q.append((ne, res + "L"))
        ne = ((nx % 10) * 1000) + (nx // 10)
        if visit[ne] == False:
            Q.append((ne, res + "R"))

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    visit = [False] * 10000
    print(dslr(a))
import heapq
from collections import defaultdict
from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline

T = int(input())
for _ in range(T):
    res = []
    N, M = map(int, input().split())
    dp = [[] for i in range(M)]
    dic = defaultdict(list)
    for i in range(N):
        s, e, c = map(int, input().split())
        dic[s].append((c, e))
        dic[e].append((c, s))
    Q = [(0, 0, 0)]
    visit = [False] * M
    while Q:
        c, e, s = heapq.heappop(Q)
        if visit[e]:
            continue
        else:
            dp[e] = dp[s] + [e]
        if e == M-1:
            break
        visit[e] = True
        for nc, ne in dic[e]:
            heapq.heappush(Q, (nc + c, ne, e))

    print(f"Case #{_+1}:", end=" ")
    if dp[M-1]:
        print(*dp[M-1])
    else:
        print(-1)
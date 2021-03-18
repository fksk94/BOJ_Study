import heapq
from sys import stdin
input = stdin.readline

gems = []
N, K = map(int, input().split())
for i in range(N):
    w, c = map(int, input().split())
    heapq.heappush(gems, (w, c))

knapsack = [int(input()) for i in range(K)]
knapsack.sort()

res = 0
res_arr = []

for min_w in knapsack:
    while True:
        if gems and min_w >= gems[0][0]:
            w, c = heapq.heappop(gems)
            heapq.heappush(res_arr, -c)
        else:
            break
    if res_arr:
        res -= heapq.heappop(res_arr)

print(res)

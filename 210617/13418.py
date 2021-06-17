from collections import defaultdict
from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline
import heapq

N, M = map(int, input().split())
dic = defaultdict(list)

# 0이 오르막길이므로 코스트를 XOR연산으로 변환
for i in range(M + 1):
    a, b, c = map(int, input().split())
    dic[a].append((c^1, b))
    dic[b].append((c^1, a))

# MST 함수 (프림)
def MST(Q, ch):
    res = 0
    heapq.heapify(Q)
    visit = [False] * (N + 1)
    visit[0] = True
    while Q:
        cost, next = heapq.heappop(Q)
        # 이미 방문한 것은 제외
        if visit[next]:
            continue
        res += cost
        visit[next] = True
        for i in dic[next]:
            # 이미 방문한 것은 제외(여기서 안해주면 시간초과)
            if visit[i[1]]:
                continue
            heapq.heappush(Q, (i[0] * ch, i[1]))
    return res

# 처음 코스트의 부호변환 작업(최대힙을 위해)
adj = [(-c, n) for c, n in dic[0]]

# 최대와 최소 값의 차 구함.
print(MST(adj[:], -1)**2 - MST(dic[0][:], 1)**2)
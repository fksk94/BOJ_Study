from collections import defaultdict, deque


def bfs():
    while q:
        val, loc = q.popleft()
        for j in range(len(barns.get(loc))):
            rloc = barns[loc].pop()
            if M[rloc] == float('inf'):
                M[rloc] = val + 1
                q.append((val+1, rloc))
    return val


N, K = map(int, input().split())
M = [float('inf')] * 20001
barns = defaultdict(list)
for _ in range(K):
    a, b = map(int, input().split())
    barns[a] += [b]
    barns[b] += [a]

q = deque([(0, 1)])
M[1] = 0
res = bfs()
ans = []
for i in range(len(M)):
    if M[i] == res:
        ans.append(i)
if ans:
    print(ans[0], res, len(ans))
else:
    print(1, 0, 1)
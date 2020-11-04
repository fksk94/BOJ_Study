from collections import deque

def bfs():
    cnt = 1
    visit[1] = 1
    while q:
        cnt += 1
        for j in range(len(q)):
            for i in friends.get(q.popleft()):
                if not visit[i]:
                    q.append(i)
                    visit[i] = cnt

T = int(input())
friends = {}
visit = [0] * 100001
for _ in range(1, T):
    a, b = map(int, input().split())
    if friends.get(a):
        friends[a] += [b]
    else:
        friends[a] = [b]
    if friends.get(b):
        friends[b] += [a]
    else:
        friends[b] = [a]
q = deque([1])
bfs()
for i in range(2, T+1):
    for j in friends[i]:
        if visit[j] + 1 == visit[i]:
            print(j)
            break
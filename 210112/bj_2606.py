N = int(input())
M = int(input())
virus = [[] for i in range(101)]
for i in range(M):
    a, b = map(int, input().split())
    virus[a].append(b)
    virus[b].append(a)

visited = [False] * (N+1)
visited[1] = True
S = virus[1]
cnt = 0
while S:
    tmp = S.pop()
    if visited[tmp] == False:
        visited[tmp] = True
        S.extend(virus[tmp])
        cnt += 1
print(cnt)
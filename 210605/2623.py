from collections import defaultdict, deque
from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline

N, M = map(int, input().split())
dic = defaultdict(list)
dms = [0] * (N+1)
for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr)-1):
        dic[arr[i]].append(arr[i+1])
        dms[arr[i+1]] += 1
Q = deque(list(range(1, N+1)))

res = []
check = False
cnt = 0
while Q:
    num = Q.popleft()
    if cnt > N:
        check = True
        break
    if dms[num]:
        Q.append(num)
        cnt += 1
        continue
    else:
        cnt = 0
        for i in dic[num]:
            dms[i] -= 1
        res.append(num)

if check:
    print(0)
else:
    for i in res:
        print(i)
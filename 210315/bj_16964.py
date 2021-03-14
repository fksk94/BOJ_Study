from sys import stdin, setrecursionlimit
from collections import defaultdict
input = stdin.readline
setrecursionlimit(200000)


dic = defaultdict(list)
N = int(input())
visit = [False] * (N+1)
visit[1] = True

for i in range(N-1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

t = -1
order = list(map(int, input().split()))
while len(order) > 1:
    tmp = order.pop()
    if len(dic[t]) == 1 and t != 1:
        if t != tmp:
            print(0)
            break
    if len(dic.get(tmp)) == 1:
        t = dic[tmp].pop()
        dic[t].remove(tmp)
    else:
        print(0)
        break
else:
    if order[0] != 1:
        print(0)
    else:
        print(1)
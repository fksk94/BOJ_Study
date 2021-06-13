from collections import defaultdict
from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline


n = int(input())
tree = list(map(int, input().split()))
del_n = int(input())

dic = defaultdict(list)
for i in range(len(tree)):
    if tree[i] == -1:
        start = i
        continue
    if tree[i] != del_n and i != del_n:
        dic[tree[i]].append(i)

Q = dic[start]
if Q or start == del_n:
    cnt = 0
    while Q:
        ne = Q.pop()
        for i in dic[ne]:
            Q.append(i)
        if ne != del_n and not dic[ne]:
            cnt += 1
    print(cnt)
else:
    print(1)


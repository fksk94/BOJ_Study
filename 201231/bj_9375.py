from sys import stdin
from collections import defaultdict
input = stdin.readline


T = int(input())
for _ in range(T):
    dic = defaultdict(list)
    N=int(input())
    for i in range(N):
        a, b = input().split()
        dic[b].append(a)
    cnt = 1
    for i in dic:
        cnt *= (len(dic[i])+1)
    print(cnt - 1)
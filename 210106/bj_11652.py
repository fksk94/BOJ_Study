from sys import stdin
from collections import defaultdict
input = stdin.readline


N = int(input())
mem = defaultdict(int)
for i in range(N):
    a = int(input())
    mem[a] += 1
compare = (0, float('inf'))
for key, item in mem.items():
    if item >= compare[0]:
        if item == compare[0] and key < compare[1]:
            compare = (item, key)
        elif item > compare[0]:
            compare = (item, key)
print(compare[1])
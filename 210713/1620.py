from sys import stdin
input = stdin.readline

dic = dict()
N, M = map(int, input().split())
res = 0
for i in range(N):
    name = input().rstrip()
    dic[name] = i+1
    dic[str(i+1)] = name

for i in range(M):
    Q = input().rstrip()
    print(dic[Q])
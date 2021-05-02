from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

dic = dict()
for i in range(N):
    site, pw = input().rstrip().split()
    dic[site] = pw

for i in range(M):
    site = input().rstrip()
    print(dic.get(site))
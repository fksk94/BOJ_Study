from sys import stdin
input = stdin.readline


N, M = map(int, input().split())
dic = dict()

for i in range(N):
    a, b = map(int, input().split())
    dic[a] = b

for i in range(M):
    a, b = map(int, input().split())
    dic[a] = b

res = 1
S = [(1, 0)]
can = [float('inf')] * 101
can[1] = 0
while S:
    tmp, cnt = S.pop()
    if tmp >= 100:
        if can[100] > cnt:
            can[100] = cnt
        continue
    for i in range(1, 7):
        if dic.get(tmp+i):
            if can[dic.get(tmp+i)] > cnt + 1:
                can[dic.get(tmp+i)] = cnt + 1
                S.append((dic.get(tmp+i), cnt+1))
        else:
            if tmp + i < 101 and can[tmp + i] > cnt + 1:
                S.append((tmp + i, cnt + 1))
                can[tmp + i] = cnt + 1

print(can[100])
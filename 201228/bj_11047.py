from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
arr = [int(input()) for i in range(N)]
for i in range(N):
    if arr[i] > K:
        here = i
        break
else:
    here = N-1

cnt = 0
while K:
    cnt += K // arr[here]
    K -= arr[here] * (K//arr[here])
    here -= 1
print(cnt)
N, K = map(int, input().split())
arr = list(map(int, input().split()))
S = 0
res = []
last = N-K
while S <= last:
    store_K = K
    while K <= N:
        sum_arr = 0
        cnt = K-S
        m = sum([arr[i] for i in range(S, K)])/cnt
        tmp = 0
        for i in range(S, K):
            tmp += (arr[i] - m)**2
        res.append((tmp/cnt)**0.5)
        K += 1
    K = store_K
    K += 1
    S += 1
print(min(res))
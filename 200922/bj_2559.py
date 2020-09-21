N, K = map(int, input().split())
arr = list(map(int, input().split()))
t = sum(arr[0:K])
max_d = t
for i in range(K, N):
    t = t + arr[i] - arr[i-K]
    if max_d < t:
        max_d = t
print(max_d)
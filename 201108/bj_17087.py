def GCD(a,b):
    while b != 0:
        a, b = b, a%b
    return a

N, S = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(N):
    arr[i] = abs(arr[i] - S)
arr.sort()
for i in range(N-1):
    arr[i+1] = GCD(arr[i+1], arr[i])
print(arr[N-1])
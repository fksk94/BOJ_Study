a, b = map(int, input().split())
arr = [0]
for i in range(1, 300):
    arr.extend([i] * i)

print(sum(arr[a:b+1]))
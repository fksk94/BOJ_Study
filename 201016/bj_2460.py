sum = 0
arr = []
for _ in range(10):
    a, b = map(int, input().split())
    sum = sum - a + b
    arr.append(sum)
print(max(arr))
a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

s = arr[0]
cnt = 1
for i in arr:
    if i < s + b:
        continue
    else:
        s = i
        cnt += 1

print(cnt)
a, b = map(int, input().split())
arr = []
for i in range(a-1, 0, -1):
    if b - i <= 0:
        ttmp = [k for k in range(1, i+2)]
        tmp = ttmp[b]
        ttmp.remove(tmp)
        ttmp = [tmp] + ttmp
        for j in range(a, i+1, -1):
            arr.append(j)
        arr.extend(ttmp)
        break
    else:
        b -= i
for i in range(len(arr)):
    print(arr[i], end=" ")
arr =[]
for i in range(5):
    N = int(input())
    arr.append(N)
if arr:
    print(sum(arr)//len(arr))
    print(sorted(arr)[2])
else:
    print(-1)
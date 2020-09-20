T = int(input())
arr = list(map(int, input().split()))
arr2 = []
for i in range(1,T+1):
    arr2.insert(arr[i-1], i)
print(*list(reversed(arr2)))
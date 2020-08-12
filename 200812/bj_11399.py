s = int(input())
arr = list(map(int, input().split()))

sum_arr = 0
n = len(arr)
for i in range(n, 0, -1) :
    sum_arr += min(arr)*i
    arr.remove(min(arr))

print(sum_arr)
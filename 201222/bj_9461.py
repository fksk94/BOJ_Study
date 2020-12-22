T = int(input())
arr = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16] + [0] * 90
for i in range(10, 101):
    arr[i] = arr[i-1] + arr[i-5]

for i in range(T):
    N = int(input())
    print(arr[N])

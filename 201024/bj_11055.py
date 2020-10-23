N = int(input())
arr = list(map(int, input().split()))
s_arr = [arr[i] for i in range(len(arr))]
for j in range(N):
    for i in range(j, -1, -1):
        if arr[i] < arr[j]:
            if s_arr[j] < s_arr[i]+arr[j]:
                s_arr[j] = s_arr[i]+arr[j]
print(max(s_arr))
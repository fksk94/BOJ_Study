T = int(input())
arr = list(map(int, input().split()))
e_arr = list(enumerate(sorted(arr)))
for i in range(T):
    for j in range(T):
        if e_arr[j][1] == arr[i]:
            print(e_arr[j][0], end=' ')
            e_arr.remove(e_arr[j])
            break
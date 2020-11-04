N = int(input())
arr = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())), reverse=True)
print(sum([arr[i]*arr2[i]for i in range(N)]))
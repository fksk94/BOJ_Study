n, max_n = map(int, input().split())

arr = list(map(int, input().split()))

result_list = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for z in range(j+1, n):
            result_list.append(arr[i] + arr[j] + arr[z])
com_result = max_n

for i in result_list :
    if com_result >= max_n - i >= 0 :
        com_result = max_n - i
        result = i
print(result)
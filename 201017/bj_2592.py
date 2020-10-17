arr =[]
check = [0] * 1001
for i in range(10):
    N = int(input())
    arr.append(N)
for i in arr:
    check[i] += 1
print(sum(arr)//len(arr))
print(check.index(max(check)))
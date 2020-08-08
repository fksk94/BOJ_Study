s = input()
n = int(s)
arr = list(s)
min_sum = 0
for i in range(n, n - (len(arr)*10), -1) :
    sum = i
    if i >= 0 :
        arr_2 = list(str(i))
        for j in arr_2 :
            sum += int(j)
        if sum == n :
            min_sum = i

print(min_sum)
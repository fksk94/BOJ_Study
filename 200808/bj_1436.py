n = int(input())

arr = []
for i in range(666, 2666800) :
    x = list(str(i))
    for j in range(len(x)-2) :
        if x[j] == x[j+1] == x[j+2] == '6' :
            arr.append(i)
            break

print(arr[n-1])
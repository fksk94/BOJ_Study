s = int(input())

arr_x = []
arr_y = []
for _ in range(s):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

first_idx = []

for i in range(s):
    first = 1
    for j in range(s):
        if arr_x[i] < arr_x[j] and arr_y[i] < arr_y[j]:
            first += 1
    first_idx.append(first)

print(first_idx[0],end = '')
for i in first_idx[1:s] :
    print(f" {i}", end='')
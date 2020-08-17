import sys

s = int(input())
arr = []
arr_dict = {}
for i in range(s):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    if arr_dict.get(n) :
        arr_dict.get(n).append(m)
    else :
        arr_dict[n] = [m]

for i in range(-100000, 100001) :
    if arr_dict.get(i) :
        a =len(arr_dict.get(i))
        for j in range(a) :
            print(i, min(arr_dict.get(i)))
            arr_dict[i].remove(min(arr_dict[i]))

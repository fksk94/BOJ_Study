import sys

s = int(input())
arr = []
arr_dict = {}
for i in range(s):
    n = sys.stdin.readline().rstrip()
    m = len(n)
    if arr_dict.get(m) :
        arr_dict.get(m).append(n)
    else :
        arr_dict[m] = [n]

for i in range(1, 51) :
    if arr_dict.get(i) :
        arr_dict[i] = sorted(list(set(arr_dict[i])))
        for j in arr_dict[i] :
            print(j)
import sys

s = int(input())
arr = []
arr_dict = {}
for i in range(s):
    n, voca = map(str, sys.stdin.readline().rstrip().split())
    if arr_dict.get(n) :
        arr_dict.get(n).append(voca)
    else :
        arr_dict[n] = [voca]

for i in range(1, 201) :
    if arr_dict.get(str(i)) :
        for j in arr_dict[str(i)] :
            print(i, j)
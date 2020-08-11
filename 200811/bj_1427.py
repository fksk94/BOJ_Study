import sys

n = sys.stdin.readline().rstrip()
arr = list(n)
counting = [0] * 10

for i in range(len(arr)) :
    counting[int(arr[i])] += 1

for i in range(9, -1, -1) :
    if counting[i] != 0 :
        while counting[i] > 0 :
            print(i,end='')
            counting[i] -= 1
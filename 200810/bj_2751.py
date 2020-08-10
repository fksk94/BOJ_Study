import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n) :
    arr.append(int(sys.stdin.readline()))

counting = [0] * 2000001

result = []

for i in arr :
    counting[i] += 1

for i in range(-1000000, 1000001) :
    if counting[i] != 0 :
        while counting[i] > 0 :
            result.append(i)
            counting[i] -= 1

for i in result :
    print(i)
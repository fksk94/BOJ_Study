import sys

n = int(sys.stdin.readline())
counting = [0] * 10001
for i in range(n) :
    a = int(sys.stdin.readline())
    counting[a] += 1

for i in range(1, 10001) :
    if counting[i] != 0 :
        while counting[i] > 0 :
            print(i)
            counting[i] -= 1
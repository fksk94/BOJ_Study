import sys

n = int(sys.stdin.readline())
counting = [0] * 10001
for i in range(n) :
    a = int(sys.stdin.readline())
    counting[a] += 1

for i in range(1, 10001) :
    print('{}\n'.format(i)*counting[i], end="")
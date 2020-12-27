from sys import stdin
input = stdin.readline

N = int(input())
arr= []
for i in range(N):
    tmp = int(input())
    if tmp == 0:
        arr.pop()
    else:
        arr.append(tmp)
print(sum(arr))

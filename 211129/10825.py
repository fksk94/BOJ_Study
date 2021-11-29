from sys import stdin
input = stdin.readline

T = int(input())
arr = [list(input().rstrip().split()) for i in range(T)]

arr.sort(key=lambda x:x[0])
arr.sort(key=lambda x:int(x[3]), reverse=True)
arr.sort(key=lambda x:int(x[2]))
arr.sort(key=lambda x:int(x[1]), reverse=True)
for i in range(T):
    print(arr[i][0])

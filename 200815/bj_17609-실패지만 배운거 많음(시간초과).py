import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n) :
    arr.append(sys.stdin.readline().rstrip())

for i in range(n):
    result = []
    if arr[i][0:(len(arr[i])//2)] == arr[i][len(arr[i])-1:((len(arr[i])-1)//2):-1] :
        print(0)
    else :
        if [1 for j in range(len(arr[i])) if (arr[i][:j]+arr[i][j+1:])[0:(len(arr[i])-1)//2] == (arr[i][:j]+arr[i][j+1:])[(len(arr[i])-1):(len(arr[i])//2-1):-1]]:
            print(1)
        else :
            print(2)
import sys

T = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(T)]
res = []

for _ in range(6):
    result = 0
    tmp = _ + 1
    for k in range(T):
        for i in range(6):
            if arr[k][i] == tmp:
                if i == 0:
                    tmp = arr[k][5]
                    result += max(arr[k][1], arr[k][2], arr[k][3], arr[k][4])
                elif i == 5:
                    tmp = arr[k][0]
                    result += max(arr[k][1], arr[k][2], arr[k][3], arr[k][4])
                elif i == 1:
                    tmp = arr[k][3]
                    result += max(arr[k][0], arr[k][2], arr[k][4], arr[k][5])
                elif i == 3:
                    tmp = arr[k][1]
                    result += max(arr[k][0], arr[k][2], arr[k][4], arr[k][5])
                elif i == 2:
                    tmp = arr[k][4]
                    result += max(arr[k][0], arr[k][1], arr[k][3], arr[k][5])
                elif i == 4:
                    tmp = arr[k][2]
                    result += max(arr[k][0], arr[k][1], arr[k][3], arr[k][5])
                break

    res.append(result)
print(max(res))
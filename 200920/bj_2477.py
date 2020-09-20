def solution():
    T = int(input())
    arr = [list(map(int, input().split())) for i in range(6)]
    com = []
    boarder = []
    x = []
    y = []
    for i in range(len(arr)):
        com.append(arr[i][0])
    for i in range(1,5):
        if com.count(i) == 2:
            boarder.append(i)

    for i in range(len(arr)):
        if not arr[i][0] in boarder:
            x.append(arr[i][1])
            sarr = arr[i:] + arr[:i]
            for j in range(6):
                if sarr[j][0] in boarder:
                    y.append(sarr[j][1])
    result = x[0]*x[1] - y[1]*y[2]
    return result*T

print(solution())
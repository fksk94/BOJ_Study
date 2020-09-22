def solution():
    N, M = map(int, input().split())
    x_arr = [0]
    y_arr = [0]
    T = int(input())
    for _ in range(T):
        x, y = map(int, input().split())
        if x == 0:
            x_arr.append(y)
        else:
            y_arr.append(y)
    x_arr.sort()
    y_arr.sort()
    max_x = 0
    max_y = 0
    for i in range(1, len(x_arr)):
        if max_x < x_arr[i]-x_arr[i-1]:
            max_x = x_arr[i]-x_arr[i-1]
    if max_x < M-x_arr[len(x_arr)-1]:
        max_x = M - x_arr[len(x_arr) - 1]
    for i in range(1, len(y_arr)):
        if max_y < y_arr[i]-y_arr[i-1]:
            max_y = y_arr[i]-y_arr[i-1]
    if max_y < N - y_arr[len(y_arr)-1]:
        max_y = N - y_arr[len(y_arr) - 1]
    print(max_x*max_y)
solution()
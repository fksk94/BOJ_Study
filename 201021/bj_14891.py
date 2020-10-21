def change(num, d):
    global arr
    if d == 1:
        if num == 1:
            if arr[num][2] != arr[num + 1][6]:
                if arr[num + 1][2] != arr[num + 2][6]:
                    if arr[num + 2][2] != arr[num + 3][6]:
                        arr[num + 3] = arr[num + 3][1:] + [arr[num + 3][0]]
                    arr[num + 2] = [arr[num + 2][7]] + arr[num + 2][:7]
                arr[num + 1] = arr[num + 1][1:] + [arr[num + 1][0]]
            arr[num] = [arr[num][7]] + arr[num][:7]
        if num == 2:
            if arr[num][2] != arr[num + 1][6]:
                if arr[num + 1][2] != arr[num + 2][6]:
                    arr[num + 2] = [arr[num + 2][7]] + arr[num + 2][:7]
                arr[num + 1] = arr[num + 1][1:] + [arr[num + 1][0]]
            if arr[num][6] != arr[num - 1][2]:
                arr[num - 1] = arr[num - 1][1:] + [arr[num - 1][0]]
            arr[num] = [arr[num][7]] + arr[num][:7]
        if num == 3:
            if arr[num][2] != arr[num + 1][6]:
                arr[num + 1] = arr[num + 1][1:] + [arr[num + 1][0]]
            if arr[num][6] != arr[num - 1][2]:
                if arr[num - 1][6] != arr[num - 2][2]:
                    arr[num - 2] = [arr[num - 2][7]] + arr[num - 2][:7]
                arr[num - 1] = arr[num - 1][1:] + [arr[num - 1][0]]
            arr[num] = [arr[num][7]] + arr[num][:7]
        if num == 4:
            if arr[num][6] != arr[num - 1][2]:
                if arr[num - 1][6] != arr[num - 2][2]:
                    if arr[num - 2][6] != arr[num - 3][2]:
                        arr[num - 3] = arr[num - 3][1:] + [arr[num - 3][0]]
                    arr[num - 2] = [arr[num - 2][7]] + arr[num - 2][:7]
                arr[num - 1] = arr[num - 1][1:] + [arr[num - 1][0]]
            arr[num] = [arr[num][7]] + arr[num][:7]
    else:
        if num == 1:
            if arr[num][2] != arr[num + 1][6]:
                if arr[num + 1][2] != arr[num + 2][6]:
                    if arr[num + 2][2] != arr[num + 3][6]:
                        arr[num + 3] = [arr[num + 3][7]] + arr[num + 3][:7]
                    arr[num + 2] = arr[num + 2][1:] + [arr[num + 2][0]]
                arr[num + 1] = [arr[num + 1][7]] + arr[num + 1][:7]
            arr[num] = arr[num][1:] + [arr[num][0]]
        if num == 2:
            if arr[num][2] != arr[num + 1][6]:
                if arr[num + 1][2] != arr[num + 2][6]:
                    arr[num + 2] = arr[num + 2][1:] + [arr[num + 2][0]]
                arr[num + 1] = [arr[num + 1][7]] + arr[num + 1][:7]
            if arr[num][6] != arr[num - 1][2]:
                arr[num - 1] = [arr[num - 1][7]] + arr[num - 1][:7]
            arr[num] = arr[num][1:] + [arr[num][0]]
        if num == 3:
            if arr[num][2] != arr[num + 1][6]:
                arr[num + 1] = [arr[num + 1][7]] + arr[num + 1][:7]
            if arr[num][6] != arr[num - 1][2]:
                if arr[num - 1][6] != arr[num - 2][2]:
                    arr[num - 2] = arr[num - 2][1:] + [arr[num - 2][0]]
                arr[num - 1] = [arr[num - 1][7]] + arr[num - 1][:7]
            arr[num] = arr[num][1:] + [arr[num][0]]
        if num == 4:
            if arr[num][6] != arr[num - 1][2]:
                if arr[num - 1][6] != arr[num - 2][2]:
                    if arr[num - 2][6] != arr[num - 3][2]:
                        arr[num - 3] = [arr[num - 3][7]] + arr[num - 3][:7]
                    arr[num - 2] = arr[num - 2][1:] + [arr[num - 2][0]]
                arr[num - 1] = [arr[num - 1][7]] + arr[num - 1][:7]
            arr[num] = arr[num][1:] + [arr[num][0]]


arr = [[0]] + [list(map(int, list(input()))) for i in range(4)]
K = int(input())
for i in range(K):
    n, direction = map(int, input().split())
    change(n, direction)
print(arr[1][0] + arr[2][0] * 2 + arr[3][0] * 4 + arr[4][0] * 8)
def check():
    ch1 = [0] * 5
    ch2 = [0] * 5
    ch3 = 0
    ch4 = 0
    for i in range(5):
        for j in range(5):
            if arr2[i][j] == True:
                ch1[i] += 1
                ch2[j] += 1
            if i == j:
                if arr2[i][j] == True:
                    ch3 += 1
            if i + j == 4:
                if arr2[i][j] == True:
                    ch4 += 1
    result = ch2.count(5) + ch1.count(5)
    if ch3 == 5:
        result += 1
    if ch4 == 5:
        result += 1
    return result



arr = [list(map(int, input().split())) for i in range(5)]
call = [list(map(int, input().split())) for i in range(5)]
arr2 = [[False] * 5 for i in range(5)]
for i in range(5):
    for j in range(5):
        for k in range(5):
            for m in range(5):
                if arr[k][m] == call[i][j]:
                    arr2[k][m] = True
                    break
            if arr[k][m] == call[i][j]:
                break
        if check() >= 3:
            print((i)*5+(j+1))
            break
    if check() >= 3:
        break
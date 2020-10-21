def howmany(n):
    global cnt2
    for k1 in range(0, 7, 3):
        for k2 in range(0, 7, 3):
            if k1+n < 11 and k2+n < 11:
                for i in range(k1, k1+n):
                    for j in range(k2, k2+n):
                        if i == k1 or i == k1+n-1 or j == k2 or j == k2+n-1:
                            if check[i][j] == True:
                                cnt2 += 1
                                break
                    if check[i][j] == True:
                        break


init = [['+', '-', '-', '+', '-', '-', '+', '-', '-', '+'], ['|', '.', '.', '|', '.', '.', '|', '.', '.', '|'], ['|', '.', '.', '|', '.', '.', '|', '.', '.', '|'], ['+', '-', '-', '+', '-', '-', '+', '-', '-', '+'], ['|', '.', '.', '|', '.', '.', '|', '.', '.', '|'], ['|', '.', '.', '|', '.', '.', '|', '.', '.', '|'], ['+', '-', '-', '+', '-', '-', '+', '-', '-', '+'], ['|', '.', '.', '|', '.', '.', '|', '.', '.', '|'], ['|', '.', '.', '|', '.', '.', '|', '.', '.', '|'], ['+', '-', '-', '+', '-', '-', '+', '-', '-', '+']]
arr = [list(input()) for i in range(10)]
check = [[0] * 10 for i in range(10)]
cnt, cnt2 = 0, 0
for i in range(10):
    for j in range(10):
        if init[i][j] != arr[i][j]:
            cnt += 1
            check[i][j] = True

for i in range(4, 11, 3):
    howmany(i)

print(cnt//2, 14-cnt2)
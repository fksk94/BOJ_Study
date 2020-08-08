x, y = map(int, input().split())
W = 'W'
B = 'B'
success_1 = [[W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W]
             ]
success_2 = [[B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B],
             [B, W, B, W, B, W, B, W],
             [W, B, W, B, W, B, W, B]
             ]

arr = []
for i in range(x) :
    arr.append(list(input()))
result = 64
for i in range(x-7):
    for j in range(y-7) :
        result_sum_1 = 0
        result_sum_2 = 0
        for m in range(i, i+8) :
            for n in range(j, j+8) :
                if arr[m][n] != success_1[m-i][n-j] :
                    result_sum_1 += 1
                if arr[m][n] != success_2[m-i][n-j] :
                    result_sum_2 += 1
        if result_sum_1 < result_sum_2 :
            pre_result = result_sum_1
        else :
            pre_result = result_sum_2
        if pre_result < result :
            result = pre_result
print(result)
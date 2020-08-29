def perfect_sort(max_num) :
    if max_num == 6 :
        return

    perfect_sort(max_num-3)
    for i in range(max_num, 19, 3) :
        arr[i-3:i], arr[i-6:i-3] = arr[i-6:i-3], arr[i-3:i]
        all_of_arr.append(arr[:])
        perfect_sort(max_num - 3)
    return

def game(start, sarr) :
    global sig
    if start == 15 :
        sig = True
        return
    for i in range(start + 3, 18, 3):
        if sarr[start] > 0 and sarr[i + 2] > 0:
            sarr[start] -= 1
            sarr[i + 2] -= 1

        elif sarr[start + 1] > 0 and sarr[i + 1] > 0:
            sarr[start + 1] -= 1
            sarr[i + 1] -= 1

        elif sarr[start + 2] > 0 and sarr[i] > 0:
            sarr[start + 2] -= 1
            sarr[i] -= 1
        else :
            return
    game(start + 3, sarr)
    return


for i in range(4) :
    sig = False
    cnt = 0
    all_of_arr = []
    arr = list(map(int, input().split()))
    perfect_sort(18)
    for j in range(0, 18, 3) :
        if sum(arr[j:j+3]) == 5 :
            cnt += 1

    if cnt == 6 :
        for j in all_of_arr:
            game(0, j)
        if sig == True:
            print(1, end=' ')
        else:
            print(0, end=' ')
    else :
        print(0, end=' ')



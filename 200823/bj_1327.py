# 입력
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 기본값 설정
sarr = "".join(str(i) for i in arr)
sarr_init = sarr
sarr_sort = "".join(str(i) for i in sorted(arr))
all_of_arr = [sarr]
bfs_dict = {sarr : 0}
count = 0


# arr 바꾸기.
num = 0
try :
    while num < 40317:
        sarr_init = all_of_arr[num]
        count = bfs_dict[sarr_init]+1
        num += 1
        for i in range(n-m+1) :
            sarr = sarr_init
            sarr = sarr[0:i] + ''.join(reversed(sarr[i:(m + i)])) + sarr[(m + i):n]
            if bfs_dict.get(sarr) == None :
                bfs_dict[sarr] = count
                all_of_arr.append(sarr)
        if bfs_dict.get(sarr_sort) != None :
            print(bfs_dict[sarr_sort])
            break
except :
    print(-1)
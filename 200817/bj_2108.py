import sys
s = int(input())
count_arr = [0]*8001
sum_n = 0
mid_count = -1
max_item = 1
sig = False
s_count = 0

for i in range(s):
    count_arr[int(sys.stdin.readline().rstrip())+4000] += 1

# 정렬

for i in range(8001) :
    if count_arr[i] :
        sum_n += (i-4000)*count_arr[i]
        mid_count += count_arr[i]
        if mid_count >= s//2 and sig == False:
            sig = True
            mid_value = i-4000
        if count_arr[i] > max_item :
            max_item = count_arr[i]
            s_count = 0
        if max_item == count_arr[i]:
            s_count += 1
            a = i - 4000
            if s_count == 2 :
                a_2 = i-4000

# 평균값
print(round(sum_n / s))

# 중앙값
print(mid_value)

# 최빈값
if s_count != 1 :
    print(a_2)
else :
    print(a)

# 범위
for i in range(8001) :
    if count_arr[i] :
        min_n = i-4000
        break
for i in range(8000, -1, -1) :
    if count_arr[i] :
        max_n = i-4000
        break
print(max_n - min_n)
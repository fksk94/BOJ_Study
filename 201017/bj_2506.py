N = int(input())
a = list(map(int,input().split()))
cnt = 0
sum = 0
for i in a:
    sum += cnt
    if i == 0:
        cnt = 0
    else:
        cnt += 1

print(sum+cnt)
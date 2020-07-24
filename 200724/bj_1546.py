a = int(input())
b = list(map(int, input().split()))
sum_b = 0
for i in range(a) :
    sum_b += b[i]/max(b)*100
print(sum_b/a)
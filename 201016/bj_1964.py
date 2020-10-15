T = int(input())
sum = 1
for i in range(1, T+1):
    sum += (i*3 +1)
print(sum%45678)
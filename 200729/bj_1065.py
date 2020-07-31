n = int(input())
sum_i = 0
if n < 100 :
    sum_i = n
else :
    sum_i += 99
    for i in range(100, n+1):
        if (i//100 - (i//10 - (i//100)*10)) == ((i//10-(i//100)*10) - i%10) :
            sum_i += 1
if n >= 1000 :
    sum_i = 144
    
print(sum_i)
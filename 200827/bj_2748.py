def fibo(n) :
    if n < 3 :
        return 1
    if dict_fibo.get(n):
        return dict_fibo.get(n)
    return fibo(n-1) + fibo(n-2)

s = int(input())
dict_fibo = {0:0}
for i in range(1,91) :
    if not dict_fibo.get(i):
        dict_fibo[i] = fibo(i)

print(dict_fibo.get(s))
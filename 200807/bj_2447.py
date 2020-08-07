def fact(i, j, number):
    if number == 1 :
        star_matrix[i][j] = '*'
        return

    a = number//3
    for x in range(3) :
        for y in range(3) :
            if x == 1 and y == 1 :
                continue
            else :
                fact(i+x*a, j+y*a, a)

s = int(input())
star_matrix = [[' ']*s for _ in range(s)]

fact(0, 0, s)
for i in range(s) :
    for j in range(s):
        print(star_matrix[i][j], end = '')
    if i == s -1 :
        continue
    else :
        print()


# 밑의 식처럼 쓸 수 있도록 노력하자!
'''
def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]
 
def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' '*n]*n)
 
    return a + b + a
 
print('\n'.join(star10(int(input()))))
'''
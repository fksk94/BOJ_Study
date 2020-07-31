def fact(number):
    if number == 0 :
        return 0
    if number == 1 :
        return 1
    return fact(number-2) + fact(number-1)

s = int(input())
print(fact(s))
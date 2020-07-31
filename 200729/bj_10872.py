def fact(number):
    if number == 0 :
        return 1
    return number * fact(number-1)

s = int(input())
print(fact(s))
s = int(input())

for i in range(s) :
    li = list(map(int, input().split()))
    if (li[2]//li[0]) >= 9 :
        if (li[2]%li[0]) == 0 :
            if (li[2]//li[0]) == 9 :
                print(f"{(li[0])}0{li[2]//li[0]}")
            else :
                print(f"{(li[0])}{li[2]//li[0]}")
        else :
            print(f"{(li[2]%li[0])}{li[2]//li[0]+1}")
    else :
        if (li[2]%li[0]) == 0 :
            print(f"{(li[0])}0{li[2]//li[0]}")
        else :
            print(f"{(li[2]%li[0])}0{li[2]//li[0]+1}")
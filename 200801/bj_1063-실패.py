s = input().split()

king = list(s[0])
stone = list(s[1])

king[1] = int(king[1])
stone[1] = int(stone[1])

for i in range(0, int(s[2])) :
    a = input()
    if a == 'R' :
        if king[0] == 'H' :
            pass
        elif king[0] == 'G' :
            if stone[0] == 'H' and king[1] == stone[1] :
                pass
            else :
                king[0] = 'H'
                pass
        else :
            if stone[1] == king[1] and ord(stone[0]) == (ord(king[0])+1):
                king[0] = chr(ord(king[0])+1)
                stone[0] = chr(ord(stone[0])+1)
            else :
                king[0] = chr(ord(king[0])+1)

    elif a == 'L' :
        if king[0] == 'A' :
            pass
        elif king[0] == 'B' :
            if stone[0] == 'A' and king[1] == stone[1] :
                pass
            else :
                king[0] = 'A'
                pass
        else :
            if stone[1] == king[1] and ord(stone[0]) == (ord(king[0])-1):
                king[0] = chr(ord(king[0])-1)
                stone[0] = chr(ord(stone[0])-1)
            else :
                king[0] = chr(ord(king[0])-1)

    elif a == 'B' :
        if king[1] == 1 :
            pass
        elif king[1] == 2 :
            if stone[1] == 1 and king[0] == stone[0] :
                pass
            else :
                king[1] = 1
                pass
        else :
            if stone[0] == king[0] and stone[1] == (king[1]-1):
                king[1] = king[1]-1
                stone[1] = stone[1]-1
            else :
                king[1] = king[1]-1

    elif a == 'T' :
        if king[1] == 8 :
            pass
        elif king[1] == 7 :
            if stone[1] == 8 and king[0] == stone[0] :
                pass
            else :
                king[1] = 8
                pass
        else :
            if stone[0] == king[0] and stone[1] == (king[1]+1):
                king[1] = king[1]+1
                stone[1] = stone[1]+1
            else :
                king[1] = king[1]+1

    elif a == 'RT' :
        if king[0] == 'H' or king[1] == 8 :
            pass
        elif king[0] == 'G' and king[1] == 7 :
            if stone[0] == 'H' and stone[1] == 8 :
                pass
            else :
                king[0] = 'H'
                king[1] = 8
                pass           
        else :
            if stone[1] == (king[1]+1) and ord(stone[0]) == (ord(king[0])+1):
                king[0] = chr(ord(king[0])+1)
                stone[0] = chr(ord(stone[0])+1)
                king[1] = king[1]+1
                stone[1] = stone[1]+1
            else :
                king[1] = king[1]+1
                king[0] = chr(ord(king[0])+1)

    elif a == 'LT' :
        if king[0] == 'A' or king[1] == 8 :
            pass
        elif king[0] == 'B' and king[1] == 7 :
            if stone[0] == 'A' and stone[1] == 8 :
                pass
            else :
                king[0] = 'A'
                king[1] = 8
                pass          
        else :
            if stone[1] == (king[1]+1) and ord(stone[0]) == (ord(king[0])-1):
                king[0] = chr(ord(king[0])-1)
                stone[0] = chr(ord(stone[0])-1)
                king[1] = king[1]+1
                stone[1] = stone[1]+1
            else :
                king[1] = king[1]+1
                king[0] = chr(ord(king[0])-1)

    elif a == 'RB' :
        if king[0] == 'H' or king[1] == 1 :
            pass
        elif king[0] == 'G' and king[1] == 2 :
            if stone[0] == 'H' and stone[1] == 1 :
                pass
            else :
                king[0] = 'H'
                king[1] = 1
                pass
        else :
            if stone[1] == (king[1]-1) and ord(stone[0]) == (ord(king[0])+1):
                king[0] = chr(ord(king[0])+1)
                stone[0] = chr(ord(stone[0])+1)
                king[1] = king[1]-1
                stone[1] = stone[1]-1
            else :
                king[1] = king[1]-1
                king[0] = chr(ord(king[0])+1)

    elif a == 'LB' :
        if king[0] == 'A' or king[1] == 1 :
            pass
        elif king[0] == 'B' and king[1] == 2 :
            if stone[0] == 'A' and stone[1] == 1 :
                pass
            else :
                king[0] = 'A'
                king[1] = 1
                pass            
        else :
            if stone[1] == (king[1]-1) and ord(stone[0]) == (ord(king[0])-1):
                king[0] = chr(ord(king[0])-1)
                stone[0] = chr(ord(stone[0])-1)
                king[1] = king[1]-1
                stone[1] = stone[1]-1
            else :
                king[1] = king[1]-1
                king[0] = chr(ord(king[0])-1)

print(f"{king[0]}{king[1]}")
print(f"{stone[0]}{stone[1]}")
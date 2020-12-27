from sys import stdin
input = stdin.readline

while True:
    S = []
    A = input().rstrip()
    if A == '.':
        break
    try:
        for j in range(len(A)):
            if A[j] == '(':
                S.append(1)
            elif A[j] == '[':
                S.append(2)
            elif A[j] == ')':
                if S.pop() != 1:
                    print('no')
                    break
            elif A[j] == ']':
                if S.pop() != 2:
                    print('no')
                    break
        else:
            if S == []:
                print('yes')
            else:
                print('no')
    except:
        print('no')

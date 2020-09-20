def solution():
    result = 0
    X, Y = map(int, input().split())
    T = int(input())
    locations = [tuple(map(int, input().split())) for i in range(T+1)]
    for i in range(T):
        dong = locations[T][1]
        store = locations[i][1]
        if locations[T][0] == locations[i][0]:
            result += abs(dong - store)
        elif (locations[T][0] == 1 or locations[T][0] == 2):
            if (locations[i][0] == 1 or locations[i][0] == 2):
                result += abs(dong - store) + min(X - dong, dong, X - store, store) * 2 + Y
            elif locations[i][0] == 3:
                if locations[T][0] == 1:
                    result += dong + store
                else:
                    result += dong + Y - store
            elif locations[i][0] == 4:
                if locations[T][0] == 1:
                    result += X - dong + store
                else:
                    result += X - dong + Y - store
        elif (locations[T][0] == 3 or locations[T][0] == 4):
            if (locations[i][0] == 3 or locations[i][0] == 4):
                result += abs(dong - store) + min(Y - dong, dong, Y - store, store) * 2 + X
            elif locations[i][0] == 1:
                if locations[T][0] == 3:
                    result += dong + store
                else:
                    result += dong + X - store
            elif locations[i][0] == 4:
                if locations[T][0] == 1:
                    result += Y - dong + store
                else:
                    result += Y - dong + X - store
    print(result)
solution()
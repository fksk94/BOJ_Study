import sys
sys.setrecursionlimit(2000)
n = int(sys.stdin.readline())

arr_cost =[]
dp1 = [0]*(n+1)
dp2 = [0]*(n+1)
dp3 = [0]*(n+1)

# 입력
for i in range(n) :
    c1, c2, c3  = map(int, sys.stdin.readline().split())
    arr_cost.append([c1, c2, c3])

def redp(homes, count):

    if homes <= 0:
        return 0

    elif dp1[homes] > 0 and count == 0:
        return dp1[homes]

    elif dp2[homes] > 0 and count == 1:
        return dp2[homes]

    elif dp3[homes] > 0 and count == 2:
        return dp3[homes]

    else:
        min_cost = 10000001
        if count != 0 :
            cost = redp(homes-1, 0) + arr_cost[homes-1][0]
            if cost < min_cost:
                min_cost = cost
        if count != 1 :
            cost = redp(homes-1, 1) + arr_cost[homes-1][1]
            if cost < min_cost:
                min_cost = cost
        if count != 2:
            cost = redp(homes-1, 2) + arr_cost[homes-1][2]
            if cost < min_cost:
                min_cost = cost

        if count == 0:
            dp1[homes] = min_cost

        if count == 1:
            dp2[homes] = min_cost

        if count == 2:
            dp3[homes] = min_cost

        return min_cost

print(redp(n, 3))
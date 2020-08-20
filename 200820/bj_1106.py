import sys
sys.setrecursionlimit(2000)
n, m = map(int, sys.stdin.readline().split())
arr_cost =[]
arr_people =[]
dp = [0]*1001

# ют╥б
for i in range(m) :
    c, customer = map(int, sys.stdin.readline().split())
    arr_cost.append(c)
    arr_people.append(customer)

def redp(people, city):
    min_cost = 100001

    if people <= 0:
        return 0

    elif dp[people] > 0:
        return dp[people]

    else:
        for i in range(city):
            cost = redp(people - arr_people[i], city) + arr_cost[i]
            if cost < min_cost:
                min_cost = cost
        dp[people] = min_cost

        return min_cost

print(redp(n, m))
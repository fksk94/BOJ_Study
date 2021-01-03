from sys import stdin

input = stdin.readline
N = int(input())
distances = list(map(int, input().split()))
cities = list(map(int, input().split()))

fuel = cities[0]
ans = fuel * distances[0]
for i in range(1, N-1):
    if fuel > cities[i]:
        fuel = cities[i]
    ans += fuel * distances[i]
print(ans)

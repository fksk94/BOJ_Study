N = int(input())
for i in range(N):
    print(sorted(list(map(int, input().split())))[-3])
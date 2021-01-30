from sys import stdin
input = stdin.readline

N, K = map(int, input().split())
convayer = list(map(int, input().split()))
robots = [False] * (2*N)
cnt = convayer.count(0)

res = 0
while True:
    # 1번
    if robots[N-1]:
        robots[N-1] = False
    convayer = [convayer[-1]] + convayer[:len(convayer)-1]
    robots = [robots[-1]] + robots[:len(robots)-1]

    # 2번
    if robots[N-1]:
        robots[N-1] = False
    for i in range(N-2, -1, -1):
        if robots[i]:
            if convayer[i+1] and robots[i+1] == False:
                convayer[i+1] -= 1
                robots[i+1] = True
                robots[i] = False
                if convayer[i+1] == 0:
                    cnt += 1


    # 3번
    if convayer[0]:
        convayer[0] -= 1
        robots[0] = True
        if convayer[0] == 0:
            cnt += 1

    # 4번
    res += 1
    if cnt >= K:
        break

print(res)
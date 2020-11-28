import sys
input = sys.stdin.readline

def sol():
    N, M = map(int, input().split())
    arr = [tuple(map(int, input().split())) for i in range(N)]
    arr.sort(key=lambda x:x[0], reverse=True)
    arr.sort(key=lambda x: x[1])

    ans = arr[0][0]
    cost = arr[0][1]
    cost_list = []
    if arr[0][0] >= M:
        cost_list.append(cost)
    else:
        for i in range(1, N):
            ans += arr[i][0]
            if arr[i][1] == arr[i-1][1]:
                cost += arr[i][1]
            else:
                cost = arr[i][1]

            if ans >= M and cost == arr[i][1]:
                cost_list.append(cost)
                break
            elif ans >= M:
                cost_list.append(cost)
                continue

    if cost_list:
        print(min(cost_list))
    else:
        print(-1)

sol()
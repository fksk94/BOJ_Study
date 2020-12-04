from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

def sol():
    N, M, S, E = map(int, input().split())
    dic = defaultdict(list)
    ans = [float('inf')] * 5001
    visited = [True] + [False] * 5000

    for i in range(M):
        arr = list(map(int, input().split()))
        dic[arr[0]] += [(arr[1], arr[2], arr[3])]
        dic[arr[1]] += [(arr[0], arr[2], arr[4])]

    Q = [(0, 1)]
    ans[1] = 0
    while Q:
        val, get_node = heapq.heappop(Q)
        if visited[get_node] == True:
            continue
        visited[get_node] = True
        tmp = dic[get_node]
        # 비교를 잘 못 했네?
        for i in tmp:
            if i[2]:
                # 퇴근시간 미 포함
                if (ans[get_node] + i[1]) <= S or E < ans[get_node]:
                    ans[i[0]] = min(ans[get_node] + i[1], ans[i[0]])
                    heapq.heappush(Q, (ans[i[0]], i[0]))

                # 포함되는 4가지 경우
                # S - E 중간에 있는 경우
                elif ans[get_node] + i[1] <= E and S < ans[get_node]:
                    if (ans[get_node] + i[1]*2) > E:
                        compare_val = (ans[get_node] + i[1]*2) - ((ans[get_node] + i[1]*2) - E)/2
                    else:
                        compare_val = (ans[get_node] + i[1] * 2)

                    ans[i[0]] = min(compare_val, ans[i[0]])
                    heapq.heappush(Q, (ans[i[0]], i[0]))

                # 중간에서 E의 뒤까지
                elif ans[get_node] + i[1] > E and S < ans[get_node]:
                    ans[i[0]] = min(ans[get_node] + i[1] + (E - ans[get_node])/2, ans[i[0]])
                    heapq.heappush(Q, (ans[i[0]], i[0]))

                # S의 앞에서 E의 뒤까지
                elif ans[get_node] + i[1] > E and S >= ans[get_node]:
                    ans[i[0]] = min(ans[get_node] + i[1] + (E - S)/2, ans[i[0]])
                    heapq.heappush(Q, (ans[i[0]], i[0]))

                # S의 앞에서 중간까지
                elif ans[get_node] + i[1] <= E and S >= ans[get_node]:
                    if (ans[get_node] + i[1] + (ans[get_node] + i[1] - S)) > E:
                        compare_val = (ans[get_node] + i[1] + (ans[get_node] + i[1] - S)) - ((ans[get_node] + i[1] + (ans[get_node] + i[1] - S)) - E)/2
                    else:
                        compare_val = (ans[get_node] + i[1] + (ans[get_node] + i[1] - S))

                    ans[i[0]] = min(compare_val, ans[i[0]])
                    heapq.heappush(Q, (ans[i[0]], i[0]))
            else:
                ans[i[0]] = min(ans[get_node] + i[1], ans[i[0]])
                heapq.heappush(Q, (ans[i[0]], i[0]))

    arr = [0 if ans[i] == float('inf') else ans[i] for i in range(5001)]
    res = max(arr)
    if int(res) == res:
        print(int(res))
    else:
        print(res)
sol()
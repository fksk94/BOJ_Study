from itertools import combinations

def solution():
    T = int(input())
    arr = [list(map(int, input().split())) for i in range(T)]
    ch = list(combinations(range(0,T), T//2))
    length = len(ch)
    ans = float('inf')
    for i in range(length//2):
        tmp_sum = 0
        for j in ch[i]:
            for k in ch[i]:
                tmp_sum += arr[j][k]
        for j in ch[length - 1 - i]:
            for k in ch[length - 1 - i]:
                tmp_sum -= arr[j][k]
        if ans > abs(tmp_sum):
            ans = abs(tmp_sum)
    print(ans)
solution()
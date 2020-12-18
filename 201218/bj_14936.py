# dfs
def dfs(e, m):
    res.add(e)
    if m-N >= 0:
        dfs(e^method_all, m-N)
    if m-N//2-N%2 >=0:
        dfs(e^method_odd, m-N//2-N%2)
    if m-N//2 >=0 and N > 1:
        dfs(e^method_even, m-N//2)
    if m-N//3 >=0 and N > 2:
        dfs(e^method_3th, m-N//3)

# 층수, 시간 입력
N, M = map(int, input().split())
elevator = 0
method_all = 2 ** N - 1
method_odd = int('1' * (N%2) + '01' * (N//2), 2)
method_even = int('0' if N//2 == 0 else '10' * (N//2), 2)
method_3th = int('0' if N//3 == 0 else '100' * (N//3), 2)
res = set()
dfs(elevator, M)
print(len(res))
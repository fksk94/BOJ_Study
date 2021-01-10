N, M, B = map(int, input().split())
board = [list(map(int, input().split())) for i in range(N)]
blocks = B
amounts = [0] * 257
for i in range(N):
    for j in range(M):
        amounts[board[i][j]] += 1
    blocks += sum(board[i])

for i in range(257):
    if amounts[i]:
        min_height = i
        break

for i in range(256, -1, -1):
    if amounts[i]:
        max_bong = i
        break

max_height= min(blocks // (N*M), 256)
mem = [0] * (max_height + 1)
for i in range(min_height, max_height + 1):
    for j in range(min_height, max_bong+1):
        if i > j:
            mem[i] += amounts[j] * (i - j)
        else:
            mem[i] += amounts[j] * ((j - i) * 2)

ans = mem[min_height]
idx = min_height
for i in range(min_height + 1, max_height + 1):
    if ans >= mem[i]:
        ans = mem[i]
        idx = i
print(ans, idx)
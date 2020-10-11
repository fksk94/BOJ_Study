import sys

def dfs(x):
    global res
    # res에 넣을 값이 작을 때
    if res > (25 - sum(paper)):
        # 모두 0 일 때, res 값 바꿈
        if sum_board == sum([(5 - paper[_]) * (_ * _) for _ in range(1, 6)]):
            res = 25 - sum(paper)
            return
        # 아니라면 이거 실행
        else:
            # 10X10 돌리고
            for i in range(x, 10):
                for j in range(10):
                    # 1을 찾으면
                    if board[i][j] == 1:
                        # 들어갈 수 있는 색종이의 크기 최대값 찾아서 그거부터 체크시작.
                        for num in range(check((i, j)), 0, -1):
                            # 그 크기의 색종이가 아직 존재한다면
                            if paper[num] > 0:
                                inverse((i, j), num)
                                paper[num] -= 1
                                dfs(i)
                                paper[num] += 1
                                inverse((i, j), num)
                        # 한 dfs에는 한 곳만 보면 되니까 return
                        return
    else:
        return

def check(s):
    max_len = min(10-s[0], 10-s[1], 5)
    for k in range(max_len, 0, -1):
        for i in range(s[0], s[0]+k):
            for j in range(s[1], s[1]+k):
                if board[i][j] == 0:
                    break
            if board[i][j] == 0:
                break
        else:
            return k

def inverse(s, m):
    for i in range(s[0], s[0]+m):
        for j in range(s[1], s[1] + m):
            board[i][j] = board[i][j]^1


# 입력 받고
board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
sum_board = sum([sum(board[i]) for i in range(10)])

# 초기값 입력
paper = [0, 5, 5, 5, 5, 5]
res = 25

# 1인 점을 찾고, 사각형 최대값을 찾아서 넣을 수 있는거 다 해! 그럼 끝?
dfs(0)

# 출력
if res == 25:
    print(-1)
else:
    print(res)
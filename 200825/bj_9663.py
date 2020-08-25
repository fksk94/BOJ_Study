# 퀸 놓아보기 함수
def build_queen(n, N) :
    global result           # 글로벌로 생성
    # 재귀 빠져나가기
    if n == N :
        result += 1
        return
    # 재귀 빠져나갈 수 없을 때 퀸을 놓아보고 이전 퀸들과 비교.
    else :
        for i in range(N) :
            row[n] = i
            # for문이 break 걸리지 않고 다 돌면 else(재귀) 실행
            for j in range(n):
                # 한 열에 하나씩 들어가므로 열 바교는 필요없다. 또한 대각선은 수학식을 생각해보면 쉽게 구할 수 있다.
                if row[j] == row[n] or (row[n] - n) == (row[j] - j) or (row[n] + n) == (row[j] + j):
                    break
            else : build_queen(n+1, N)

# 입력
s = int(input())

# 초기값 설정
result = 0
row = [300] * s

# 퀸 놓아보기 함수
build_queen(0, s)

# 출력
print(result)
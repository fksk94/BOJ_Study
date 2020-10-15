# 리스트 풀기
def change(s):
    for i in s:
        if type(i) == type(list()):
            change(i)
        else:
            print(i, end='')

# 후위식 만들기
def gotopost(S, current_cnt):
    for i in range(len(S)):
        if S[i] == '*':
            if tmp_opsign[current_cnt]:
                if tmp_opsign[current_cnt][len(tmp_opsign[current_cnt])-1] == '*' or tmp_opsign[current_cnt][len(tmp_opsign[current_cnt])-1] == '/':
                    postfix.append(tmp_opsign[current_cnt].pop())
                    tmp_opsign[current_cnt].append(S[i])
                else:
                    cnt[current_cnt] += 1
                    tmp_opsign[current_cnt].append(S[i])
            else:
                cnt[current_cnt] += 1
                tmp_opsign[current_cnt].append(S[i])

        elif S[i] == '/':
            if tmp_opsign[current_cnt]:
                if tmp_opsign[current_cnt][len(tmp_opsign[current_cnt])-1] == '*' or tmp_opsign[current_cnt][len(tmp_opsign[current_cnt])-1] == '/':
                    postfix.append(tmp_opsign[current_cnt].pop())
                    tmp_opsign[current_cnt].append(S[i])
                else:
                    cnt[current_cnt] += 1
                    tmp_opsign[current_cnt].append(S[i])
            else:
                cnt[current_cnt] += 1
                tmp_opsign[current_cnt].append(S[i])

        elif S[i] == '+':
            for _ in range(cnt[current_cnt]):
                postfix.append(tmp_opsign[current_cnt].pop())
            cnt[current_cnt] = 1
            tmp_opsign[current_cnt].append(S[i])

        elif S[i] == '-':
            for _ in range(cnt[current_cnt]):
                postfix.append(tmp_opsign[current_cnt].pop())
            cnt[current_cnt] = 1
            tmp_opsign[current_cnt].append(S[i])
        else:
            postfix.append(S[i])

    for _ in range(cnt[current_cnt]):
        postfix.append(tmp_opsign[current_cnt].pop())


S = list(input())
while ')' in S:
    postfix = []
    tmp_opsign = [[] for i in range(100)]
    cnt = [0] * 100
    for i in range(len(S)):
        if len(S) == 1:
            break
        if S[i] == ')':
            for j in range(len(S[:i]), -1, -1):
                if S[j] == '(':
                    gotopost(S[j + 1:i], 0)
                    S = S[:j] + [postfix] + S[i + 1:]
                    break
            break
postfix = []
tmp_opsign = [[] for i in range(100)]
cnt = [0] * 100
gotopost(S, 0)
change(postfix)

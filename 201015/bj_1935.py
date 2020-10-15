import math
# 후위계산
def calculate(postfix):
    i = 2
    while True:
        if postfix[i] == '+':
            postfix[i] = postfix[i - 1] + postfix[i - 2]
            postfix = postfix[:i - 2] + postfix[i:]
            i -= 2
        elif postfix[i] == '*':
            postfix[i] = postfix[i - 1] * postfix[i - 2]
            postfix = postfix[:i - 2] + postfix[i:]
            i -= 2
        elif postfix[i] == '-':
            postfix[i] = postfix[i - 2] - postfix[i - 1]
            postfix = postfix[:i - 2] + postfix[i:]
            i -= 2
        elif postfix[i] == '/':
            postfix[i] = postfix[i - 2] / postfix[i - 1]
            postfix = postfix[:i - 2] + postfix[i:]
            i -= 2
        else:
            i += 1
        if len(postfix) == 1:
            break
    return postfix[0]

N = int(input())
postfix = list(input())
for j in range(N):
    val = float(input())
    for i in range(len(postfix)):
        if type(postfix[i]) == type('a'):
            if ord(postfix[i]) == 65 + j:
                postfix[i] = val
print("{:.2f}".format(calculate(postfix)))
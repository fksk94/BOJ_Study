from sys import stdin
# stdin = open('input.txt', 'r')
input = stdin.readline

n = int(input())
for _ in range(n):
    rs = []
    ls = []
    s = input().rstrip()
    for i in s:
        if i == "<":
            if ls:
                rs.append(ls.pop())
        elif i == ">":
            if rs:
                ls.append(rs.pop())
        elif i == "-":
            if ls:
                ls.pop()
        else:
            ls.append(i)
    print("".join(ls), end="")
    print("".join(reversed(rs)))
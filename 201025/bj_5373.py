def circle(arr, n):
    arr2 = [arr[i][:] for i in range(3)]
    if n == '+':
        for i in range(3):
            for j in range(3):
                arr[i][j] = arr2[2-j][i]
    else:
        for i in range(3):
            for j in range(3):
                arr[i][j] = arr2[j][2-i]

def change(s):
    if s[0] == 'U':
        if s[1] == '-':
            for i in range(3):
                plane2[0][i], plane3[0][i], plane4[0][i], plane5[0][i] = plane3[0][i], plane4[0][i], plane5[0][i], plane2[0][i]
        else:
            for i in range(3):
                plane3[0][i], plane4[0][i], plane5[0][i], plane2[0][i] = plane2[0][i], plane3[0][i], plane4[0][i], plane5[0][i]
        circle(plane1, s[1])
    if s[0] == 'D':
        if s[1] == '+':
            for i in range(3):
                plane2[2][i], plane3[2][i], plane4[2][i], plane5[2][i] = plane3[2][i], plane4[2][i], plane5[2][i], plane2[2][i]
        else:
            for i in range(3):
                plane3[2][i], plane4[2][i], plane5[2][i], plane2[2][i] = plane2[2][i], plane3[2][i], plane4[2][i], plane5[2][i]
        circle(plane6, s[1])
    if s[0] == 'F':
        if s[1] == '+':
            for i in range(3):
                plane1[2][i], plane3[2-i][2], plane6[2][i], plane5[i][0] = plane3[2-i][2], plane6[2][i], plane5[i][0], plane1[2][i]
        else:
            for i in range(3):
                plane3[2-i][2], plane6[2][i], plane5[i][0], plane1[2][i] = plane1[2][i], plane3[2-i][2], plane6[2][i], plane5[i][0]
        circle(plane2, s[1])
    if s[0] == 'B':
        if s[1] == '-':
            for i in range(3):
                plane1[0][2-i], plane3[i][0], plane6[0][2-i], plane5[2-i][2] = plane3[i][0], plane6[0][2-i], plane5[2-i][2], plane1[0][2-i]
        else:
            for i in range(3):
                plane3[i][0], plane6[0][2-i], plane5[2-i][2], plane1[0][2-i] = plane1[0][2-i], plane3[i][0], plane6[0][2-i], plane5[2-i][2]
        circle(plane4, s[1])
    if s[0] == 'L':
        if s[1] == '-':
            for i in range(3):
                plane1[i][0], plane2[i][0], plane6[2-i][2], plane4[2-i][2] = plane2[i][0], plane6[2-i][2], plane4[2-i][2], plane1[i][0]
        else:
            for i in range(3):
                plane2[i][0], plane6[2-i][2], plane4[2-i][2], plane1[i][0] = plane1[i][0], plane2[i][0], plane6[2-i][2], plane4[2-i][2]
        circle(plane3, s[1])
    if s[0] == 'R':
        if s[1] == '+':
            for i in range(3):
                plane1[i][2], plane2[i][2], plane6[2-i][0], plane4[2-i][0] = plane2[i][2], plane6[2-i][0], plane4[2-i][0], plane1[i][2]
        else:
            for i in range(3):
                plane2[i][2], plane6[2-i][0], plane4[2-i][0], plane1[i][2] = plane1[i][2], plane2[i][2], plane6[2-i][0], plane4[2-i][0]
        circle(plane5, s[1])

T = int(input())
for _ in range(T):
    N = int(input())
    order = list(input().split())
    # 1은 2 3 4 5랑 연결 ('U')
    # 6도 2 3 4 5랑 연결 ('D')
    # 2는 4번 빼고 ('F')
    # 4도 2번 빼고 ('B')
    # 3은 5번 빼고 ('L')
    # 5도 3번 빼고 연결 ('R')
    plane1 = [['w'] * 3 for i in range(3)]
    plane2 = [['r'] * 3 for i in range(3)]
    plane3 = [['g'] * 3 for i in range(3)]
    plane4 = [['o'] * 3 for i in range(3)]
    plane5 = [['b'] * 3 for i in range(3)]
    plane6 = [['y'] * 3 for i in range(3)]

    for i in order:
        change(i)

    for i in range(3):
        print(''.join(plane1[i]))

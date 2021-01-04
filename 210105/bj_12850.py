from sys import stdin
import pprint
input = stdin.readline

def mult_mat(a, b):
    tmp = [[0]*8 for i in range(8)]
    for i in range(8):
        for j in range(8):
            for z in range(8):
                tmp[i][j] += a[i][z] * b[z][j]
            tmp[i][j] %= 1000000007
    return tmp

def DAC(cnt):
    if cnt == 1:
        return mat
    elif dic.get(cnt):
        return dic.get(cnt)
    else:
        if cnt % 2:
            tmp = mult_mat(DAC(cnt//2), DAC(cnt//2+1))
            dic[cnt] = tmp
            return tmp
        else:
            tmp = mult_mat(DAC(cnt // 2), DAC(cnt // 2))
            dic[cnt] = tmp
            return tmp


N = int(input())
mat = [[0, 1, 1, 0, 0, 0, 0, 0],
       [1, 0, 1, 1, 0, 0, 0, 0],
       [1, 1, 0, 1, 1, 0, 0, 0],
       [0, 1, 1, 0, 1, 1, 0, 0],
       [0, 0, 1, 1, 0, 1, 0, 1],
       [0, 0, 0, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 1],
       [0, 0, 0, 0, 1, 0, 1, 0]]
dic = {}
print(DAC(N)[0][0])
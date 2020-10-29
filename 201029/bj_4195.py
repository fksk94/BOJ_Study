from sys import stdin

def find(i):
    if networks[i] == i:
        for j in arr:
            networks[j] = i
        return i
    else:
        arr.append(i)
        return find(networks[i])

def union(a, b):
    global arr
    a = find(a)
    arr = []
    b = find(b)
    arr = []

    if a != b:
        networks[b] = a
        nums[a] += nums[b]
        nums[b] = 1

    return nums[a]


# 테케 갯수 입력
T = int(input())
# 배열, 결과 초기화, 입력
res = 0
for _ in range(T):
    TT = int(input())
    networks = [i for i in range(200002)]
    nums = [1] * 200002
    friend_dic = {}
    cnt = 1
    arr = []
    for __ in range(TT):
        a, b = stdin.readline().rstrip().split()
        if not friend_dic.get(a):
            friend_dic[a] = cnt
            cnt += 1
        if not friend_dic.get(b):
            friend_dic[b] = cnt
            cnt += 1
        print(union(friend_dic[a], friend_dic[b]))
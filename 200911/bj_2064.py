import sys, re
def solution():
    T = int(sys.stdin.readline())
    ips = [sys.stdin.readline().rstrip() for i in range(T)]
    ip = []
    net_addr = []
    net_mask = []
    all_of_mask = []

    # ip 나눠서 받고
    for j in range(4):
        ip += [[int(re.findall('\d+', i)[j]) for i in ips]]

    # 그냥 나눠서 받을 거를 이진수로 바꾼다음,  스트링형태로 바꾸면..?
    # 되긴 되겟지만... 이게 좋은 건가...? 32 * 1000 * 4 * 10 정도라고 치면 시간은 별로 안 들긴 하네
    #

    # ip 4파트 비교
    for part in ip:
        visited = [True] * 8
        tmp = part[0]

        # 초기값잡아주고 그값에서 visited에 False 되어있는 곳 다 0으로 만들 계획
        for i in range(1, len(part)):
            tmp = tmp & part[i]
        str_tmp = str(format(tmp, 'b'))
        while True:
            if len(str_tmp) == 8 :
                break
            else :
                str_tmp = '0'+str_tmp

        # 문자변환
        for jjip in range(len(part)) :
            str_jjip = str(format(part[jjip], 'b'))
            while True:
                if len(str_jjip) == 8 :
                    break
                else :
                    str_jjip = '0'+str_jjip
            part[jjip] = str_jjip

        # visited에 False 삽입
        for k in range(1, len(part)):
            for i in range(8):
                if part[0][i] != part[k][i]:
                    visited[i] = False
        mask = '11111111'
        for i in range(len(visited)):
            if visited[i] == False :
                sig = False
                str_tmp = str_tmp[:i] + '0'*(8-i)
                mask = mask[:i] + '0'*(8-i)
                break
        for i in net_mask:
            if i != '255':
                mask = '00000000'
                str_tmp = '00000000'
        net_addr.append(str(int(str_tmp,2)))
        net_mask.append(str(int(mask,2)))

    # 출력
    print('.'.join(net_addr))
    print('.'.join(net_mask))

solution()
from itertools import permutations
def check():
    for i in range(1, len(N) + 1):
        per = permutations(numbers, i)
        for j in per:
            a = int("".join(j))
            num = N_N - a
            if num < 1:
                continue
            tmp = str(num)
            for k in tmp:
                if k in j:
                    break
            else:
                if int(tmp) == 0 or a == 0:
                    continue
                if len(set(list(tmp))) == len(tmp):
                    return (tmp, "".join(j))
    return False

N = input()
N_N = int(N)
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

ans = check()
if ans:
    print(ans[0] + " + " + ans[1])
else:
    print(-1)
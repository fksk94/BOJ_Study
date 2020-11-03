B, C, D = map(int, input().split())
A1, A2 = map(int, input().split())
E1, E2 = map(int, input().split())
low = A1/A2
high = E1/E2
Bstart, Bend = int(low * B), int(high * B)
Cstart, Cend = int(low * C), int(high * C)
Dstart, Dend = int(low * D), int(high * D)
if Bstart * A2 <= A1*B:
    Bstart += 1
if Cstart * A2 <= A1*C:
    Cstart += 1
if Dstart * A2 <= A1*D:
    Dstart += 1

if Bend * E2 >= E1*B:
    Bend -= 1
if Cend * E2 >= E1*C:
    Cend -= 1
if Dend * E2 >= E1*D:
    Dend -= 1


cnt1, cnt2 = 0, 0
i=Bstart
tmp = [(Cstart, Dstart)]
j, k = tmp[0][0], tmp[0][1]
res =0
while Cstart <= j <= Cend:
    cnt1, cnt2 = 0, 0
    while Bstart <= i <= Bend:
        if i * C < j * B:
            i += 1
        else:
            cnt1 = i - Bstart
            break
    else:
        cnt1 = i - Bstart
    while Dstart <= k <= Dend:
        if k * C <= j * D:
            k += 1
        else:
            cnt2 = Dend - k +1
            break
    res += cnt1*cnt2
    j+=1


print(res)
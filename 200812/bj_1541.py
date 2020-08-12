s = input()
start = 0
end = s[-1]
tmp_sum = 0
result = 0
sig = False
for i in range(len(s)) :
    if s[i] == '+' :
        end = i
        tmp_sum += int(s[start:end])
        start = i+1
    elif s[i] == '-' :
        end = i
        tmp_sum += int(s[start:end])
        if sig == False :
            result += tmp_sum
            sig = True
        else :
            result -= tmp_sum
        start = i+1
        tmp_sum = 0
    elif i == len(s)-1 :
        end = i+1
        tmp_sum += int(s[start:end])
        if sig == False :
            result += tmp_sum
            sig = True
        else :
            result -= tmp_sum

print(result)
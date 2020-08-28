def TSP(goto, cost) :
    dict_check['visit_plan'].remove(goto)
    if len(dict_check['visit_plan']) == 0 :
        if arr[goto][dict_check['start-end']] == 0:
            pass
        elif result[0] > cost + arr[goto][dict_check['start-end']] :
            result[0] = cost + arr[goto][dict_check['start-end']]
        dict_check['visit_plan'].append(goto)
        return
    else :
        for x in dict_check['visit_plan'] :
            if arr[goto][x] == 0 :
                continue
            if result[0] > cost+arr[goto][x] :
                TSP(x, cost+arr[goto][x])
        dict_check['visit_plan'].append(goto)
        return

s = int(input())
arr = []
for _ in range(s) :
    arr.append(list(map(int, input().split())))

result = [10000000000000]
for i in range(s) :
    for j in range(s) :
        if i == j :
            continue
        else :
            dict_check = {
                'visit_plan' : [_ for _ in range(s)]
            }
            if arr[i][j] == 0 :
                continue
            dict_check['start-end'] = i
            dict_check['visit_plan'].remove(i)
            TSP(j, arr[i][j])

print(result[0])
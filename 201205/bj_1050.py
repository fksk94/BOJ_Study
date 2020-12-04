from collections import defaultdict
import re

# 재료, 레시피 개수 입력
N, M = map(int, input().split())
# 재료 입력
goods = [tuple(input().split()) for i in range(N)]

# 재료나 포션의 가격 딕셔너리
potions = defaultdict(list)
for name, cost in goods:
    potions[name].append(int(cost))

# 레시피를 위해 잠시 저장할 공간
recipes = []
ingredients_count = []
love_portions = []
love_portions_count = []

# 레시피 입력 Love 포션은 마지막에 함
for i in range(M):
    data = input()
    wait_check = re.split(r'.[0-9]', data)
    if wait_check[0] == 'LOVE':
        love_portions.append(wait_check)
        love_portions_count.append(re.findall(r'[0-9]', data))
    else:
        recipes.append(re.split(r'.[0-9]', data))
        ingredients_count.append(re.findall(r'[0-9]', data))
cnt = 0

# 순서대로 하는데.. 문제점이 있다. 나중에 더 작은 값의 상황이 나온다면 어떻게 되는 거지?
# 그럼 레시피를 안없애고 해보자.
while cnt < 51:
    idx = 0
    while idx < len(recipes):
        tmp_cost = 0
        for i in range(1, len(recipes[idx])):
            if potions.get(recipes[idx][i]):
                tmp_cost += min(potions.get(recipes[idx][i]))*int(ingredients_count[idx][i-1])
            else:
                break
        else:
            potions[recipes[idx][0]].append(tmp_cost)
        idx += 1
    cnt += 1
res = []
for i in range(len(love_portions)):
    tmp_cost = 0
    for j in range(1, len(love_portions[i])):
        if potions.get(love_portions[i][j]):
            tmp_cost += min(potions.get(love_portions[i][j]))*int(love_portions_count[i][j-1])
        else:
            break
    else:
        potions['LOVE'].append(tmp_cost)

res = potions.get('LOVE')
if res:
    if min(res) > 1000000000:
        print(1000000001)
    else:
        print(min(res))
else:
    print(-1)


def solution():
    T = int(input())
    arr = list(map(int, input().split()))
    cnt = 1
    result = []
    for i in range(T-1):
        if arr[i] <= arr[i+1]:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
    result.append(cnt)
    cnt = 1
    for i in range(len(arr)-1):
        if arr[i] >= arr[i+1]:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 1
    result.append(cnt)
    return max(result)

print(solution())
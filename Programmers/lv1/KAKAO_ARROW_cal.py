def compare(arr1, arr2):
    idx = 10
    while idx >= 0:
        if arr1[idx] > arr2[idx]:
            return 1
        elif arr1[idx] < arr2[idx]:
            return 0
        else:
            idx -= 1
        #print("<compare> idx = {0} / arr1[{0}] = {1} / arr2[{0}] = {2}".format(idx, arr1[idx], arr2[idx]))
    return -1

def cal(arr1, arr2):
    res = 0
    for i in range(len(arr2)):
        if arr1[i] > arr2[i]:
            res += 10 - i
            #print("<cal> arr1[{0}] = {2} > arr2[{0}] = {3}  >>>>>>  res = {1}(+10 - i({0}))".format(i, res, arr1[i], arr2[i]))
        elif arr1[i] < arr2[i]:
            res -= 10 - i
    return res

def dfs(info, idx, cand, arr, n):
    #print("<dfs> info={0}, idx={1}, cand={2}, arr={3}, n={4}".format(info, idx, cand, arr, n))
    if idx == 10 and n >= 0:
        cur = arr + [n]
        #print("<dfs> cur={0}, info={1}, [n]={2}".format(cur, info, [n]))
        total = cal(cur, info)
        #print("<dfs> total = ", total)
        if total > cand[0]:
            cand[0] = total
            cand[1] = cur
        elif total == cand[0]:
            if compare(cur, cand[1]):
                cand[1] = cur

    if n < 0 or idx == 11:
        return

    dfs(info, idx + 1, cand, arr + [info[idx] + 1], n - (info[idx] + 1))
    dfs(info, idx + 1, cand, arr + [0], n)

def solution(n, info):
    answer = []
    cand = [0, [0] * 11]
    dfs(info, 0, cand, [], n)
    if cand[0] == 0:
        return -1
    else:
        return cand[1]

n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
print(solution(n, info))









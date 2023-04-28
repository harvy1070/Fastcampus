def solution(X, Y):
    answer = []
    xDict = dict()
    yDict = dict()

    for x in X:
        xDict[x] = xDict.get(x, 0) + 1
    for y in Y:
        yDict[y] = yDict.get(y, 0) + 1
    # print("1. xDict = {0} / yDict = {1}".format(xDict, yDict))
    # xDict의 키를 기준으로 탐색, 짝꿍이 있다면 xDict와 yDict에서 -1 해주고 answer에 추가하기
    for k, v in xDict.items():
        # print("2. k = {0}, v = {1}".format(k, v))
        if k in yDict.keys():
            while yDict[k] > 0 and xDict[k] > 0:
                answer.append(k)
                yDict[k] = yDict.get(k) - 1
                xDict[k] = xDict.get(k) - 1
                # print("3. answer = {0}, xDict = {2} , yDict = {1}".format(answer, yDict, xDict))
    # 아무것도 없을 경우 -1 return
    if len(answer) == 0:
        return "-1"
    # answer에 0밖에 없을 경우 0 return
    if answer.count('0') == len(answer):
        return "0"

    answer.sort(reverse=True)
    return ''.join(answer)

X = "12321"
Y = "42531"
print(solution(X, Y))

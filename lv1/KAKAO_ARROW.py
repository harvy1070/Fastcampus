from collections import deque
def bfs(n, info):
    res = []
    q = deque([(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])])
    maxGap = 0

    while q:
        focus, arrow = q.popleft()
        print("<bfs> 1. focus = {0}, arrow = {1}".format(focus, arrow))
        print("<bfs> 2. sum(arrow) = {0}, n = {1}".format(sum(arrow), n))
        if sum(arrow) == n:
            apeach, lion = 0, 0
            for i in range(11):
                if not (info[i] == 0 and arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
                print("<bfs> 3. info[{0}] = {3}, arrow[{0}] = {4} / apeach = {1}, lion = {2}".format(i, apeach, lion, info[i], arrow[i]))
            if apeach < lion: # 라이언 승리시
                gap = lion - apeach
                print("<bfs> 4. *** lion win *** \n gap({0}) = lion({1}) - apeach({2})".format(gap, lion, apeach))
                if maxGap > gap:
                    continue
                if maxGap < gap:
                    maxGap = gap
                    res.clear()
                res.append(arrow)
        elif sum(arrow) > n: # 화살을 더 쏜 경우
            continue

        elif focus == 10: # 화살을 덜 쏜 경우
            tmp = arrow.copy()
            #print("<bfs> *** elif 덜 쏜 경우 *** \n tmp = {0}".format(tmp))
            tmp[focus] = n - sum(tmp)
            q.append((-1, tmp))
            #print("<bfs> *** elif 덜 쏜 경우 *** \n q.append((-1, tmp)) = {0}".format(q))

        else:
            tmp = arrow.copy()
            #print("<bfs> *** else 화살 쏘기 *** \n tmp = {0}".format(tmp))
            tmp[focus] = info[focus] + 1
            q.append((focus + 1, tmp)) # 어피치보다 1발 많이 쏘기
            #print("<bfs> *** else 화살 쏘기(어피치보다 1발 많이) *** \n q = {0}".format(q))
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            q.append((focus+1, tmp2)) # 0발 쏘기
            #print("<bfs> *** else 화살 쏘기(0발 쏘기) *** \n q = {0}".format(q))
    return res

def solution(n, info):
    winList = bfs(n, info)

    if not winList:
        return -1
    elif len(winList) == 1:
        return winList[0]
    else:
        return winList[-1]

n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]

print(solution(n, info))
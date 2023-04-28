from collections import deque
def solution(places):
    answer = []

    for p in places:
        key = False
        nowArr = []
        print("1. p = ", p)
        for n in p:
            print("2. n = ", n)
            nowArr.append(list(n))

        for i in range(5):
            print("3. i = ", i)
            if key:
                break
            for j in range(5):
                print("4. j = ", j)
                if key:
                    break
                if nowArr[i][j] == "P":
                    if i + 1 < 5:
                        if nowArr[i+1][j] == "O":
                            if i + 2 < 5:
                                if nowArr[i+2][j] == "P":
                                    key = True
                                    break
                    if j+1 < 5:
                        if nowArr[i][j+1] == "P":
                            key = True
                            break
                        if nowArr[i][j+1] == "O":
                            if j+2 < 5:
                                if nowArr[i][j+2] == "P":
                                    key = True
                                    break
                    if i + 1 < 5 and j + 1 < 5:
                        # 만약 우측 아래가 사람이고, 오른 쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i + 1][j + 1] == "P" and (nowArr[i + 1][j] == "O" or nowArr[i][j + 1] == "O"):
                            key = True;
                            break;

                        # 좌측 아래부분입니다.
                    if i + 1 < 5 and j - 1 >= 0:
                        # 만약 좌측 아래가 사람이고, 왼쪽 또는 아랫부분중 하나라도 빈테이블이면 break
                        if nowArr[i + 1][j - 1] == "P" and (nowArr[i + 1][j] == "O" or nowArr[i][j - 1] == "O"):
                            key = True;
                            break;

        if key:
            answer.append(0)
        else:
             answer.append(1)
    return answer

def bfs(p, idx):
    q = deque([idx])
    visited = [[False] * 5 for _ in range(5)]
    dic = {0:[0, 1], 1:[-1, 0], 2:[0, 1], 3:[1, 0]}

    while q:
        x, y, d = q.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dic[i][0]
            ny = y + dic[i][1]
            nd = d + 1

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                visited[nx][ny] = True

                if p[nx][ny] == 'P':
                    if nd <= 2:
                        return False
                elif p[nx][ny]== 'O':
                    if nd == 1:
                        q.append([nx, ny, nd])
    return True

def solution2(places):
    answer = []
    for p in places:
        flag = 1

        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    result = bfs(p, [i, j, 0])
                    if not result:
                        flag = 0
            answer.append(flag)
    return answer

def check_distance(place):
    # P값의 좌표를 plist에 담는다
    plist = [(y, x) for y in range(5) for x in range(5) if place[y][x] == 'P']
    print("<check_distance> 1. plist = ", plist)

    # 각 좌표 거리 계산, 거리에 따라 거리두기 여부 판단
    for y, x in plist:
        print("<check_distance> 2. y = {0} / x = {1}".format(y, x))
        print("<check_distance> 5. place[{0}][{1}] = {2}".format(y, x, place[y][x]))
        for y2, x2 in plist:
            print("<check_distance> 3. y2 = {0} / x2 = {1}".format(y2, x2))
            dist = abs(y-y2) + abs(x-x2) # 맨해튼 거리
            print("<check_distance> 4. abs({0}-{1}) + abs({2}-{3}) = dist({4})".format(y, y2, x, x2, dist))
            print("<check_distance> 5. place[{0}][{1}] = {2}".format(y2, x2, place[y2][x2]))
            if dist == 0 or dist > 2:
                continue
            if dist == 1: # 두 사람의 거리가 1인 경우
                return 0
            elif y == y2 and place[y][int((x+x2)//2)] != 'X': # 열은 같으나 두 사람 사이에 파티션이 없는 경우
                return 0
            elif x == x2 and place[int((y+y2)//2)][x] != 'X': # 행이 같으나 두 사람 사이에 파티션이 없는 경우
                return 0
            elif y != y2 and x != x2: # 열 / 행이 다른경우(대각선), 두 사람 사이에 파티션이 없는 경우
                if place[y2][x] != 'X' or place[y][x2] != 'X':
                    return 0
    return 1

def solution3(places):
    answer = []
    for p in places:
        print("<solution> 1. p = ", p)
        answer.append(check_distance(p))
        print("<solution> 2. answer = ", answer)
    return answer

places = 	[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
             ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
             ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
             ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
             ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution3(places))
def solution(m, n, board):
    for i in range(m):
        board[i] = list(board[i])
    #print(board)

    cnt = 0
    rm = set()
    while True:
        # board 순회, 4블록이 된 곳 좌표를 집합에 기록
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                #print(t)
                if t == []:
                    continue
                elif board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
                    rm.add((i, j))
                    rm.add((i+1, j))
                    rm.add((i, j+1))
                    rm.add((i+1, j+1))
                    print(rm)
        # 좌표 존재 시, 집합의 길이만큼 세고 블록을 지움
        #print(rm)
        if rm:
            cnt += len(rm)
            for i, j in rm:
                board[i][j] = []
            rm = set()
        # 없다면 함수 종료
        else:
            return cnt

        # 블록을 위에서 아래로 당겨줌
        #print(board)
        while True:
            moved = 0
            for i in range(m - 1):
                for j in range(n):
                    if board[i][j] and board[i + 1][j] == []:
                        board[i + 1][j] = board[i][j]
                        board[i][j] = []
                        moved = 1
            if moved == 0:
                break

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

print(solution(m, n, board))
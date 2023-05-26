def solution(board):
    n = len(board)
    m = len(board[0])

    # dp ready
    dp = [[0] * m for _ in range(n)]
    #print("1. base(dp) = ", dp)
    dp[0] = board[0]
    for i in range(1, n):
        dp[i][0] = board[i][0]
        #print("2. dp[{0}][0] = board[{0}][0] / dp[{0}][0] = {1}".format(i, board[i][0]))

    for i in range(1, n):
        for j in range(1, m):
            #print("3. board[{0}][{1}] = {2}".format(i, j, board[i][j]))
            if board[i][j] == 1:
                print("board[{0}][{1}] == 1".format(i, j))
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                #print("4. <board == 1> dp[{0}][{1}] = {2}".format(i, j, dp[i][j]))
                #print("5. <result1> dp[{0}][{1}] = {2}".format(i, j, dp[i][j]))
                print("dp[{0}][{1}] = min(dp[{0}-1][{1}-1], dp[{0}-1][{1}], dp[{0}][{1}-1]) + 1".format(i, j))
                print("dp[{0}][{1}] = min({2}, {3}, {4}) + 1".format(i, j, dp[i-1][j-1], dp[i-1][j], dp[i][j-1]))
                print("dp = ", dp)
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        #print("temp<max(dp[{0}])> = {1}".format(i, max(dp[i])))
        answer = max(answer, temp)
        #print("answer = ", answer)
    #print("***=== result = dp ===***", dp)
    return answer ** 2

board = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
print(solution(board))
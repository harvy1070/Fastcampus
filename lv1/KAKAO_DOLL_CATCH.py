# def solution(board, moves):
#     stacklist = []
#     answer = 0
#
#     for m in moves:
#         for i in range(len(board)):
#             # print("1. moves(m) > {0}, i > {1}".format(m, i))
#             if board[i][m-1] != 0:
#                 stacklist.append(board[i][m-1])
#                 board[i][m-1] = 0
#                 if len(stacklist) > 1:
#                     if stacklist[-1] == stacklist[-2]:
#                         stacklist.pop(-1)
#                         stacklist.pop(-1)
#                         answer += 2
#                         # print("3. stacklist >> {0}, answer >> {1}".format(stacklist, answer))
#                 break
#     return answer

def solution(board, moves):
    stacklist = []
    answer = 0

    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0:
                stacklist.append(board[i][m-1])
                board[i][m-1] = 0
                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                break
    return answer

board = [
	[0,0,0,0,0],
	[0,0,1,0,3],
	[0,2,5,0,1],
	[4,2,4,4,2],
	[3,5,1,3,1]
	]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))
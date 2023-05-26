# # lv2. game map
#
# from collections import deque
# def solution(maps):
#     answer = 0
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     def bfs(x, y):
#         queue = deque()
#         queue.append((x, y))
#         while queue:
#             x, y = queue.popleft()
#             #print(x, y)
#             print(queue)
#             for i in range(4):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 # 맵 벗어나면 무시
#                 if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue
#
#                 # 벽 무시
#                 if maps[nx][ny] == 0: continue
#
#                 # 처음 가는 길이면 거리계산 후 다시 상하좌우 확인
#                 if maps[nx][ny] == 1:
#                     maps[nx][ny] = maps[x][y] + 1
#                     queue.append((nx, ny))
#
#         return maps[len(maps)-1][len(maps[0])-1]
#     answer = bfs(0, 0)
#     return -1 if answer == 1 else answer
#
# maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
# print(solution(maps))

# 2 x n 타일
def solution(n):
    dp = [1] * (n+1)
    dp[1] = 1
    print(dp)
    for i in range(2, n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 1000000007
        print(dp[i-1])
    return dp[n]

n = 4
print(solution(n))
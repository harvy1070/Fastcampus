from collections import deque
def solution(maps):
    answer = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        #print("1. queue = ", queue)
        queue.append((x, y))
        #print("2. queue.append = ", queue)

        while queue:
            #print("3. (queue.popleft())x, y = ", x, y)
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                #print("4. nx, ny = ", nx, ny)

                if nx < 0 or nx >= len(maps) or ny < 0 or ny >= len(maps[0]): continue

                if maps[nx][ny] == 0: continue

                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    #print("5. maps[nx][ny] = ", maps[nx][ny])
                    queue.append((nx, ny))
                    print("6. (if == 1)queue = ", queue)

        return maps[len(maps)-1][len(maps[0])-1]
    answer = bfs(0, 0)
    return -1 if answer == 1 else answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))
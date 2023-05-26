# MAP
# n = int(input())
# x, y = 1, 1
# plans = input().split()
# # L R U D 이동방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']
#
# for p in plans:
#     for i in range(len(move_types)):
#         if p == move_types[i]:
#             nx = x + dx[i]
#             print("nx = ", nx)
#             ny = y + dy[i]
#             print("ny = ", ny)
#
#         # 공간을 벗어나는 경우
#     if nx < 1 or ny < 1 or nx > n or ny > n:
#         continue
#
#     x, y = nx, ny
# print(x,y)

# TIME '3'이 들어간 시간 세기
# h = int(input())
#
# cnt = 0
# for i in range(h + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 cnt += 1
# print(cnt)

# king of knight
# start = 'c7'
# row = int(start[1])
# column = int(ord(start[0])) - int(ord('a')) + 1
# print("column = ", column)
# # 나이트가 이동할 수 있는 방향 정의(L자로 상하좌우 움직임)
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# result = 0
# for s in steps:
#     next_row = row + s[0]
#     next_column = column + s[1]
#
#     # 해당 위치로 이동 가능하면 cnt 증가
#     if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
# print(result)

# game develop

n, m = map(int, input().split())
# 맵을 생성한 후 0으로 초기화
d = [[0] * m for _ in range(n)]
# 캐릭터의 현재 위치, 방향 입력받기
x, y, direction = map(int, input().split())
# 전체 맵 정보 입력받기
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
# 북동남서 방향 정의 0 북(상) 1 동(우) 2 남(하) 3 서(좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
cnt = 0
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    print(d)
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있으면 뒤로 가기
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다인 경우
        else:
            break
        turn_time = 0
print(cnt)






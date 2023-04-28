# def solution(park, routes):
#     x, y = 0, 0
#     # park의 S = 시작점이 어딘지 파악하는 for문
#     for i in range(len(park)):
#         for j in range(len(park[i])):
#             if park[i][j] == 'S':
#                 x = i
#                 y = j
#                 break
#     print("1. x = {0}, y = {1}".format(x, y))
#
#     for i in routes:
#         a, b = x, y
#         print("2. i = {0}, a = {1}, b = {2}".format(i, a, b))
#         for j in range(int(i[2])):
#             print("3. j = {0}, a = {1}, b = {2}".format(j, a, b))
#             if i[0] == 'N' and b != 0 and park[b-1][a] != 'X':
#                 b -= 1
#                 if j == int(i[2]) - 1:
#                     y = b
#                     print("4-1(if/N). b = {0} / y = {1}".format(b, y))
#             elif i[0] == 'S' and b != len(park)-1 and park[b+1][a] != 'X':
#                 b += 1
#                 if j == int(i[2]) - 1:
#                     y = b
#                     print("4-2(if/S). b = {0} / y = {1}".format(b, y))
#             elif i[0] == 'W' and a != 0 and park[b][a-1] != 'X':
#                 a -= 1
#                 if j == int(i[2]) - 1:
#                     x = a
#                     print("4-3(if/W). a = {0} / x = {1}".format(a, x))
#             elif i[0] == 'E' and a != len(park[0]) - 1 and park[b][a+1] != 'X':
#                 a += 1
#                 if j == int(i[2]) - 1:
#                     x = a
#                     print("4-4(if/E). a = {0} / x = {1} / len(park[0]) = {2}".format(a, x, len(park[0])))
#     return [x, y]

# solution2 // class 활용한 솔루션
# class Dog:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.g = {"N": (-1, 0), "W": (0, -1), "E": (0, 1), "S": (1, 0)}
#
#     def move(self, park, direction, distance):
#         i, j = self.g[direction]
#         x, y = self.x + (i * distance), self.y + (j * distance)
#         if x < 0 or y < 0 or x >= len(park) or y >= len(park[0]):
#             return park
#         elif "X" in park[x][min(self.y, y) : max(self.y, y) + 1] or "X" in [
#             row[y] for row in park[min(self.x, x) : max(self.x, x)]
#         ]:
#             return park
#         park[self.x][self.y] = "O"
#         park[x][y] = "S"
#         self.x = x
#         self.y = y
#         return park
#
#     @classmethod
#     def detect_start_dogs_location(self, park):
#         for i, row in enumerate(park):
#             for j, item in enumerate(row):
#                 if item == "S":
#                     return i, j
#
#
# def solution(park, routes):
#     park = [list(row) for row in park]
#     x, y = Dog.detect_start_dogs_location(park)
#
#     dog = Dog(x, y)
#
#     for route in routes:
#         direction, distance = route.split()
#         park = dog.move(park, direction, int(distance))
#
#     return [dog.x, dog.y]

def solution(park, routes):
    x = 0
    y = 0

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x = j
                y = i
                break

    for route in routes:
        # 위치 초기화
        xx = x
        yy = y
        # 이동 - 장애물이 있거나 공원을 벗어나면 명령 무시
        for step in range(int(route[2])):
            # 동쪽 : 현재 위치가 map 가장 오른쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            if route[0] == 'E' and xx != len(park[0]) - 1 and park[yy][xx+1] != 'X':
                xx += 1
                if step == int(route[2]) - 1:
                    x = xx # step 만큼 움직였으면 위치 초기화
            # 서쪽 : 현재 위치가 map 가장 왼쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'W' and xx != 0 and park[yy][xx-1] != 'X':
                xx -= 1
                if step == int(route[2]) - 1:
                    x = xx
            # 남쪽 : 현재 위치가 map 가장 아래쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'S' and yy != len(park[0]) - 1 and park[yy+1][xx] != 'X':
                yy += 1
                if step == int(route[2]) - 1:
                    y = yy
            # 북쪽 : 현재 위치가 map 가장 위쪽이면 안됨, 이동할 곳이 장애물이면 안됨
            elif route[0] == 'N' and yy != 0 and park[yy-1][xx] != 'X':
                yy -= 1
                if step == int(route[2]) - 1:
                    y = yy
    return [y, x]


park = ["OOS", "OOO", "OOO"]
routes = ["E 2", "S 2", "W 1"]
print(solution(park, routes))

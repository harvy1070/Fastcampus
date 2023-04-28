# 재귀함수
# def recursive_function(i):
#     if i == 100:
#         return
#     print(i, '번째 재귀 함수에서', i+1,'번째 재귀 함수를 호출')
#     recursive_function(i + 1)
#     print(i, '번째 재귀 함수 종료')
# recursive_function(1)

# 재귀함수를 이용한 팩토리얼
# def factorial_iterative(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
#
# def factorial_recursive(n):
#     if n<=1:
#         return 1
#     else:
#         return n * factorial_iterative(n-1)
#
# print(factorial_iterative(5))
# print(factorial_recursive(5))

# DFS(깊이우선탐색)
# inf = 999999999
#
# graph = [
#     [0, 7, 5],
#     [7, 0, inf],
#     [5, inf, 0]
# ]
#
# print(graph)

# 인접리스트
# graph = [[] for _ in range(3)]
# print(graph)
# graph[0].append((1, 7))
# graph[0].append((2, 5))
# print(graph)
# graph[1].append((0, 7))
#
# graph[2].append((0, 5))
# print(graph)

# DFS / BFS
# from collections import deque
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=' ')
#
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# def bfs(graph, start, visited):
#     queue = deque([start])
#
#     visited[start] = True
#
#     while queue:
#         v = queue.popleft()
#         print(v, end = ' ')
#
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]
# visited = [False] * 9
# #dfs(graph, 1, visited)
# bfs(graph, 1, visited)

# make a icecream

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        # 상하좌우 위치 재귀호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)

















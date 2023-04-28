from collections import defaultdict
def solution(tickets):
    visited = defaultdict(list)
    graph = defaultdict(list)
    start = "ICN"
    goal = len(tickets) + 1
    answer = []
    # print("<solution> goal = {0}".format(goal))

    for t in tickets:
        # print("<solution/for1> 1-1. t = {0}".format(t))
        graph[t[0]].append(t[1])
        # print("<solution/for1> 1-2. graph = {0}".format(graph))
        visited[t[0]].append(False)
        # print("<solution/for1> 1-3. visited = {0}".format(visited))
    print("graph = ", graph)
    print("visited = ", visited)
    def dfs(now, path):
        nonlocal goal
        # print("<dfs> 1. now(airport) = {0} / path([start, airport]) = {1}".format(now, path))
        if len(path) == goal:
            answer.append(path)
            # print("<dfs/if> 2. len(path):{0} == goal:{1} >> answer:{2}".format(len(path), goal, answer))
            return 0
        for j in range(len(graph[now])):
            # print("<dfs/for> 3. j = {0} / graph[now] = {1}".format(j, graph[now]))
            if not visited[now][j]:
                nxt = graph[now][j]
                # print("<dfs/for/if> 4-1. visited[now][j] = {0}, nxt = {1}".format(visited[now][j], nxt))
                visited[now][j] = True
                # print("<dfs/for/if> 4-2. visited[{0}][{1}] = {2}".format(now, j, visited[now][j]))
                dfs(nxt, path + [nxt])
                visited[now][j] = False
                # print("<dfs/for/if> 4-3. visited[{0}][{1}] = {2}".format(now, j, visited[now][j]))

    for i in range(len(graph[start])):
        # print("<solution/for/2> 2-1. i = {0} / graph[start] = {1}".format(i, graph[start]))
        airport = graph[start][i]
        visited[start][i] = True
        # print("<solution/for2> 2-2. airport = {0} / visited[{1}][{2}] = {3}".format(airport, start, i, visited[start][i]))
        dfs(airport, [start, airport])
        visited[start][i] = False
        # print("<solution/for2> 2-3. visited[start][i] = False")
        # print(">>> visited[{0}][{1}] = {2}".format(start, i, visited[start][i]))

    answer.sort()
    return answer[0]

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

print(solution(tickets))









def solution(n, computers):
    def dfs(v):
        visited[v] = True
        print("<dfs> 1. visited[{0}] = {1}".format(v, visited[v]))
        for nei in range(n):
            print("<dfs> 2-1. nei = {0}, visited[{0}] = {1}".format(nei, visited[nei]))
            print("<dfs> 2-2. v = {0}, nei = {1}, computers[{0}][{1}]".format(v, nei, computers[v][nei]))
            if not visited[nei] and computers[v][nei]:
                dfs(nei)
                print("<dfs> 3. dfs({0})".format(nei))
    count = 0
    visited = [False] * (n)
    print("<solution> 1. visited = {0}".format(visited))

    for node_idx in range(n):
        print("<solution> 2. node_idx = {0}, visited[{0}]".format(node_idx, visited[node_idx]))
        if not visited[node_idx]:
            dfs(node_idx)
            count += 1
            print("<solution> 3. count = {0}".format(count))
    return count

def dfs(graph, v, visited):
    visited[v] = True
    n = len(graph)

    for node in range(n):
        if graph[v][node] == 1 and visited[node] == False:
            dfs(graph, node, visited)

def solution2(n, computers):
    answer = 0
    visited = [0] * n

    for s in range(n):
        if visited[s] == 0:
            dfs(computers, s, visited)
            answer += 1
    return answer


n = 3
computers = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]

print(solution2(n, computers))
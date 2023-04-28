from collections import deque
def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    print("<bfs> 1. q = {0}".format(q))
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        print("<bfs/while> 2-1. q = {0} / value = {1} / v = {2} / count = {3}".format(q, value, v, count))
        print("<bfs/while> 2-2. visited = {0}".format(visited))
        if visited[v] == -1:
            visited[v] = count
            count += 1
            print("<bfs/while/if> 3. visited[{0}] = {1} / count = {2}".format(v, visited[v], count))
            for e in adj[v]:
                print("<bfs/while/if/for> 4-1. e = {0} / adj = {1} / v = {2}".format(e, adj, v))
                q.append([e, count])
                print("<bfs/while/if/for> 4-2. q = {0} / e = {1} / count {2}".format(q, e, count))
def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1)
    adj = [[] for _ in range(n+1)]
    print("<solution> 1. visited = {0} / adj = {1}".format(visited, adj))

    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
        print("<solution/for1> 2. x = {0} / y = {1} / adj = {2}".format(x, y, adj))

    bfs(1, visited, adj)

    for value in visited:
        print("<solution/for2> 3. visited = {0}".format(visited))
        if value == max(visited):
            answer += 1
            print("<solution/for2/if> 4. value = {0} / max(visited) = {1} / answer = {2}".format(value, max(visited), answer))
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))


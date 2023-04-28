from collections import deque
def solution(n, edge):
    adj = [[] for _ in range(n+1)]
    visit = [0] * (n+1)
    print("<setting> adj = {0} , visit = {1}".format(adj, visit))

    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
        print("1-1. adj[{0}].append({1}) : {2}".format(a, b, adj[a]))
        print("1-2. adj[{0}].append({1}) : {2}".format(b, a, adj[b]))
        print(">>> adj = {0}".format(adj))
    visit[1] = 1
    q = deque([1])
    #print("2. q = {0}".format(q))

    while q:
        print("2. q = {0}".format(q))
        x = q.popleft()
        print("3. x = {0}".format(x))
        for n in adj[x]:
            print("4. n = {0} / adj[{1}] >>> {2}".format(n, x, adj))
            if not visit[n]:
                visit[n] = visit[x] + 1
                print("5-1. visit = {0} >>> visit[x] + 1".format(visit))
                q.append(n)
                print("5-2. q = {0}".format(q))
    max_v = max(visit)
    print("6. max_v = {0}".format(max_v))
    cnt = visit.count(max_v)
    print("7. cnt = {0}".format(cnt))
    return cnt if cnt > 0 else 1

def bfs(v, visited, adj):
    print("<bfs> 1. v = {0}, visited = {1}, adj ={2}".format(v, visited, adj))
    count = 0
    q = deque([[v, count]])
    while q:
        print("<bfs> 2. q = {0}".format(q))
        value = q.popleft()
        v = value[0]
        count = value[1]
        print("<bfs> 3. value = {0} ///// v = {1}, count = {2}".format(value, v, count))
        print("<bfs> 4. visited = {0}".format(visited))
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])

def solution2(n, edge):
    answer = 0
    visited = [-1] * (n + 1)
    adj = [[] for _ in range(n+1)]
    for e in edge:
        x = e[0]
        y = e[1]
        adj[x].append(y)
        adj[y].append(x)
    bfs(1, visited, adj)
    for value in visited:
        if value == max(visited):
            answer += 1
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution2(n, edge))




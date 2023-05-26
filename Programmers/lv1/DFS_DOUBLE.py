from collections import deque
def bfs(start, visited, graph):
    queue = deque([start])
    result = 1
    visited[start] = True
    while queue:
        print("<bfs> 1. queue = ", queue)
        now = queue.popleft()
        print("<bfs> 2. now = ", now)
        for i in graph[now]:
            print("<bfs> 3. i =", i)
            if visited[i] == False:
                print("<bfs> 4. visited[{0}] = {1}".format(i, visited[i]))
                result += 1
                queue.append(i)
                print("<bfs> 5. queue.append({0}) = {1}".format(i, queue))
                visited[i] = True
    return result

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    print("<solution> 1. graph = ", graph)

    for v1, v2 in wires:
        print("<solution> 2. v1 = {0} / v2 = {1}".format(v1, v2))
        graph[v1].append(v2)
        print("<solution> 3. graph[v1] = ", graph[v1])
        graph[v2].append(v1)
        print("<solution> 4. graph[v2] = ", graph[v2])

    for start, not_visit in wires:
        print("<solution 5. start = {0} / not_visit = {1}".format(start, not_visit))
        visited = [False] * (n+1)
        print("<solution> 6. visited = ", visited)
        visited[not_visit] = True
        result = bfs(start, visited, graph)
        print("<solution> 7. result = ", result)
        if abs(result - (n-result)) < answer:
            print("<solution> abs(result({0}) --- (n({1}) - result({2})".format(result, n, result))
            answer = abs(result - (n - result))
    return answer

def solution2(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        print(s)
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2*len(s)-n))
    return ans

n = 7
wires = [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]
print(solution2(n, wires))
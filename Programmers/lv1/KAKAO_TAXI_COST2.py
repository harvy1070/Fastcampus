import heapq
def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    # print("graph = {0}".format(graph))
    for f in fares:
        print("<solution/for> 1. f = {0}".format(f))
        x, y, z = f[0], f[1], f[2]
        graph[x].append((y, z))
        graph[y].append((x, z))
        # print("<solution/for> 2. graph[x] = {0} / graph[y] = {1}".format(graph[x], graph[y]))
        print("<solution/for1> 2-1. graph[x] = {0}".format(graph[x]))
        print("<solution/for1> 2-2. graph[y] = {0}".format(graph[y]))
    def dijkstra(n, start, end):
        print("<dijkstra> 1. n:{0} / start:{1} / end:{2}".format(n, start, end))
        distance = [20000000 for _ in range(n+1)]
        q = []
        heapq.heappush(q, (0, start))
        print("<dijkstra> 2. q = {0}".format(q))
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q)
            print("<dijkstra/while> 3. dist = {0} / now = {1}".format(dist, now))
            if distance[now] < dist:
                print("<dijkstra/while/if> 4. distance = {0} < dist = {1} // now = {2}".format(distance, dist, now))
                continue
            for i in graph[now]:
                print("<dijkstra/while/for> 5-1. graph = {0} / now = {1}".format(graph, now))
                cost = dist + i[1]
                print("<dijkstra/while/for> 5-2. cost = {0}".format(cost))
                if cost < distance[i[0]]:
                    print("<dijkstra/while/for/if> 6-1. cost:{0} < distance[i[0]]:{1}".format(cost, distance[i[0]]))
                    distance[i[0]] = cost
                    print("<dijkstra/while/for/if> 6-2. distance[i[0]] = {0}".format(cost))
                    heapq.heappush(q, (cost, i[0]))
                    print("<dijkstra/while/for/if> 6-3. q = {0}".format(q))
                    print("<dijkstra/while/for/if> 6-4. distance = {0}".format(distance))
        return distance[end]

    result = []
    for p in range(1, n+1):
        if p != s:
            print("<solution/for2/if> 3-1. p:{0} != s:{1}".format(p, s))
            s_to_p = dijkstra(n, s, p)
            print("<solution/for2/if> 4-1. s_to_p = {0}".format(s_to_p))
            p_to_a = dijkstra(n, p, a)
            print("<solution/for2/if> 4-2. p_to_a = {0}".format(p_to_a))
            p_to_b = dijkstra(n, p, b)
            print("<solution/for2/if> 4-3. p_to_b = {0}".format(p_to_b))
            result.append(s_to_p + p_to_a + p_to_b)
            print("<solution/for2/if> 5-1. result = {0}".format(result))
        else:
            result.append(dijkstra(n, s, a) + dijkstra(n, s, b))
            print("<solution/for2/else> 3-2. p:{0} == s:{1}".format(p, s))
            print("<solution/for2/else> 5-2. result = {0}".format(result))
    return min(result)


n = 6 # 지점 갯수
s = 4 # 출발 지점
a = 6 # A의 도착지
b = 2 # B의 도착지
# 지점 사이 예상 요금
fares = [[4, 1, 10], [3, 5, 24],
         [5, 6, 2], [3, 1, 41],
         [5, 1, 24], [4, 6, 50],
         [2, 4, 66], [2, 3, 22],
         [1, 6, 25]]

print(solution(n, s, a, b, fares))
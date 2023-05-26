import heapq
def solution(n, s, a, b, fares):
    def dijkstra(start):
        res = [float('INF') for _ in range(n + 1)]
        res[start] = 0
        #print("================== res : {0} ==================".format(res))
        q = []
        # print("<dijkstra> 5. start = {0}".format(start))
        heapq.heappush(q, (res[start], start))
        # print("<dijkstra> 6. heapq.heappush({0}, ({1}, {2}))".format(q, res[start], start))
        while q:
            print("=============== q = {0} ===============".format(q))
            # print("<dijkstra> 7. q = {0}".format(q))
            result_x, x = heapq.heappop(q)
            # print("<dijkstra> 8. result_x = {0}, x = {1}, graph[x] = {2}".format(result_x, x, graph[x]))
            for fu, fw in graph[x]:
                print("<dijkstra> 9. fu = {0}, fw = {1}, res = {2}".format(fu, fw, res))
                if res[fu] > result_x + fw:
                    print("<dijkstra> 10. (if) res[{0}] > result_x:{1} + fw:{2}".format(fu, result_x, fw))
                    res[fu] = result_x + fw

                    heapq.heappush(q, ([res[fu], fu]))
                    print("<dijkstra> 11. heapq.heappush({0}, ([{1}, {2}]))".format(q, res[fu], fu))
                    print("<dijkstra> 12. q = {0}".format(q))
        return res
    ans = 200000001
    graph = [[] for _ in range(n+1)]
    #print("<solution> 1. graph = {0}".format(graph))
    for i, j, c in fares:
        # print("<solution> 2-1. i = {0}, j = {1}, c = {2}".format(i, j, c))
        # print("<solution> 2-2. graph = {0}".format(graph))
        graph[i].append((j, c))
        graph[j].append((i, c))
        # print("<solution> 3-1. graph[{0}] = {1}".format(i, graph[i]))
        # print("<solution> 3-2. graph[{0}] = {1}".format(j, graph[j]))
    dist = [[]]
    for i in range(1, n+1):
        print("<solution> 4. dist = {0}".format(dist))
        dist.append(dijkstra(i))

    for i in range(1, n+1):
        print("<solution> 12. ans = {0}".format(ans))
        ans = min(ans, dist[s][i] + dist[i][a] + dist[i][b])
    return ans

def solution2(n, s, a, b, fares):
    ans = 200000001
    cost = [[ans] * (n+1) for _ in range(n + 1)]
    #print("<solution2> 1. cost = {0}".format(cost))
    def floyd_warshall():
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    print("<floyd> 1. k:{0} , i:{1} , j:{2}".format(k, i, j))
                    if i == j:
                        print("<floyd> (if) i:{0} == j:{1}".format(i, j))
                        cost[i][j] == 0
                        print("<floyd> (if) cost[{0}][{1}] == 0".format(i, j))
                    else:
                        cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j])
                        print("<floyd> (else) cost[i][j] = min(cost[i][k] + cost[k][j], cost[i][j]")
                        print(">>> cost[{0}][{1}] = min(cost[{0}][{2}]:{3} + cost[{2}][{1}]:{4}, cost[{0}][{1}]:{5}".format(
                            i, j, k, cost[i][k], cost[k][j], cost[i][j]
                        ))
    #print("=============== 1. cost = {0} ===============".format(cost))
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
    #print("<solution> 2. cost = {0}".format(cost))
    floyd_warshall()

    #print("=============== 2. cost = {0} ===============".format(cost))
    for i in range(1, n+1):
        ans = min(cost[s][i] + cost[i][a] + cost[i][b], ans)
        print()
    return ans


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10],
         [3, 5, 24],
         [5, 6, 2],
         [3, 1, 41],
         [5, 1, 24],
         [4, 6, 50],
         [2, 4, 66],
         [2, 3, 22],
         [1, 6, 25]]
print(solution2(n, s, a, b, fares))
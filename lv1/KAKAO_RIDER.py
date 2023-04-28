import heapq
def dijkstra(dist, adj):
    heap = [] # 출발 노드 기준으로 각 노드들의 최소 비용 탐색
    heapq.heappush(heap, [0, 1]) # 거리, 노드
    print("<dijkstra> 1. heapq = ", heapq)
    while heap:
        print("<dijkstra> 2. heap = ", heap)
        cost, node = heapq.heappop(heap)
        print("<dijkstra> 3. cost = {0} / node = {1}".format(cost, node))
        for c, n in adj[node]:
            print("<dijkstra> 4. c = {0} / n = {1} ** adj[node]".format(c, n))
            if cost+c < dist[n]:
                print("<dijkstra> 5. cost+c = {0} / dist[{1}] = {2}".format(cost+c, n, dist[n]))
                dist[n] = cost+c
                print("<dijkstra> 6. dist[{0}] = {1}".format(n, dist[n]))
                heapq.heappush(heap, [cost+c, n])
                print("<dijkstra> 7. heapq.heappush(heap({0}), [cost+c({1}), n({2})]".format(heap, cost+c, n))

def solution(N, road, K):
    dist = [float('inf')] * (N+1) # dist 배열 만들고 최소거리 갱신
    print("<solution> 1. dist = ", dist)
    dist[1] = 0 # 자기 자신이므로 거리 0
    adj = [[] for _ in range(N+1)] # 인접 노드 거리 기록할 배열
    print("<solution> 2. adj = ", adj)
    for r in road:
        print("<solution> 3. r = ", r)
        adj[r[0]].append([r[2],r[1]])
        print("<solution> 4. adj[{0}].append([{1}, {2}]) = {3}".format(r[0], r[2], r[1], adj[r[0]]))
        adj[r[1]].append([r[2],r[0]])
        print("<solution> 5. adj[{0}].append([{1}, {2}]) = {3}".format(r[1], r[2], r[0], adj[r[1]]))
    dijkstra(dist, adj)
    return len([i for i in dist if i <= K])

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3

print(solution(N, road, K))